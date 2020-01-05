FROM nginx:alpine

RUN echo "@testing http://dl-5.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories && \
    apk add --update && \
    apk add --upgrade apk-tools && \
    apk add --update && \
    apk upgrade && \
    apk add php7-fpm php7-curl php7-dom php7-openssl php7-xml php7-json && \
    rm -rf /var/cache/apk/* && \
    mkdir /app

VOLUME /app

COPY ./default.conf /etc/nginx/conf.d/
COPY ./code /app

CMD nginx && /usr/sbin/php-fpm7 -F
