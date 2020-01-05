FROM ubuntu:15.10
MAINTAINER R. Cody Erben "erben22@mtnaircomputer.net"
ENV REFRESHED_AT 2016-02-01
RUN apt-get -yqq update && apt-get -yqq install nginx RUN mkdir -p /var/www/html/website
ADD nginx/global.conf /etc/nginx/conf.d/
ADD nginx/nginx.conf /etc/nginx/nginx.conf
EXPOSE 80
