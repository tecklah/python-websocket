from confluent_kafka import Consumer, KafkaError
import asyncio
import websockets

kafkaconsumer = Consumer({
    'bootstrap.servers': '127.0.0.1',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'
})

kafkaconsumer.subscribe(['test'])


async def consumerhandler(websocket):
    try:
        message = await asyncio.wait_for(websocket.recv(), 1)
        print("Incoming message:", message)
    except asyncio.TimeoutError:
        pass
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)


async def producerhandler(websocket):

    # Poll Kafka for new message
    kafkamessage = kafkaconsumer.poll(1.0)

    if kafkamessage is None:
        return
    elif not kafkamessage.error():

        outgoingmessage = kafkamessage.value().decode('utf-8')
        print("Sending out Kafka message: ", outgoingmessage)

        # Send out Kafka message to existing web sockets
        await websocket.send(outgoingmessage)

    elif kafkamessage.error().code() == KafkaError._PARTITION_EOF:
        print('End of partition reached {0}/{1}'.format(kafkamessage.topic(), kafkamessage.partition()))
    else:
        print('Error occurred: {0}'.format(kafkamessage.error().str()))

async def connectwebsocket():
    try:
        async with websockets.connect('ws://127.0.0.1:8081/wsocket') as websocket:

            while True:

                #asyncio.gather(consumerhandler(websocket), producerhandler(websocket))

                consumertask = asyncio.create_task(consumerhandler(websocket))
                producertask = asyncio.create_task(producerhandler(websocket))
                done, pending = await asyncio.wait([producertask, consumertask], return_when=asyncio.ALL_COMPLETED,)
                for task in pending:
                    print("Cancelling")
                    task.cancel()

                print("Running")
                await asyncio.sleep(0.1)

    except websockets.exceptions.InvalidHandshake:
        print('Exception raised when a handshake request or response is invalid.')
    except websockets.exceptions.InvalidURI:
        print('Exception raised when an URI isn’t a valid websocket URI.')
    except websockets.exceptions.InvalidStatusCode:
        print('Handshake responce status code is invalid')
    except Exception as e:
        print('Error in making the Websocket Connection!!')
        print(e.args)

    kafkaconsumer.close()

asyncio.get_event_loop().run_until_complete(connectwebsocket())
asyncio.get_event_loop().run_forever()


