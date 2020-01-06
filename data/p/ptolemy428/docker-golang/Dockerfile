 
FROM golang:1.7

MAINTAINER Larry Liang <ptolemy428@gmail.com>

RUN apt-get update \
    && apt-get install -y less \
    && apt-get install -y vim \
    && apt-get install -y curl \
    && apt-get install -y jq
    
WORKDIR /go
