import socket
import threading

serverAddress = socket.gethostbyname(socket.gethostname())
serverPort = 1234
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverAddress, serverPort))

def receiveMessage():
    while True:
        try:
            msgFromServer = clientSocket.recv(1024).decode()
            print(msgFromServer)
        except:
            clientSocket.close()
            break

def sendMessage():
    while True:
        try:
            msgForServer = input()
            clientSocket.send(msgForServer.encode())
        except:
            clientSocket.close()
            break

receiveMessageThread = threading.Thread(target=receiveMessage)
receiveMessageThread.start()

sendMessageThread = threading.Thread(target=sendMessage)
sendMessageThread.start()