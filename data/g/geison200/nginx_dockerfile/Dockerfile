FROM nginx:stable


MAINTAINER Gêisson Machado Antunes <geisonnm@hotmail.com>


RUN rm -f /etc/nginx/conf.d/*

# config file for nginx 
#COPY config/nginx.conf /etc/nginx/nginx.conf

COPY config/virtual-host.conf /etc/nginx/conf.d


EXPOSE 80
