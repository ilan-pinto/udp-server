
# UDP Headless Server 

UDP server is sample for headless service on OpenShift/kubernetes.
Headless service exposes all DNS hosts which are basicly the pods liked to the service. 
a service can broadcast to all pods by using nslookup on the service name 
- [Headless Service](https://kubernetes.io/docs/concepts/services-networking/service/#headless-services) 
- [Discovering Running Pods By Using DNS and Headless Services in Kubernetes](https://medium.com/swlh/discovering-running-pods-by-using-dns-and-headless-services-in-kubernetes-7002a50747f4) 





## Use case 
after deploying this example you will have two apps: 
- sender-app - a python script that gets 2 params: service name, message to broadcast. sender app will discover all the hosts dns broadcast the message to all hosts.   
- reciver-app - a python app that listens on port 12000 and process recived messages 



## How to? 


### Testing on your local computer 
for testing the reciver app on your local computer:
note! the below commad is not using a headless service. 

1. start the reciver app `python reciver-app/app.py` 
1. open a secound terminal and exec the `nc -u 127.0.0.1 12000`
1. every line will be sent to the reciver-app

### Containerizing the apps 


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





<!-- #### On open shift 
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
> oc get pod {pod_name} -o jsonpath='{range .items[*]}{.spec.nodeName}{"\n"}'  -->


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



### notes 
- headless service only picks the first DNS it Doesn’t to all pods -https://faun.pub/kubernetes-headless-service-vs-clusterip-and-traffic-distribution-904b058f0dfd 

- Headless services still provide load balancing across pods but through the DNS round-robin mechanism instead of through the service proxy.




'''