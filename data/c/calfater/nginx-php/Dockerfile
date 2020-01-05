FROM calfater/base-image:ubuntu-18.04

ARG PHP_VERSION=7.2

RUN apt-get update
RUN apt-get install -y nginx
RUN export DEBIAN_FRONTEND=noninteractive; \
    apt-get install -y php${PHP_VERSION}-fpm; \
    ln -fs /usr/share/zoneinfo/Europe/Paris /etc/localtime; \
    dpkg-reconfigure --frontend noninteractive tzdata
RUN apt-get install -y php${PHP_VERSION}-mysql
RUN apt-get install -y php${PHP_VERSION}-gd
RUN apt-get install -y php${PHP_VERSION}-mbstring
RUN apt-get install -y php${PHP_VERSION}-xml
RUN apt-get install -y composer

RUN apt-get install -y sendmail
#RUN yes | sendmailconfig

ENV PHP_VERSION=${PHP_VERSION}
ENV WORKDIR=/home/nginx-php
ENV PUID=1000
ENV PGID=1000

WORKDIR $WORKDIR
ENTRYPOINT ["/home/nginx-php/entrypoint.sh"]
VOLUME ["/config", "/www"]
EXPOSE 80

COPY ["origin", "origin"]
COPY ["entrypoint.sh", "entrypoint.sh"]

RUN cp /etc/php/${PHP_VERSION}/fpm/php.ini origin/

RUN ["chmod", "+x", "entrypoint.sh"]

