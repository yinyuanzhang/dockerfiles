FROM node:latest
MAINTAINER Suhail Taj Shaik <suhailtajshaik@gmail.com>

RUN npm install -g json-server

WORKDIR /data
VOLUME /data

EXPOSE 9090

ADD run.sh /run.sh
ENTRYPOINT ["bash", "/run.sh"]
CMD []