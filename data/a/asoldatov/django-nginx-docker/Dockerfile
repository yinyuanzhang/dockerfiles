FROM python:3.5-slim

MAINTAINER Alexandr Soldatov <alexsandr.soldatow@gmail.com>

# Install nginx and supervisor
ENV NGINX_VERSION 1.10.1-1~jessie

RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys 573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62 \
	&& echo "deb http://nginx.org/packages/debian/ jessie nginx" >> /etc/apt/sources.list \
	&& apt-get update \
	&& apt-get install -y supervisor \
	&& apt-get install --no-install-recommends --no-install-suggests -y \
						ca-certificates \
						nginx=${NGINX_VERSION} \
						nginx-module-xslt \
						nginx-module-geoip \
						nginx-module-image-filter \
						nginx-module-perl \
						nginx-module-njs \
						gettext-base \
	&& rm -rf /var/lib/apt/lists/*

# configure nginx
RUN rm /etc/nginx/nginx.conf /etc/nginx/mime.types && mkdir /var/www/
COPY nginx /etc/nginx
# link nginx logs to docker logs collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log && ln -sf /dev/stderr /var/log/nginx/error.log
# install django
RUN pip install --upgrade pip && pip install django==1.9
# expose static port
EXPOSE 80