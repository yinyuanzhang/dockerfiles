FROM ubuntu:16.04
MAINTAINER Shafqat Ahmed

RUN   apt update && \
      apt install -y  build-essential libssl-dev nano wget git curl  && \
      cd /tmp && \      
      wget https://deb.nodesource.com/setup_6.x && \ 
      chmod +x setup_6.x && \
      ./setup_6.x && \
      apt install nodejs -y && \
      npm install forever -g && \
      npm install nodemon -g && \
      apt install net-tools -y && \
      wget -O jq https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64 && \
      chmod +x ./jq && \
      cp jq /usr/bin