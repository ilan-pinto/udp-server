

from socket import *
import os
import SampleApp
import logging
import sys
from Config import PORT




#configure log
root = logging.getLogger()
root.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
root.addHandler(handler) 


# Create a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Assign IP address and port number to socket
serverSocket.bind(('', PORT))

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

