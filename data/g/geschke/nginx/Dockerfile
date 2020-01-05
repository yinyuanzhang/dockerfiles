FROM alpine:3.4

LABEL last_changed="2016-11-30"

MAINTAINER Ralf Geschke <ralf@kuerbis.org>

RUN apk update \
  && apk add nginx \
  && chown -R nginx /var/lib/nginx \
  && mkdir -p /run/nginx \
  && chown -R nginx /run/nginx


COPY files/nginx.conf /etc/nginx/
VOLUME /etc/nginx/sites-enabled
VOLUME /etc/nginx/conf.d
VOLUME /var/www


EXPOSE 80 443


#USER nginx
#WORKDIR /home/deploy

CMD ["nginx"]
