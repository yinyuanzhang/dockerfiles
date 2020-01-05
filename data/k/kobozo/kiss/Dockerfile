FROM ulsmith/alpine-apache-php7

MAINTAINER Kobozo <yannick@kobozo.be>

LABEL be.kobozo.app="kiss"
LABEL be.kobozo.vendor="kobozo"

RUN apk add php7-openssl php7-yaml && \
    apk update && \
    apk upgrade 

ADD app/ /app/
ADD php.ini /etc/php7/php.ini

RUN chmod 757 -R /app/bootstrap/cache/ && \
    chmod 757 -R /app/storage/
