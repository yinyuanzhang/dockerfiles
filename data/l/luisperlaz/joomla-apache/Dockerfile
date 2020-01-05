FROM php:5.6-apache
MAINTAINER Luis Alberto Pérez <luisperlazaro@gmail.com>

ENV JOOMLA_VERSION 3.4.1
ENV JOOMLA_PACKAGE https://github.com/joomla/joomla-cms/releases/download/$JOOMLA_VERSION/Joomla_$JOOMLA_VERSION-Stable-Full_Package.zip
ENV HTTPD_USER=www-data
ENV DATA_DIR=/var/www/html

RUN rm /etc/apache2/mods-available/php5.load
RUN apt-get update && apt-get install -y \
	unzip \
	php5 \
	php5-mysql \
	php5-xsl

RUN mkdir -p $DATA_DIR
WORKDIR $DATA_DIR
ADD $JOOMLA_PACKAGE joomla_package.zip
RUN unzip joomla_package.zip && rm joomla_package.zip && rm index.html
RUN echo 'php_value output_buffering "0"' > .htaccess
RUN chown -R $HTTPD_USER $DATA_DIR

EXPOSE 80
