# python-websocket
A sample project using Python to create a web socket server and a Kafka listener that push streaming data to the web socket server.

Step 1 : Install Kafka on the computer and create a new topic 'test'. See https://kafka.apache.org/quickstart
Step 2 : Install PyCharm and create a new Python project.
Step 3 : Copy both files into the project.
Step 4 : Startup the web socket server on the same machine using 127.0.0.1:8081.
Step 5 : Startup the Kafka listener to poll data from 'test' topic and send them to the web socket server.

You can create a front-end HTML page that connects to the web socket server and display any incoming data from the web socket server. A sample of the HTML page will be make available when ready.
