# CLI-TCP-ChatRoom-Application
This repository contains the code for implementing a command line interfaced TCP Chatroom Application. This fully-functioning TCP chat will have one server that hosts the chat and multiple clients that are connected to it and communicate with each other. This is implemented as a client-server architecture, that is multiple clients (the users) and one central server that hosts everything and provides the data for these clients.

[PEP 8](https://www.python.org/dev/peps/pep-0008/) Python style guide is followed for all codes in python

### Contents
* [Getting started](#getting-started)
* [Instructions](#instructions-to-use)
* [Approach](#approach-followed-to-implement)
* [References](#references)

## Getting started
* Install Python3 - Follow this [link](https://www.python.org/downloads/) to download and install Python3
* Install pip - Follow this [link](https://pip.pypa.io/en/stable/installation/) to install pip 
* Install Colorama - Run the following command to install the package
```
pip install colorama
```
* Run the below command to copy the source code locally (Assuming git is installed)
```
git clone https://github.com/RAGUL1902/CLI-TCP-ChatRoom-Application.git
```
* Now the complete source code is setup on your local computer and ready to run.
* Run server.py in a terminal first and then client.py in multiple other terminal using the following commands.
```
python3 server.py
```
```
python3 client.py
```
* Now the clients can interact with each other using the server.

## Instructions to Use
* Client will be asked to enter a username before connecting to the chatroom.
* Server is the admin, which can either accept or reject the request of the client to join.
* Once the client is accepted into the chatroom, all the messages sent is broadcasted to every other client by default
* Client can use the command ```/color <colorname> <message> ``` to send the message in different colors.
* Available colors are red, green, yellow, blue, megenta, cyan and white.
* To send a private message to a user the command ```/private <username> <message>``` can be used.
* Both the commands can be combined like ```/private <username> /color <colorname> <message>``` to send a colored message to a private user
* The command ```/leave``` can be used to leave the chat. When a client leaves the chat, the same in announced to the rest of the clients.

## Approach followed to implement
The socket library in python is used to implement socket programming in a client-server architecture. The ```/color``` and ```/leave``` command is implemented in ```client.py``` whereas the ```/private``` command is implemented in ```server.py```. Seperate functions are made for every implemented feature. 

### Server.py
* Server.py acts as a server to manage different clients. It is responsible for recieving the messages from a client and broadcast it to other clients.
* It maintains the list of connection sockets of the clients present in the chatroom. It also maintains their respective usernames and addresses.
* Server creates a seperate thread for every connected client, so receiving and sending messages between mutiple clients becomes independent of the presence of other clients.
* The private message functionality is also implemented in the ```server.py```.
* The private message is sent to the desired client by finding it's connection socket from the list using it's username.

### Client.py
* The client program has two seperate function for sending and receiving messages from the server.
* Those two functions are run in seperate threads so they can send and receive messages of independent of each other.
* A seperate function is created to validate the incoming message so as to find if it should be outputed in a different color.
* The client also checks for the ```/leave``` command, on which finding it will close the connection socket.

## References
* [Sockets in python](https://docs.python.org/3/howto/sockets.html)
* [Socket programming python - GeeksforGeeks](https://www.geeksforgeeks.org/socket-programming-python/)
* [Threading in python - GeeksforGeeks](https://www.geeksforgeeks.org/multithreading-python-set-1/)
* [Colorama in python](https://pypi.org/project/colorama/)
* [Stackoverflow]()

   
