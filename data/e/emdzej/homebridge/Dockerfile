FROM node:alpine

MAINTAINER Michał Jaskólski <michal@jaskolski.online>

RUN apk update && apk add --no-cache build-base avahi-dev avahi dbus

RUN npm install -g homebridge --unsafe-perm

RUN apk del --purge build-base

COPY avahi-daemon.conf /etc/avahi/avahi-daemon.conf

USER root

RUN mkdir -p /var/run/dbus /homebridge

#COPY config.json /homebridge/config.json

COPY homebridge.sh /homebridge/homebridge.sh 
RUN chmod +x /homebridge/homebridge.sh

VOLUME ["/homebridge"]

EXPOSE 5353 51826
#should be run with --net host

ENTRYPOINT ["/homebridge/homebridge.sh"]
