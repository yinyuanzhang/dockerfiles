FROM ubuntu:18.04
LABEL maintainer="Fiko Borizqy <fiko@dr.com>"

# This file will be executed
ENV DCMD "/usr/sbin/docker-fiko-nginx-php.sh"

# Installing nginx
RUN apt-get update && apt-get install -y nginx

# Installing PHP
RUN apt-get update && apt-get install -y php7.2 \
	php7.2-fpm \
	php7.2-mysql \
	php7.2-cli \
	php7.2-common \
	php7.2-json \
	php7.2-curl \
	php7.2-gd \
	php7.2-intl \
	php7.2-mbstring \
	php7.2-xsl \
	php7.2-zip \
	php-gettext \
	php-imagick

# move to root directory
RUN cd /; \
	# creating $DCMD file
	touch $DCMD; \
	mkdir /run/php; \
	chmod +x $DCMD; \
	echo '#!/bin/bash' >> $DCMD; \
	echo 'cd /' >> $DCMD; \
	echo './etc/init.d/nginx start' >> $DCMD; \
	echo './etc/init.d/php7.2-fpm start' >> $DCMD; \
	echo 'echo $TIMEZONE > /etc/timezone' >> $DCMD; \
	# realtime logs
	echo 'tail -f /var/log/nginx/access.log -n 0 \' >> $DCMD; \
	echo '& tail -f /var/log/nginx/error.log -n 0' >> $DCMD;

# run PHP for the first time
RUN service php7.2-fpm start;

# Copying default Nginx configuration
COPY ./nginx.default.conf /etc/nginx/conf.d/default.conf
# Copying default PHP Pages
COPY ./public_html/ /var/www/html/

# Move to a directory
WORKDIR /var/www/html

EXPOSE 80 443

CMD ["/usr/sbin/docker-fiko-nginx-php.sh"]