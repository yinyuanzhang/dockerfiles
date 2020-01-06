FROM ubuntu:18.04

RUN apt update
RUN apt install curl -y

RUN mkdir /data
COPY ./script.sh /data/script.sh


CMD ["/bin/bash", "/data/script.sh"]
