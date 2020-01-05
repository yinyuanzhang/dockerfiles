FROM python:3-alpine

LABEL author='Ivan Lau' maintainer='ivan@ivanlau.xyz'

RUN echo "http://dl-8.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories

RUN \
    apk update && \
    apk add --no-cache ffmpeg libffi-dev libsodium-dev opus-dev && \
    adduser -D -h /home/container container

USER container
ENV USER=container HOME=/home/container
WORKDIR /home/container

COPY python3/entrypoint.sh /entrypoint.sh
CMD ['/bin/ash', '/entrypoint.sh']