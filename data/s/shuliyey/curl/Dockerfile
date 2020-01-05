FROM alpine

MAINTAINER Zeyu Ye <Shuliyey@gmail.com>

ARG DOCKERIZE_VERSION=v0.6.1

RUN apk add --update curl bash jq \
  && curl -L https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz -o dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
  && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
  && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
  && rm -rf /var/cache/apk/*

CMD ["bash"]
