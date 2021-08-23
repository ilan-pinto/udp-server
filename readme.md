# UDP Headless Server 

UDP server is a demo code for broadcasting messages using headless service on OpenShift/Kubernetes.

### The Problem
UDP broadcasting might expose significant network security risks like UDP flooding. Therefore, in many cases, broadcasting addresses are blocked.

### What is headless service? 
Headless service Kubernetes doesn’t allocate a dedicated cluster IP or performs load balancing. Instead, all the pods assigned to the service will connect to the service, pod's IP will become the A records of the services.
A service can broadcast to all pods by using nslookup on the service name 
- [Headless Service](https://kubernetes.io/docs/concepts/services-networking/service/#headless-services) 
- [Discovering Running Pods By Using DNS and Headless Services in Kubernetes](https://medium.com/swlh/discovering-running-pods-by-using-dns-and-headless-services-in-kubernetes-7002a50747f4) 





## Use case 
After deploying this example, two apps will be deployed : 
- Sender-app - a python script that gets two params: service name, message to broadcast. sender app will discover all the hosts DNS broadcast the message to all hosts.   
- Receiver-app - a python app that listens on port 12000 and processes received messages 



## How to? 


### Testing on your local computer 
To test the receiver app on your local computer:
note! The below command is not using a headless service. 

1. start the receiver app `python receiver-app/app.py` 
1. open a second terminal and exec the `NC -u 127.0.0.1 12000`
1. messages will be sent to the receiver-app

### Containerizing the apps 
In one of the apps folders, you can find a Dockerfile. Build the images if needed or use the one that exists in quay.io 
quay.io/ilan_pinto/senderapp 
quay.io/ilan_pinto/reciverapp

### How to deploy? 
1. clone this repo to your github
1. login to OpenShift using the `oc login` command 
1. create new project using the `oc new-project` command 
1. deploy the template `oc create -f deployments/Deploy.yaml`
1. process template and deploy `oc process udp-broadcasting | oc create -f -`
1. login to the sender pod `oc exec -i -t sender-app -- sh` 
1. broadcast message in the network `python app.py -s headless-udp -m 'brodacsting'` 
you should see a meesage like this 
    >   2021-08-02 12:44:46,383 - root - INFO - sent message to :10.128.5.167
    >   2021-08-02 12:44:46,383 - root - INFO - sent message to :10.128.5.165
1. check logs of udp pods `oc logs statefulset-udp-server-0` , `oc logs statefulset-udp-server-1`
in the logs you should see 
    >   2021-08-02 12:44:46,386 - root - INFO - got message:b'brodacsting' 

### Another option (running from terminal)
1. clone this repo to your GitHub
1. login to OpenShift using the `oc login` command 
1. create new project using the `oc new-project headless-demo` command
1. deploy the services & pods `oc create -f deployments`
1. validate pods are created `oc get pods` - you should see 3 pods - 1 sender-app, 2 receiver-app  
1. run the following command from terminal `oc exec sender-app -- sh -c "python app.py -s headless-udp -m test”` 
1. check logs of receiver-app pods  `oc logs statefulset-UDP-server-1` you should see: 
    >   2021-08-22 20:20:56,167 - root - INFO - Message from Client:b'test' Client IP Address:('10.130.3.209', 38063)

1. now scale up statefulset-UDP-server to 5 pods and try again to send broadcast a message using the sender-app. Check logs of the new and old pods.   