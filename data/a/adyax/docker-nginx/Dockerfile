# Docker Adyax
#
#

FROM debian:stable

MAINTAINER Benoît GRUNENBERGER <bgrunenberger@adyax.com>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-key adv --fetch-keys "http://nginx.org/keys/nginx_signing.key" && \
	apt-get update -y && \
	apt-get install -y nginx openssl ca-certificates && \
	apt-get -y -q autoclean && \
	apt-get -y -q autoremove

ADD nginx.conf /etc/nginx/nginx.conf
ADD nginx-site.conf /etc/nginx/sites-available/default

ADD ssl/server.crt /etc/nginx/server.crt
ADD ssl/server.key /etc/nginx/server.key

EXPOSE 80 443

ENTRYPOINT ["nginx"]

#CMD ["service nginx start &"]
