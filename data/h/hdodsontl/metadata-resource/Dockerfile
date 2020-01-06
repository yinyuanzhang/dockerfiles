FROM alpine:3.7

RUN apk update
RUN apk add util-linux

COPY check in out /opt/resource/
RUN chmod +x /opt/resource/*
