FROM alpine:latest

MAINTAINER Axel Wegener <awmath@sparse-space.de>

RUN apk update --no-cache && apk upgrade --no-cache && apk add --no-cache dnsmasq

EXPOSE 53
EXPOSE 67/udp

CMD ["dnsmasq", "-d"]
