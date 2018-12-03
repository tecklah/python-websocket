# python-websocket
A sample project using Python to create a web socket server and a Kafka listener that push streaming data to the web socket server.

1. Install Kafka on the computer and create a new topic 'test'. See https://kafka.apache.org/quickstart
2. Install PyCharm and create a new Python project.
3. Copy the files into the project.
4. Startup the web socket server "websocketserver.py" on the same machine using 127.0.0.1:8081.
5. Startup the Kafka listener "kafkalistener.py" to poll data from 'test' topic and send them to the web socket server.
6. Startup the sample web application "app.py" to run on port 127.0.0.1:8080.

The sample web application gets data via web socket from the server. The Kafka listener send data to the web socket server when the interval polling managed to retrieve data from Kafka server.
