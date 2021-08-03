FROM registry.access.redhat.com/ubi8/python-38
RUN cd /home
RUN mkdir sender-app 
WORKDIR /home/sender-app 
ADD app.py Config.py /home/sender-app/
ENTRYPOINT ["tail"]
CMD ["-f","/dev/null"]
