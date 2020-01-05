FROM ubuntu:14.04

## Install tools
RUN apt-get update && \
    apt-get install software-properties-common supervisor -y 

## Install nginx
# add ppa repository
ENV NGINX_VERSION stable
RUN echo "deb http://ppa.launchpad.net/nginx/$NGINX_VERSION/ubuntu `lsb_release -sc` main" > /etc/apt/sources.list.d/nginx-$NGINX_VERSION.list && \
	apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C300EE8C && \
	apt-get update
# installation
RUN apt-get install nginx -y

## Configure nginx
ADD config/nginx.conf /etc/nginx/nginx.conf
ADD config/default /etc/nginx/sites-enabled/

## Supervisor configuration
ADD config/supervisor-nginx.conf /etc/supervisor/conf.d/nginx.conf

## Docker config
EXPOSE 80
CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisor/supervisord.conf"]