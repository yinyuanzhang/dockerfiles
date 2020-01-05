FROM node:6
MAINTAINER muratcan.karakurt@gmail.com

ADD . /opt/hubot
RUN cd /opt/hubot && npm install && chmod +x bin/hubot
WORKDIR /opt/hubot
ENTRYPOINT ["./bin/hubot"]