FROM ubuntu:18.04
MAINTAINER koo <kookh0987@gmail.com>

# Avoding user interaction with tzdata
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN apt-get install  -y python3.6
RUN apt-get install  -y python3-pip

RUN pip3 install --no-cache-dir tensorflow
RUN apt-get install  -y python3-flask
RUN pip3 install keras
RUN apt-get install nano
RUN apt install -y git 
