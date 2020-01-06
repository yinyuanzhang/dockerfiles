FROM alpine:latest

MAINTAINER Michał Jaskólski <michal@jaskolski.online>

RUN apk add --update mosquitto && mkdir /data && chown nobody /data 

VOLUME ["/data"]
WORKDIR /data

USER nobody

EXPOSE 1883

ENTRYPOINT ["mosquitto"]
