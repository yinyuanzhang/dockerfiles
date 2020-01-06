#A simple dockerfile for getting public IP Address
FROM alpine:edge
MAINTAINER Serdar.Sarioglu@mysystem.org

RUN apk update
RUN apk add bind-tools bash

CMD ["bash", "-c", "echo Your Public IP: $(dig +short myip.opendns.com @resolver1.opendns.com)"]
