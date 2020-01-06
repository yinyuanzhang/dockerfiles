FROM nodered/node-red-docker

LABEL maintanier 'TREINAMENTO'

USER root

ENV NAME=''

COPY flows.json /data/

COPY package.json /usr/src/node-red/
COPY package.json /data/

COPY run.sh /

RUN npm install -g node-red-mongodb

RUN chmod +x /run.sh

EXPOSE 1880

CMD ["/run.sh"]