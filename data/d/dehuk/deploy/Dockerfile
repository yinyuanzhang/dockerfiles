FROM alpine:3.9

ENV PHP_PACKEGES php7 php7-json php7-curl php7-intl php7-ctype php7-mbstring php7-gd php7-mcrypt php7-cgi

ENV MAIN_PACKAGES curl rsync openssh

RUN apk update \
    && apk add $PHP_PACKEGES \
    && apk add $MAIN_PACKAGES \
    && rm -rf /var/cache/apk/*
