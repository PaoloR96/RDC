# -*- coding: utf-8 -*-
# include Python's socket library
from socket import *

serverName = 'localhost'
serverPort = 12000

# create UDP socket
# In C: int socket(int family, int type, int protocol);
clientSocket = socket(AF_INET, SOCK_DGRAM)

# get user keyboard input 
# message = input('Input lowercase sentence: ')
message = input('Input sentence: ')

# Attach server name, port to message; send into socket
# In C: int sendto(int sockfd, char *buff, int nbytes, int flags,
# struct sockaddr *to, int addrlen);
clientSocket.sendto(message.encode(), (serverName, serverPort))

# read reply message from socket into modifiedMessage string
# In C: int recvfrom(int sockfd, char *buff, int nbytes, int flags,
# struct sockaddr *from, int *addrlen);
# modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
echoMessage, serverAddress = clientSocket.recvfrom(2048)

# Print out received echoMessage string
print('Sentence received:', echoMessage.decode())

# Close socket
# In C: int close(int fd);
clientSocket.close()
