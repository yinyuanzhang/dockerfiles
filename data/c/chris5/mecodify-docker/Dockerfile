FROM php:5-apache
MAINTAINER Chris927 <chris@uber5.com>

RUN docker-php-ext-install pdo pdo_mysql mysqli

ARG RELEASE=1.31
RUN set -ex \
  && curl -L https://github.com/wsaqaf/mecodify/archive/${RELEASE}.tar.gz -o source.tar.gz \
  && tar xfz source.tar.gz \
  && rm source.tar.gz \
  && mv mecodify-${RELEASE}/* /var/www/html/ \
  && chown -R 33 /var/www/html/tmp
