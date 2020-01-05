FROM alpine:3.10

RUN echo -e "@edge http://nl.alpinelinux.org/alpine/edge/main\n@testing http://nl.alpinelinux.org/alpine/edge/testing\n@community http://nl.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories

#BUMP apktools
RUN apk update; \
    apk upgrade; \
    rm -rf /var/cache/apk/*
