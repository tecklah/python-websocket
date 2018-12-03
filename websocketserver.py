# Create a web socket server

import asyncio
import logging
import websockets
import json

connectedWebsocket = set()


async def sendmessage(websocket, message):
    try:
        await websocket.send(message)
    except websockets.exceptions.ConnectionClosed as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
        connectedWebsocket.remove(websocket) # Remove the connection


async def websockethandler(websocket, path):

    # Set consists of only unique objects
    connectedWebsocket.add(websocket)

    print("New connection. Total : ", len(connectedWebsocket))

    if path == '/wsocket':
        while True:

            try:
                async for message in websocket:

                    print("Incoming message: ", message)

                    if connectedWebsocket is not None and len(connectedWebsocket) > 0:
                        print("There are {} web sockets.".format(len(connectedWebsocket)))
                        await asyncio.wait([sendmessage(ws, message) for ws in connectedWebsocket])

            except websockets.exceptions.ConnectionClosed as ex:
                connectedWebsocket.remove(websocket)  # Remove the connection
                print("Connection removed. Total : ", len(connectedWebsocket))
                break

    else:
        pass

logger = logging.getLogger('websockets.server')
logger.setLevel(logging.ERROR)
logger.addHandler(logging.StreamHandler())

start_server = websockets.serve(websockethandler, '127.0.0.1', 8081)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
