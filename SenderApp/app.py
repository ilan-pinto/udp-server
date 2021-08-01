import logging
import sys
import argparse
from socket import *  
from Config import PORT 

#configure log
sender = logging.getLogger()
sender.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
sender.addHandler(handler) 


parser = argparse.ArgumentParser(prog='UDP packets boradcaster')
parser.add_argument('-s','--service',action='store', dest='service_name', help='headless service name')
parser.add_argument('-m','--message',action='store', dest='message', help='headless service name')

input = parser.parse_args()

service_name = input.service_name
broadcast_message = input.message

# Create a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM,IPPROTO_UDP)
 

# extract all ip 
ip_list = list({addr[-1][0] for addr in getaddrinfo(input.service_name, 0, 0, 0, 0)})

for ip in ip_list: 
    serverSocket.sendto(str.encode(broadcast_message),(ip,PORT))
    logging.info('sent message to :{}'.format(ip) )
    
