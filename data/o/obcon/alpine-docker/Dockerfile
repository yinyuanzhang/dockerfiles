FROM obcon/alpine-base

ADD rootfs /

RUN apk update && \
  apk upgrade && \
  apk add \
    docker@community && \
  rm -rf /var/cache/apk/* && \
  mkdir -p /etc/logrotate.docker.d

EXPOSE 2376

ENV DOCKER_HOST tcp://127.0.0.1:2376
