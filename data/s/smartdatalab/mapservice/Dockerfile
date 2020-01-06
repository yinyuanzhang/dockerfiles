FROM alpine:3.10
RUN apk update &&  apk add apache2  php7-cli php7-fpm  php7-dev   php7-pgsql php7-json php7-pdo php7-pdo_pgsql php7-apache2  openrc
RUN rm -f /var/www/localhost/htdocs/index.html
COPY files /var/www/localhost/htdocs
COPY apache2/httpd.conf /etc/apache2/httpd.conf
EXPOSE 80
CMD /usr/sbin/httpd -D FOREGROUND 
