# python-websocket
A sample project using Python to create a web socket server and a Kafka listener that push streaming data to the web socket server.

1. Install Kafka on the computer and create a new topic 'test'. See https://kafka.apache.org/quickstart
2. Install PyCharm and create a new Python project.
3. Copy both files into the project.
4. Startup the web socket server on the same machine using 127.0.0.1:8081.
5. Startup the Kafka listener to poll data from 'test' topic and send them to the web socket server.

You can create a front-end HTML page that connects to the web socket server and display any incoming data from the web socket server. 

A sample Python web application that get data via web socket from the server is available in source folder.
