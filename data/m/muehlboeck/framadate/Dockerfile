FROM php:5.6-apache
MAINTAINER "Florian Humer <hf@muehlboeck.com>"

RUN apt-get update && \
	apt-get install -y \
                git && \
# PHP extensions
	apt-get install -y \
		libfreetype6-dev \
	        libjpeg62-turbo-dev \
	        libmcrypt-dev \
	        libpng12-dev \
	        zlib1g-dev libicu-dev g++ \
	        php5-mysqlnd && \

	docker-php-ext-install -j$(nproc) iconv mcrypt && \
	
	docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ && \
	docker-php-ext-install -j$(nproc) gd && \

	docker-php-ext-install mysqli mysql pdo pdo_mysql && \

	docker-php-ext-configure intl && \
	docker-php-ext-install intl && \
	
	cd /var && \
        rm -rf /var/www/html && \
	
	git clone https://github.com/framasoft/framadate.git /var/www/html && \
	
	cd /var/www/html && \
	curl https://getcomposer.org/installer | php -- --quiet && \
	php composer.phar install && \
	
	mkdir /var/www/html/tpl_c && \
	chown -R www-data:www-data /var/www/html
	

# Update the PHP.ini file, enable <? ?> tags and quieten logging.
# RUN sed -i "s/error_reporting = .*$/error_reporting = E_ERROR | E_WARNING | E_PARSE/" /etc/php5/apache2/php.ini

COPY scripts/run.sh /run.sh
RUN chmod +x /run.sh

EXPOSE 80

VOLUME /var/www/html/app/inc

CMD ["/run.sh"]
