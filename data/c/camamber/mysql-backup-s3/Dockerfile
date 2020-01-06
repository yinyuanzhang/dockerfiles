FROM ubuntu:latest
LABEL maintainer="Camamber"

RUN apt-get update && apt-get install curl sudo -y
RUN curl -sL https://deb.nodesource.com/setup_10.x | sudo bash -
RUN sudo apt-get install nodejs -y

RUN useradd -m -s /bin/bash dumper
USER dumper

COPY . /home/dumper
WORKDIR /home/dumper

RUN npm install

ENTRYPOINT [ "node", "index.js" ]