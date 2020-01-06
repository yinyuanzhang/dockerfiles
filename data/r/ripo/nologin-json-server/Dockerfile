FROM node:latest
MAINTAINER Christian Lück <christian@lueck.tv>

RUN npm install -g json-server

WORKDIR /data
VOLUME /data

EXPOSE 8080
ADD run.sh /run.sh
ENTRYPOINT ["bash", "/run.sh"]
CMD []
