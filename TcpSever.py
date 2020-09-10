from socket import *
ServerPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', ServerPort))
serverSocket.listen()
connectionSocket,addr = serverSocket.accept()
print("The server is ready to receive ")
while True: 
    sentence =connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()


