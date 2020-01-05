# FROM istepanov/dokuwiki:2.0
# MAINTAINER Ilya Stepanov <dev@ilyastepanov.com>

FROM alpine:3.4
MAINTAINER Dong Li <docker@lidong.me>

ENV DOKUWIKI_VERSION 2016-06-26a
ENV MD5_CHECKSUM 9b9ad79421a1bdad9c133e859140f3f2

RUN apk --no-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/community/ add \
    php7 php7-fpm php7-gd php7-session php7-xml nginx supervisor curl tar unzip

RUN mkdir -p /run/nginx && \
    mkdir -p /var/www /var/www/wiki && \
    cd /var/www/wiki && \
    curl -O -L "https://download.dokuwiki.org/src/dokuwiki/dokuwiki-$DOKUWIKI_VERSION.tgz" && \
    tar -xzf "dokuwiki-$DOKUWIKI_VERSION.tgz" --strip 1 && \
    rm "dokuwiki-$DOKUWIKI_VERSION.tgz" 

# add plugin to support
# smtp
RUN curl -O -L "https://github.com/splitbrain/dokuwiki-plugin-smtp/archive/master.zip" && \
    unzip master.zip -d /var/www/wiki/lib/plugins/ && \
    mv /var/www/wiki/lib/plugins/dokuwiki-plugin-smtp-master /var/www/wiki/lib/plugins/smtp && \
    rm -rf master.zip

ADD nginx.conf /etc/nginx/nginx.conf
ADD supervisord.conf /etc/supervisord.conf
ADD start.sh /start.sh

RUN echo "cgi.fix_pathinfo = 0;" >> /etc/php7/php-fpm.ini && \
    sed -i -e "s|;daemonize\s*=\s*yes|daemonize = no|g" /etc/php7/php-fpm.conf && \
    sed -i -e "s|listen\s*=\s*127\.0\.0\.1:9000|listen = /var/run/php-fpm7.sock|g" /etc/php7/php-fpm.d/www.conf && \
    sed -i -e "s|;listen\.owner\s*=\s*|listen.owner = |g" /etc/php7/php-fpm.d/www.conf && \
    sed -i -e "s|;listen\.group\s*=\s*|listen.group = |g" /etc/php7/php-fpm.d/www.conf && \
    sed -i -e "s|;listen\.mode\s*=\s*|listen.mode = |g" /etc/php7/php-fpm.d/www.conf && \
    chmod +x /start.sh

EXPOSE 80
VOLUME ["/var/www/wiki"]

CMD /start.sh
