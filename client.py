# Importing the required libraries
import socket
import threading
from colorama import Fore, Back, Style

# Setting up the required things for the socket
serverAddress = socket.gethostbyname(socket.gethostname())
serverPort = 1234
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverAddress, serverPort))

# Fucntion to analyse the incoming msg and print in the respective color
def printMessage(message):
    
    msgList = message.split()
    if(len(msgList) >= 3 and msgList[1] == "/color"):

        if(msgList[2] == "red"):
            print(Fore.RED,end="")

        elif(msgList[2] == "green"):
            print(Fore.GREEN,end="")

        elif(msgList[2] == "yellow"):
            print(Fore.YELLOW,end="")

        elif(msgList[2] == "blue"):
            print(Fore.BLUE,end="")

        elif(msgList[2] == "megenta"):
            print(Fore.MAGENTA,end="")

        elif(msgList[2] == "cyan"):
            print(Fore.CYAN,end="")

        elif(msgList[2] == "white"):
            print(Fore.WHITE,end="")

        else:
            print(message)
            return

        message = msgList[0] + ' '.join(msgList[3:])
        print(message)
        print(Style.RESET_ALL,end="")
    else:
        print(message)
        return

# Fucntion to receive the messages from the server, it is made to run in a seprate thread
def receiveMessage():
    while True:
        try:
            msgFromServer = clientSocket.recv(1024).decode()
            # print(msgFromServer)
            printMessage(msgFromServer)
        except:
            clientSocket.close()
            return


# Function to send the inputed msg by te client to the server
def sendMessage():
    while True:
        try:
            msgForServer = input()

            if("/leave" == (msgForServer.split())[0]):
                clientSocket.close()

            clientSocket.send(msgForServer.encode())
        except:
            clientSocket.close()
            return


# Starting two seperate threads for sending and receiving messages
receiveMessageThread = threading.Thread(target=receiveMessage)
receiveMessageThread.start()

sendMessageThread = threading.Thread(target=sendMessage)
sendMessageThread.start()
