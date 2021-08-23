
from socket import *
import os
import logging
import sys
import struct 

from Config import PORT , MCAST_GRP


my_ip = os.environ.get('MY_POD_ID')

#configure log
root = logging.getLogger()
root.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
root.addHandler(handler) 



# Create a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM,IPPROTO_UDP)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEPORT, 1)
serverSocket.bind(('', PORT)) 
logging.info("UDP server up and listening")

while(True):    
    bytesAddressPair = serverSocket.recvfrom(1024)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = "Message from Client:{}".format(message)
    clientIP  = "Client IP Address:{}".format(address)    
    logging.info(clientMsg + ' ' + clientIP )
    logging.info(" {} starting to process message {} ".format(my_ip, message ))

          




