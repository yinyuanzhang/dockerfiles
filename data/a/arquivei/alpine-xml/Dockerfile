FROM golang:alpine
MAINTAINER Arquivei

RUN apk update && \
    apk upgrade && \
    apk add --no-cache make gcc musl-dev libxml2-dev xmlsec-dev openssl-dev tzdata git mercurial openssh

ENV PATH=$PATH:/go/bin
ENV TZ=America/Sao_Paulo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

EXPOSE 80

ENTRYPOINT make
