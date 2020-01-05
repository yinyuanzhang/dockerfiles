FROM ubuntu:16.04
MAINTAINER "info@gamutgurus.com"
RUN apt-get update
RUN apt-get install -y nginx
RUN apt-get install -y vim
COPY index.html /var/www/html
ENTRYPOINT service nginx start && bash
