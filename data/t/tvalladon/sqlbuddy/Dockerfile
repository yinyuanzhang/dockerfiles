FROM php:5.6-apache
MAINTAINER Terry Valladon <docker-sqlbuddy@terryvalladon.com>

RUN apt-get update &&\
 apt-get install -yq git && \
 rm -rf /var/lib/apt/lists/* && \
 rm -rf /var/www/html/* && \
 git clone https://github.com/calvinlough/sqlbuddy.git /var/www/html && \
 mv /var/www/html/src/* /var/www/html && \
 rm -rf /var/www/html/src

EXPOSE 80
