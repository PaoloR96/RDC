# -*- coding: utf-8 -*-
# include Python's socket library
from socket import *

serverPort = 12000

# create TCP socket
# In C: int socket(int family, int type, int protocol);
serverSocket = socket(AF_INET, SOCK_STREAM)

# bind socket to local port number 12000
# In C: int bind(int sockfd, struct sockaddr *myaddr, int addrlen);
serverSocket.bind(('', serverPort))

# put socket in passive mode
# In C: int listen(int sockfd, int qlen);
serverSocket.listen(1)
print('The server is ready to receive')

# Loop forever
while True:
   # server waits for incoming connections on accept() 
   # for incoming requests, new socket created on return
   # In C: int accept(int sockfd, struct sockaddr *peer, int *addrlen);
   connectionSocket, addr = serverSocket.accept()
   print('Accepted connection. Connection socket created: ', connectionSocket)
   
   # receive sentence on newly established connectionSocket
   sentence = connectionSocket.recv(1024)
   print('Sentence received:', sentence.decode())
   
   # convert message to upper case
   modifiedSentence = sentence.upper()
   
   # send back modified string to client
   # In C: int send(int sockfd, char *buff, int nbytes, int flags);
   connectionSocket.send(modifiedSentence)
   
   # Close connection socket
   # In C: int close(int fd);
   connectionSocket.close()
