FROM php:7.3-fpm

ADD php.ini /usr/local/etc/php/conf.d/zz-php.ini

RUN apt-get update --fix-missing && \
	apt-get install -y \
	curl \
	dnsutils \
	gifsicle \
	git \
	gnupg \
	iputils-ping \
	jpegoptim \
	libfreetype6-dev \
	libjpeg62-turbo-dev \
	libmagickwand-dev \
	libmcrypt-dev \
	libpng-dev \
	libzip-dev \
	libc-client-dev \
	libkrb5-dev \
	libpq-dev \
	locales \
	mariadb-client \
	postgresql-client \
	net-tools \
	optipng \
	pngquant \
	rsync \
	telnet \
	vim \
	zip

RUN pecl install imagick
RUN pecl install redis
RUN docker-php-ext-enable imagick
RUN docker-php-ext-install -j$(nproc) zip
RUN docker-php-ext-install -j$(nproc) iconv
RUN docker-php-ext-install -j$(nproc) pdo_mysql
RUN docker-php-ext-install -j$(nproc) pdo_pgsql
RUN docker-php-ext-install -j$(nproc) gd
RUN docker-php-ext-install -j$(nproc) pcntl
RUN PHP_OPENSSL=yes docker-php-ext-configure imap --with-kerberos --with-imap-ssl
RUN docker-php-ext-install imap
RUN docker-php-ext-configure opcache --enable-opcache
RUN docker-php-ext-install opcache
RUN docker-php-ext-install intl
RUN docker-php-ext-install bcmath
RUN docker-php-ext-enable redis

RUN pecl install mailparse
RUN docker-php-ext-enable mailparse

RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
RUN echo "de_DE.UTF-8 UTF-8" >> /etc/locale.gen
RUN locale-gen

## install node js
#RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
#RUN apt-get update && \
#	apt-get install -y \
#	nodejs
#
#RUN npm install -g svgo

RUN curl -sS https://getcomposer.org/installer | \
    php -- --install-dir=/usr/bin/ --filename=composer

RUN composer global require hirak/prestissimo

# prepare everything for www-data user
RUN usermod --shell /bin/bash www-data
RUN mkdir -p /var/www/html
RUN chown -R www-data.www-data /var/www
RUN chmod -R 755 /var/www

USER www-data

RUN echo 'alias a="php artisan"' >> ~/.bashrc
RUN echo 'alias mf="php artisan migrate:fresh"' >> ~/.bashrc
RUN echo 'alias mfs="php artisan migrate:fresh --seed"' >> ~/.bashrc
RUN echo 'alias seed="php artisan migrate:fresh --seed"' >> ~/.bashrc
RUN echo 'alias rl="php artisan route:list"' >> ~/.bashrc
RUN echo 'alias t="php artisan decaf:test"' >> ~/.bashrc
RUN echo 'alias h="php artisan decaf:test --headless"' >> ~/.bashrc
RUN echo 'alias gp="git pull"' >> ~/.bashrc
RUN echo 'alias ci="composer install"' >> ~/.bashrc
RUN echo 'alias cu="composer update"' >> ~/.bashrc
RUN echo 'alias cda="composer dump-autoload"' >> ~/.bashrc
RUN echo 'alias fresh="CURRENT=$(pwd) && cd /git && git pull && cd /var/www/html && composer install && php artisan migrate:fresh --seed && cd $CURRENT"' >> ~/.bashrc
RUN echo 'alias sa="eval \"$(ssh-agent -s)\" && ssh-add"' >> ~/.bashrc
RUN echo 'alias pu="vendor/bin/phpunit"' >> ~/.bashrc

ENV PATH="~/.composer/vendor/bin:${PATH}"
ENV HISTCONTROL="ignoredups"
