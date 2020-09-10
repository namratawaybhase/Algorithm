from socket import *
ServerPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('localhost', 12000))
sentence = input("Input lower case sentence:")
serverSocket.sendall(sentence.encode())
modifiedSentence = severSocket.recv(1024)
print("From Server:", modifiedSentence.decode())
severSocket.close()
