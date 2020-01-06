# mumble-server
#
# Version latest

FROM alpine:latest
LABEL maintainer Thomas Ingvarsson <ingvarsson.thomas@gmail.com>

RUN apk add --no-cache \
      murmur \
      qt5-qtbase-mysql \
      qt5-qtbase-postgresql

VOLUME ["/config"]

ADD ["murmur.ini", "/config/murmur.ini"]

EXPOSE 64738
EXPOSE 64738/udp

CMD ["murmurd", "-fg", "-ini", "/config/murmur.ini"]
