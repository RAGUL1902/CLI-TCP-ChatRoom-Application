import socket
import threading

serverPort = 1234
serverAddress = socket.gethostbyname(socket.gethostname())
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((serverAddress, serverPort))
serverSocket.listen()
userNameList = {}
connectedClients = []

def isUserAllowed(connectionSocket, userName):
    while True:
        inputCommand = input(f'{userName} wants to join chat. (y = allow/ n = reject): ')
        if(inputCommand == "y"):
            return True

        if(inputCommand == 'n'):
            return False
        print(f'Invalid Command \n')


def sendToAllClients(message, senderConnSocket):
    for connectionSocket in connectedClients:
        if connectionSocket is not senderConnSocket:
            connectionSocket.send(message)

def manageClients(connectionSocket, addr):
    while True:
        try:
            msgForAll = userNameList[str(addr)] + ': ' + connectionSocket.recv(1024).decode()
            sendToAllClients(msgForAll.encode(), connectionSocket)
        except:
            sendToAllClients((userNameList[str(addr)] + ' exited the chatroom.').encode(), connectionSocket)
            userNameList.remove(connectionSocket)
            connectionSocket.close()
            break

def startServer():
    while True:
        connectionSocket, addr = serverSocket.accept()
        msg = "Enter your username: "
        connectionSocket.send(msg.encode())
        userName = connectionSocket.recv(1024).decode()
        if(isUserAllowed(connectionSocket, userName)):
            print(userName, 'has connected with the server.')
            userNameList[str(addr)] = userName
            connectedClients.append(connectionSocket)
            sendToAllClients((userName + ' entered the chatroom.').encode(), connectionSocket)
            thread = threading.Thread(target=manageClients, args=(connectionSocket, addr))
            thread.start()
        else:
            msg = "Sorry the user deined "

print('Server is ready to welcome clients.')
startServer()