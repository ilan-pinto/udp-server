FROM nginx
RUN apt update 
RUN apt install net-tools -y
RUN apt install dnsutils -y
ENTRYPOINT ["tail"]
CMD ["-f","/dev/null"]