FROM nginx
MAINTAINER Arne Schauf <docker@asw.io>

RUN mkdir -p /etc/nginx/sites-enabled

VOLUME /etc/nginx/sites-enabled
VOLUME /var/log/nginx

COPY nginx.conf /etc/nginx/nginx.conf
COPY mime.types /etc/nginx/mime.types

EXPOSE 80 443 9999
