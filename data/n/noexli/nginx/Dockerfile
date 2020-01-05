#
# nginx Dockerfile
#

FROM ubuntu:14.04

RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections \
  && echo "#!/bin/sh\nexit 0" > /usr/sbin/policy-rc.d

RUN apt-get update \
  && apt-get install -y wget

RUN wget -q -O - http://nginx.org/keys/nginx_signing.key | sudo apt-key add - \
  && echo "deb http://nginx.org/packages/mainline/ubuntu/ trusty nginx" >> /etc/apt/sources.list \
  && apt-get update \
  && apt-get install -y nginx \
  && rm -rf /var/lib/apt/lists/* \
  chown -R www-data:www-data /var/lib/nginx

VOLUME ["/etc/nginx/sites-enabled", "/var/log/nginx", "/var/www/html"]

WORKDIR /etc/nginx

RUN ln -sf /dev/stdout /var/log/nginx/access.log \
  && ln -sf /dev/stderr /var/log/nginx/error.log

EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]
