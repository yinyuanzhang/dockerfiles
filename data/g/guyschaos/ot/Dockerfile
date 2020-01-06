FROM ubuntu:18.04

ARG VERSION=v1.4-rc1
RUN mkdir /config
RUN  apt-get update \
  && apt-get install -y unzip wget \
  && rm -rf /var/lib/apt/lists/*
RUN mkdir /app && cd /app && \
    wget https://github.com/shawn1m/overture/releases/download/${VERSION}/overture-linux-amd64.zip && \
    unzip overture-linux-amd64.zip -d /app && rm overture-linux-amd64.zip && chmod +x overture-linux-amd64 && mv overture-linux-amd64 overture

WORKDIR /app
VOLUME ["/config"]

CMD ./overture ${OPTS}
