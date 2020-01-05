FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \ 
    apt-get install -y \
    wget \
    git \
    awscli && \
    wget -P /tmp/ https://nodejs.org/download/release/v4.4.7/node-v4.4.7-linux-x64.tar.gz && \
    tar -C /usr/local --strip-components 1 --overwrite -xzf /tmp/node* && \
    apt-get remove -y wget && \
    rm -rf /var/lib/apt/lists/* /tmp/*

RUN npm install -g gulp bower

CMD ["sh"] 