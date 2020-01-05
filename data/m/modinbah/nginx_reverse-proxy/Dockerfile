FROM alpine:latest
LABEL maintainer="Bayu Adin H <bayu.adin.h@mail.ugm.ac.id>"
LABEL description="Docker with NGINX"

ENV PORT_NGINX 80
ENV UPSTREAM LB_Wordpress
ENV SERVER_PERTAMA=192.168.151.4 \
    SERVER_KEDUA=192.168.151.5

RUN apk add --update nginx && \
    apk add unzip && \
    apk add curl && \
    rm -rf /var/cache/apk/* && \
    mkdir -p /tmp/nginx/ && \
    mkdir -p /usr/share/nginx/html

COPY config/nginx/nginx.conf /etc/nginx/nginx.conf
COPY config/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf
COPY script/starter.sh /starter.sh

EXPOSE ${PORT_NGINX}/tcp

ENTRYPOINT  ["sh", "starter.sh"]