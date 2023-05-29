# -*- coding: utf-8 -*-
# include Python's socket library
from socket import *

serverName = 'localhost'
serverPort = 12000

# create TCP socket
# In C: int socket(int family, int type, int protocol);
clientSocket = socket(AF_INET, SOCK_STREAM)

# connect socket to remote server at (serverName, serverPort)
# In C: int connect(int sockfd, struct sockaddr *servaddr, int addrlen);
clientSocket.connect((serverName, serverPort))

# get user keyboard input 
sentence = input('Input lowercase sentence: ')

# Send sentence into socket, no need to specify server IP and port
# In C: int send(int sockfd, char *buff, int nbytes, int flags);
clientSocket.send(sentence.encode())

# read reply message from socket into modifiedMessage string
modifiedSentence = clientSocket.recv(1024)

# Print out received modifiedMessage string
print('Sentence received:', modifiedSentence.decode())

# Close socket
# In C: int close(int fd);
clientSocket.close()
