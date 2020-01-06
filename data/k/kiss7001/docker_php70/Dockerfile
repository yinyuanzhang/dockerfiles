FROM ubuntu:16.04
MAINTAINER Wooyoung Kim <kiss7001@nate.com>

RUN apt-get update
RUN apt-get install -y nginx php7.0 php7.0-fpm php7.0-cli php7.0-common php7.0-mbstring php7.0-gd php7.0-intl php7.0-xml php7.0-mysql php7.0-mcrypt php7.0-zip php7.0-curl php7.0-soap

RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf
RUN chown -R www-data:www-data /var/lib/nginx

ADD nginx/sites-available/default /etc/nginx/sites-available/default

VOLUME ["/var/www/html", "/data", "/etc/nginx/sites-enabled", "/var/log/nginx"]

WORKDIR /etc/nginx

CMD service php7.0-fpm start && service nginx start && /usr/sbin/php-fpm7.0 -F -O 2>&1 | sed -u 's,.*: \"\(.*\)$,\1,'| sed -u 's,"$,,' 1>&1

EXPOSE 80
