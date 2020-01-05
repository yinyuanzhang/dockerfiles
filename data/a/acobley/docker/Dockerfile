FROM ubuntu:14.04
MAINTAINER Andy Cobley "andy@r2-dvd.org"
ENV REFRESHED_AT 2015-30-04
RUN apt-get update
RUN apt-get install -y nginx
RUN apt-get install -y emacs
RUN mkdir -p /var/www/html
ADD http://www.flockedu.co.uk:8080/global.conf /etc/nginx/conf.d/
ADD http://www.flockedu.co.uk:8080/nginx.conf /etc/nginx/nginx.conf
EXPOSE 80
ENTRYPOINT ["/usr/sbin/nginx"]