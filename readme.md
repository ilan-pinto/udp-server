
# UDP Headless Server 

UDP server is sample for headless service on OpenShift/kubernetes.
every time a message is published to the service it is not load blanced but sent out to all pods.

## Use case 
A UDP based ecosystem that processed messages. 
incommeing messages are sent out to all of the services but only "leader" service can replay. 
In this case every service should be aware who the "leader" pod   

## Server Features 

- A leader is selected externaly  by adding a specfic IP in the YAMl file or by sending the below UDP messag to the SVC 
all the pods will recive the message and will update the leader localy  
    >    {"leader": "{IP}" }

- All the Pods will than update localy the leader ip 
- All the Pods routing the message to the leader 


## How to? 

### How to deploy? 

#### On open shift 
1. clone this repo to your github
1. login to OpenShift using the `oc login` command 
1. create new project using the `oc new-project` command 
1. create new secret source on OCP 
1. create new app using the `oc new-app` command 
>  oc new-app git@github.com:{github_user_name}/udp-server.git --source-secret={secret_name} --name=udp-server
6. modify deployment yaml port protocol to UDP 
6. modify server yaml to use NodePort and  protocol to UDP 
6. enable multi cast - https://docs.openshift.com/container-platform/4.7/networking/ovn_kubernetes_network_provider/enabling-multicast.html 



### How to test 
On your local computer use the following comman
> nc -u {node_name} {port}

node_name - can be found in the UI on the pod left bottom of the details tab . or using the following command 
> oc get pod {pod_name} -o jsonpath='{range .items[*]}{.spec.nodeName}{"\n"}' 


**TBD**
- leader publishes the message and send back to all pods the leader_list 
- every X seconds pods are checking if leader is a live. https://stackoverflow.com/questions/42867192/python-check-udp-port-open 

- If leader dies all pods starts to send message to next leader in list 

*open items* 
- how does new replice identify leader (maybe perssitantcy)
- discover all pods ip under headlees service using DNS hosts - using python getaddrinfo
   https://medium.com/swlh/discovering-running-pods-by-using-dns-and-headless-services-in-kubernetes-7002a50747f4

- can configmap be update on runtime - answer:no only on restart 


#how to




### commnuitcate 
use your terminal for sending commands to the UDP server 
using nc command 

nc [protocl] [ip] [port]
example nc -u 127.0.0.1 12000
and then type command 

Udp server diagram 




'''