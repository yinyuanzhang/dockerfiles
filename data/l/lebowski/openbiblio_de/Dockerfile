
FROM ubuntu:18.04

MAINTAINER Martin Schulte

RUN apt-get update
RUN apt-get install -y wget nano gettext-base nginx 
RUN apt-get install -y php-cli php-common php-mysql php-curl php-fpm iputils-ping


# php-fpm conf
RUN echo "cgi.fix_pathinfo = 0;" >> /etc/php/7.2/fpm/php.ini
RUN sed -i -e "s/;clear_env\s*=\s*no/clear_env = no/g" /etc/php/7.2/fpm/pool.d/www.conf
RUN sed -i 's/variables_order = "GPCS"/variables_order = "EGPCS"/g' /etc/php/7.2/fpm/php.ini 

RUN mkdir -p /var/www/html/


#nginx conf
COPY nginx.conf  /etc/nginx/sites-available/default
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY src  /var/www/html/


# Database setting on startup
COPY ./database_constants.php.tmpl /
COPY ./docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]



CMD service php7.2-fpm start && nginx

EXPOSE 80





