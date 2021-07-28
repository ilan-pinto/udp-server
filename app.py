

from socket import *
import os
import SampleApp
import logging
import sys
import struct 

from Config import PORT , MCAST_GRP




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

# Enable broadcasting mode
# serverSocket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

# Assign IP address and port number to socket
serverSocket.bind(('', PORT))
mreq = struct.pack('4sl', socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)
serverSocket.setsockopt(IPPROTO_IP, IP_ADD_MEMBERSHIP, mreq)


logging.info("UDP server up and listening")
app = SampleApp.SampleApp(serverSocket,os.environ.get('LEADER_IP'))
while(True):
    
    bytesAddressPair = serverSocket.recvfrom(1024)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = "Message from Client:{}".format(message)
    clientIP  = "Client IP Address:{}".format(address)    
    logging.info(clientMsg)
    logging.info(clientIP)


    logging.info(" {} starting to process message ".format(app.my_ip))

    try:
        app.process_message(message)
    except Exception as e :
        logging.error(e)
          


s

