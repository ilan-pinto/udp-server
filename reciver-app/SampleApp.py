import os 
import logging
import json
from Config import PORT


class SampleApp: 
    def __init__(self,serverSocket,leader_ip=None):
        self.am_i_leader = False
        self.leader_ip = leader_ip
        
        self.server = serverSocket
        self.my_ip = os.environ.get('MY_POD_ID') # should be defined in the deployment yaml 
        if self.leader_ip is None: 
            logging.info('leader ip is none useing default ')

    def leader_update(self, new_ip, new_port ):
            self.leader_ip = new_ip
            self.leader_port = new_port
            os.environ['LEADER_IP'] = new_ip
            # os.environ['LEADER_PORT'] = new_port

            if self.my_ip is not None and self.my_ip == self.leader_ip: 
                self.am_i_leader = True



    def process_message(self, msg): 
        logging.info('got message:{}'.format(msg))
        msg_str = msg.decode("utf-8").rstrip('\n') 


        #new leader update. new leader: ip, port
        if msg_str.find('leader') > 0 : 
            new_leader = json.loads(msg_str)           
            new_ip = new_leader['leader']
            self.leader_update(new_ip, PORT )

        elif self.am_i_leader == True: 
              logging.info('Leader {} ***processed*** messsge'.format(self.my_ip) )
        elif self.leader_ip is None : 
            logging.warning('NO Leader configured')
                 
        else: 
            # route to leader            
            self.server.sendto(msg,(self.leader_ip,PORT)) 
            logging.info('Routed messsage to leader') 




