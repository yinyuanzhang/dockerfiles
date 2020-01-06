FROM alpine
MAINTAINER Amandeep Singh "amtux@icloud.com"

RUN echo "http://dl-3.alpinelinux.org/alpine/edge/main" >> /etc/apk/repositories &&\
    echo "http://dl-3.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories &&\
    apk upgrade --update-cache --available &&\
    apk add micro curl &&\
    rm -rf /var/cache/apk/*