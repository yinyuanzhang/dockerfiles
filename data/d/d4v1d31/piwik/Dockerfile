FROM		alpine
MAINTAINER	David Elvers "david@d4v1d.eu"

RUN		apk update && apk upgrade
RUN		apk add bash nginx php-fpm unzip php-mysql php-gd php-json php-ctype php-dom php-iconv php-zlib php-pdo php-pdo_mysql php-pdo_sqlite
RUN		rm -rf /var/cache/apk/*

# add nginx config
ADD	nginx.conf /etc/nginx/
ADD	php-fpm.conf /etc/php/
ADD	php.ini	/etc/php/

# add entrypoint script
ADD start.sh /usr/bin/
RUN chmod +x /usr/bin/start.sh

# add piwik
ADD 	http://builds.piwik.org/piwik.zip /usr/share/nginx/html/
WORKDIR	/usr/share/nginx/html/
RUN	unzip piwik.zip
RUN	rm piwik.zip
WORKDIR /usr/share/nginx/html/piwik/

RUN 	chown -R root:nginx ./
RUN 	chown -R nginx:nginx ./tmp
RUN 	chown -R nginx:nginx ./config

EXPOSE		80

ENTRYPOINT	["start.sh"]
