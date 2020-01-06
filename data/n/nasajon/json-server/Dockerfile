FROM node:alpine
MAINTAINER Nasajon Sistemas<devops@nasajon.com.br>

RUN npm install -g json-server

RUN mkdir /data && \
    echo "{}" > db.json

EXPOSE 80

CMD json-server /data/db.json --watch --port 80
