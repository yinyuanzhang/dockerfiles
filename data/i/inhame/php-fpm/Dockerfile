FROM php:7.0.32-fpm-alpine
RUN \
	apk add --no-cache libpng libjpeg freetype libxslt icu-libs && \ 
	apk add --nocache --virtual buildDeps freetype-dev libpng-dev libjpeg-turbo-dev zlib-dev libxpm-dev libmcrypt-dev libxslt-dev icu-dev libxml2-dev libzip-dev autoconf gcc g++ make && \
	docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ --with-png-dir=/usr/include/ && \
	docker-php-ext-install mcrypt && \
	docker-php-ext-install gd && \
	docker-php-ext-install xsl && \
	docker-php-ext-install bcmath && \
	docker-php-ext-install intl && \
	docker-php-ext-install soap && \
	docker-php-ext-install zip && \
	docker-php-ext-install opcache && \
	docker-php-ext-install mysqli && \
	docker-php-ext-install pdo_mysql && \
	docker-php-ext-enable mcrypt && \
	docker-php-ext-enable gd && \
	docker-php-ext-enable xsl && \
	docker-php-ext-enable bcmath && \
	docker-php-ext-enable intl && \
	docker-php-ext-enable soap && \
	docker-php-ext-enable zip && \
	docker-php-ext-enable opcache && \
	docker-php-ext-enable mysqli && \
	docker-php-ext-enable pdo_mysql && \
	apk del buildDeps
