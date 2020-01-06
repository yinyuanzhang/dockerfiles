FROM rossriley/docker-nginx-pg-php
MAINTAINER Contenedor de nginx
RUN apt-get -y update
RUN apt-get -y install vim

ENV HOST_DB_PGSQL=paola
ENV PASS_DB_PGSQL=123
RUN mkdir /var/www/html
COPY index.php  /var/www/html/index.php
COPY 000-default.conf /etc/apache2/sites-available/000-default.conf

