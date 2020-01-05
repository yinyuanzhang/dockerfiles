FROM node:latest

MAINTAINER mtakagi

RUN npm install -g yo generator-hubot
RUN adduser --disabled-password --gecos "" yeoman; \
  echo "yeoman ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
ENV HOME /home/yeoman
USER yeoman
WORKDIR /home/yeoman
CMD ["yo", "hubot", "--default"]