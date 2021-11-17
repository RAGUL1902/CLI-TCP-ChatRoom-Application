import socket
import threading

serverPort = 1234
serverAddress = socket.gethostbyname(socket.gethostname())
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((serverAddress, serverPort))
serverSocket.listen()

addrToUserName = {}
userNameToAddr = {}
connectedClients = {}

CONST_WELCOME_MESSAGE = "Welcome to the chatroom, to continue enter your username: "
CONST_OPTIONS_MESSAGE = "You are added to the chatroom. Messages you send is broadcasted to other users." 
CONST_OPTIONS_MESSAGE +="\nTo send a private message use the following format: /private <username> <message>"
CONST_OPTIONS_MESSAGE +="\nTo send messages in different colors, use the command: /color <colorname> <message>"
CONST_OPTIONS_MESSAGE +="\nTo send a private message in different colors, use the command: /private <username> /color <colorname> <message>"
CONST_OPTIONS_MESSAGE +="\nTo leave the chat, use the command: /leave"

def isUserAllowed(connectionSocket, userName):
    while True:
        inputCommand = input(
            f'{userName} wants to join chat. (y = allow/ n = reject): ')
        
        if(inputCommand == "y"):
            return True

        if(inputCommand == 'n'):
            return False
        
        print(f'Invalid Command \n')


def sendToAllClients(message, senderConnSocket):
    
    for addr in connectedClients:
        
        if connectedClients[addr] is not senderConnSocket:
            connectedClients[addr].send(message)


def sendPrivateMessage(msgList, connectionSocket):
    message = msgList[0] + " " + ' '.join(msgList[3:])
    connectionSocket.send(message.encode())


def manageClients(connectionSocket, addr):
    while True:
        try:
            msgForAll = addrToUserName[str(
                addr)] + ': ' + connectionSocket.recv(1024).decode()
            msgList = msgForAll.split()
            
            if(len(msgList) >= 3 and msgList[1] == "/private"):
                if msgList[2] in userNameToAddr:
                    sendPrivateMessage(
                        msgList, connectedClients[userNameToAddr[msgList[2]]])
            else:
                sendToAllClients(msgForAll.encode(), connectionSocket)
        
        except:
            sendToAllClients(
                (addrToUserName[str(addr)] + ' left the chat.').encode(), connectionSocket)
            
            userNameToAddr.pop(addrToUserName[str(addr)])
            addrToUserName.pop(str(addr))
            connectedClients.pop(str(addr))
            
            connectionSocket.close()
            break


def startServer():
    while True:
        connectionSocket, addr = serverSocket.accept()
        
        msg = CONST_WELCOME_MESSAGE
        connectionSocket.send(msg.encode())
        userName = connectionSocket.recv(1024).decode()
        userName = ''.join(userName.split())
        
        if(isUserAllowed(connectionSocket, userName)):
            print(userName, 'has connected with the server.')

            addrToUserName[str(addr)] = userName
            userNameToAddr[userName] = str(addr)
            connectedClients[str(addr)] = connectionSocket
            
            sendToAllClients(
                (userName + ' entered the chatroom.').encode(), connectionSocket)
            
            connectionSocket.send(CONST_OPTIONS_MESSAGE.encode())

            thread = threading.Thread(
                target=manageClients, args=(connectionSocket, addr))
            thread.start()
        
        else:
            msg = "Sorry the user deined your request. Try again later"
            connectionSocket.send(msg.encode())
            connectionSocket.close()


print('Server is ready to welcome clients.')
startServer()
