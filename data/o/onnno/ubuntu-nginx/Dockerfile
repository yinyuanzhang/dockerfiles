FROM ubuntu:xenial

MAINTAINER Dong Li "docker@lidong.me”

ENV NGINX_VERSION 1.11.6-1~xenial

RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys 573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62 \
	&& echo "deb http://nginx.org/packages/mainline/ubuntu/ xenial nginx" >> /etc/apt/sources.list \
    && echo "deb-src http://nginx.org/packages/mainline/ubuntu/ xenial nginx" >> /etc/apt/sources.list \
	&& apt-get update \
	&& apt-get install --no-install-recommends --no-install-suggests -y \
						ca-certificates \
						nginx=${NGINX_VERSION} \
						nginx-module-xslt \
						nginx-module-geoip \
						nginx-module-image-filter \
						nginx-module-perl \
						nginx-module-njs \
						gettext-base \
                        letsencrypt \
	&& rm -rf /var/lib/apt/lists/*

COPY nginx.conf /etc/nginx/nginx.conf

# VOLUME
VOLUME /usr/share/nginx/html
VOLUME /var/log/nginx
VOLUME /etc/nginx/conf.d
VOLUME /etc/letsencrypt

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
	&& ln -sf /dev/stderr /var/log/nginx/error.log

EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]
