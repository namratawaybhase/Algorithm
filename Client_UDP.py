from socket import *
serverPort = 12000
clientSocket =socket(AF_INET, SOCK_DGRAM)
clientSocket.bind(('',5432))
message = input("Input lowercase: ")
clientSocket.sendto(message.encode(),(severName,serverPort))
modifiedMessage,severAddress = clientSocket.recvfrom(1024)
msg=modifiedMessage.decode()
print (msg)
clientSocket.close()