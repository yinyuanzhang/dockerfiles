FROM doridian/alpine-minit
MAINTAINER Doridian

RUN echo "@testing http://dl-cdn.alpinelinux.org/alpine/edge/testing/" >> /etc/apk/repositories
RUN echo "@edge http://dl-cdn.alpinelinux.org/alpine/edge/main/" >> /etc/apk/repositories
RUN apk add --no-cache boost-python@edge boost@edge deluge@testing

COPY minit_services /etc/minit/services
EXPOSE 8112 61881-61891 61881-61891/udp
VOLUME "/config" "/downloads"
