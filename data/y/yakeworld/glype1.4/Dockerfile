FROM php:7.2.2-apache-stretch

MAINTAINER admin@yakeworld.top 

RUN apt update \
  && apt -y --no-install-recommends install wget unzip git \        
  && git clone https://github.com/k1995/glype /var/www/html \
  && chown -R www-data:www-data /var/www/html 
