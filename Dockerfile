FROM nginx
RUN apt update 
RUN apt install net-tools iputils-ping install dnsutils socat netcat -y
ENTRYPOINT ["tail"]
CMD ["-f","/dev/null"]