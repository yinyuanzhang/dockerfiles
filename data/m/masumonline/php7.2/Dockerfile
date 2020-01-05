FROM ubuntu:18.04

RUN apt-get update 
RUN apt-get upgrade -y
RUN apt-get install nginx -y
ARG DEBIAN_FRONTEND=noninteractive
RUN apt install nano php-fpm php-zip php-gd  php-mbstring php-xml php-mysql supervisor curl nodejs npm composer -y
COPY ./conf/default /etc/nginx/sites-available/
COPY ./conf/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

USER root
RUN chown -R www-data:www-data /var/www/html/
RUN chmod -R 775 /var/www/html/
RUN chmod -R g+s /var/www/html/
RUN mkdir /run/php/

VOLUME /var/www/html
#WORKDIR /var/www/html
RUN usermod -u 1000 www-data
EXPOSE 80
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]