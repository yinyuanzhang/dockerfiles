FROM ubuntu:18.04

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get update && apt-get install -y sshpass ffmpeg openjdk-11-jdk curl 

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash - \
  && apt install -y nodejs 
