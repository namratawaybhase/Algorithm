from socket import *
severName="www.gmail.com"
serverPort=1200
clientSocket =socket(socket.AF_INET, socket.SOCK_DGRAM)
message = input("input lowercase")
clientSocket.send(message,(severName,serverPort))
modifiedMessage,severAddress =