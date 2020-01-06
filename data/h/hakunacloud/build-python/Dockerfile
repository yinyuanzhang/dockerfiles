FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install -y python3-pip curl gcc g++ make
RUN curl -sL https://deb.nodesource.com/setup_13.x | bash -
RUN apt-get update
RUN apt-get install -y nodejs
RUN pip3 install awscli --upgrade
RUN npm install -g @beekube/cli
