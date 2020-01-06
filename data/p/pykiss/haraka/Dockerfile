FROM node:0.12.7

RUN npm install Haraka -g
 
VOLUME /src
WORKDIR /src
 
env NODE_ENV production
env NPM_SCRIPT start
env HOME /src
cmd /root/start.sh

EXPOSE 25

ADD start.sh /root/start.sh
RUN chmod +x /root/start.sh
