FROM debian:jessie
MAINTAINER Christoph Meier <meier.c@sfeir.lu>

# Install nginx
RUN apt-get update \
	&& apt-get install -y nginx=1.6.1-1

# Add default configuration
ADD nginx.conf /etc/nginx/nginx.conf
