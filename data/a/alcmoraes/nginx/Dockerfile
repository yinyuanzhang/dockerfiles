FROM debian:jessie

MAINTAINER Alexandre Moraes <http://github.com/alcmoraes>

RUN apt-get update && apt-get install -y nginx

ADD nginx.conf /etc/nginx/
COPY sites-available /etc/nginx/sites-available

VOLUME /var/www

COPY run.sh /run.sh
RUN chmod +x /run.sh

RUN usermod -u 1000 www-data

CMD ["/run.sh"]

EXPOSE 80 8080 443
