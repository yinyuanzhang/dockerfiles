FROM forumi0721/alpine-armhf-base:latest

MAINTAINER pfeerick <peter.feerick@gmail.com>

COPY local/. /usr/local/

RUN ["docker-build-start"]

RUN ["docker-init"]

RUN ["docker-build-end"]

ENTRYPOINT ["docker-run"]

EXPOSE 8200/tcp

