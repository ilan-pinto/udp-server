FROM registry.access.redhat.com/ubi8/python-38
RUN cd /home
RUN mkdir reciver-app 
WORKDIR /home/reciver-app 
ADD app.py Config.py /home/reciver-app/
CMD ["python", "app.py"]

