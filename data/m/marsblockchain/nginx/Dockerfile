FROM nginx:1.16.0-alpine

LABEL maintainer Justin Liu <justintwd@gmail.com>

ADD ./data/conf/extra /etc/nginx/conf.d/extra

ADD ./data/conf/global.conf /etc/nginx/conf.d/global.conf

ADD ./data/conf/global.conf /etc/nginx/conf.d/global.conf

ADD ./data/static /var/www/static

RUN rm -rf /etc/nginx/conf.d/default.conf
