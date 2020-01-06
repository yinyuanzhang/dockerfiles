FROM alpine:latest

LABEL maintainer="http://alejandro.lorente.info"

COPY NamecheapDdnsUpdate.sh /usr/bin
COPY configure.sh /usr/bin

ENV DOMAIN "mydomain.tld"
ENV PASSWORD ""
ENV HOSTS "'myhost1' 'myhost2'"
ENV EMAIL ""
ENV SECONDS 600

RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing/" >> /etc/apk/repositories && \
    apk add --update bash curl libxml2-utils && \
    rm -rf /tmp/* /var/tmp/* /var/cache/apk/* /var/cache/distfiles/*

WORKDIR /mnt

CMD configure.sh && \
    while true; do \
        NamecheapDdnsUpdate.sh | tee -a /mnt/ddns.log; \
        sleep $SECONDS; \
    done
