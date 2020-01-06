FROM node:8.11.4-stretch

ENV TINI_VERSION=0.18.0 \ 
    NODE_RED_VERSION=0.19.1 \
    FLOWS=flows.json \
    NODE_PATH=/node-red/node_modules:/data/node_modules

ADD https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini /tini
COPY start.sh /start.sh
RUN chmod +x /tini && chmod +x /start.sh

RUN mkdir /node-red && mkdir /data
WORKDIR /node-red
RUN npm install node-red@${NODE_RED_VERSION}

VOLUME [ "/data" ]
EXPOSE 1880
WORKDIR /data

ENTRYPOINT [ "/tini", "--", "/start.sh" ]