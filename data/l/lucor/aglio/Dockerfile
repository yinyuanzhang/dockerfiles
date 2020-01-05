FROM alpine:3.4

MAINTAINER Luca Corbo <lu.corbo@gmail.com>

ENV AGLIO_VERSION 2.3.0

RUN apk --no-cache add \
  nodejs \
  python \
  make \
  g++

RUN npm install -g aglio@${AGLIO_VERSION}

VOLUME /data

WORKDIR /data

EXPOSE 3000 35729

ENTRYPOINT ["aglio"]
