FROM php:7.2.1-fpm

ADD https://raw.githubusercontent.com/mlocati/docker-php-extension-installer/master/install-php-extensions /usr/local/bin/

RUN chmod uga+x /usr/local/bin/install-php-extensions && sync && \
    install-php-extensions gd imap pdo_mysql bcmath sockets

RUN docker-php-ext-install mbstring
RUN docker-php-ext-install tokenizer
#breaks cache
RUN apt-get update \
	&& apt-get install -y \
		openssl \
        libxml2-dev \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libpng-dev \
        && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
        && docker-php-ext-install -j$(nproc) gd
RUN docker-php-ext-install xml
