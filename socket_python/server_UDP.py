# -*- coding: utf-8 -*-
# include Python's socket library
from socket import *

serverPort = 12000

# create UDP socket
# In C: int socket(int family, int type, int protocol);
serverSocket = socket(AF_INET, SOCK_DGRAM)

# bind socket to local port number 12000
# In C: int bind(int sockfd, struct sockaddr *myaddr, int addrlen);
serverSocket.bind(('', serverPort))
print('The server is ready to receive')

# Loop forever
while True:
   # Read from UDP socket into message
   # getting client IP and port
   # In C: int recvfrom(int sockfd, char *buff, int nbytes, int flags, struct sockaddr *from, int *addrlen);
   message, clientAddress = serverSocket.recvfrom(2048)
   print('Received "%s" from the client with address %s' % (message.decode(), clientAddress))
   
   # Convert message to upper case
   modifiedMessage = message.upper()
   
   # Send back modified string to client
   serverSocket.sendto(modifiedMessage, clientAddress)
