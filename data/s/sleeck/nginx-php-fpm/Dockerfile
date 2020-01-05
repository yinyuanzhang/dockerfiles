FROM debian:latest

MAINTAINER Sleeck <contact@sleeck.eu>
LABEL description="nginx with php-fpm"

WORKDIR /tmp

RUN apt-get update \
	&& export DEBIAN_FRONTEND="noninteractive" \
	&& apt-get -y install nginx php-fpm supervisor inotify-tools apt-utils php-mysql
	
ADD conf/supervisord_nginx.conf /etc/supervisor/conf.d/nginx.conf
ADD conf/supervisord_php-fpm.conf /etc/supervisor/conf.d/php-fpm.conf
ADD conf/supervisord_nginx-auto-reload.conf /etc/supervisor/conf.d/nginx-auto-reload.conf

RUN mkdir -p /var/run/php \
	&& sed -i "s|BINARY_LOCATION|"$(find /usr/sbin/ -name php-fpm*)"|g" /etc/supervisor/conf.d/php-fpm.conf \
	&& sed -i "s|CONFIG_LOCATION|"$(find /etc/php -name www.conf)"|g" /etc/supervisor/conf.d/php-fpm.conf \
	&& sed -i '/#location/,/}/d' /etc/nginx/sites-enabled/default \
	&& sed -i 's/# pass PHP scripts to FastCGI server/# pass PHP scripts to FastCGI server\r\n        location ~ \\.php$ {\r\n                include snippets\/fastcgi-php.conf;\r\n                fastcgi_pass unix:'$(cat /etc/php/*/fpm/pool.d/www.conf  |egrep "^listen =" | awk '{print $3}' | sed 's/\//\\\//g')';\r\n        }/g' /etc/nginx/sites-enabled/default \
	&& sed -i 's/index.nginx-debian.html/index.php index.nginx-debian.html/g' /etc/nginx/sites-enabled/default \
	&& apt-get -y autoremove \
	&& apt-get clean autoclean \
	&& rm -rf /var/lib/{log,dpkg,apt,cache}

EXPOSE 80

CMD /usr/bin/supervisord -n -c /etc/supervisor/supervisord.conf
