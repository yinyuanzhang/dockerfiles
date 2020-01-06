FROM node:latest

MAINTAINER kusu0926

RUN apt-get -q update
RUN apt-get -qy install git-core redis-server vim
RUN npm install -g yo generator-hubot coffee-script

RUN adduser --disabled-password kusubot; \
  echo "kusubot ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
ENV HOME /home/kusubot
USER kusubot
WORKDIR /home/kusubot

RUN git clone https://github.com/cataska/slack-hubot.git hubot
RUN cd hubot; npm install

CMD cd hubot; bin/hubot --adapter slack
