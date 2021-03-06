FROM debian:buster-slim
MAINTAINER Alexander Yancharuk <alex at itvault dot info>

# Keys for PHP installation
ADD https://packages.sury.org/php/apt.gpg /etc/apt/trusted.gpg.d/php.gpg

RUN chmod 644 /etc/apt/trusted.gpg.d/php.gpg \
	# Install packages needed for PHP
	&& apt-get update \
	&& DEBIAN_FRONTEND=noninteractive apt-get install -yqq --no-install-recommends \
		apt-transport-https \
		ca-certificates \
		gnupg \
		locales \
		netcat-traditional \
	&& echo "deb https://packages.sury.org/php/ buster main" > /etc/apt/sources.list.d/php.list \
	&& apt-get update \
	&& DEBIAN_FRONTEND=noninteractive apt-get install -yqq --no-install-recommends \
		php7.3-fpm \
		php7.3-bcmath \
		php7.3-curl \
		php7.3-gd \
		php7.3-intl \
		php7.3-json \
		php7.3-mbstring \
		php7.3-mysql \
		php7.3-sqlite3 \
		php7.3-opcache \
		php7.3-readline \
		php7.3-soap \
		php7.3-xml \
		php7.3-zip \
	&& DEBIAN_FRONTEND=noninteractive apt-get install -yqq --no-install-recommends \
		php-memcached \
		php-redis \
		php-amqp \
		php-xdebug \
	# Cleanup
	&& DEBIAN_FRONTEND=noninteractive apt-get purge -yqq --autoremove \
		gnupg \
		apt-transport-https \
	&& rm /etc/apt/sources.list.d/php.list \
	&& apt-get update \
	&& apt-get clean \
	&& rm -rf /var/tmp/* /tmp/* \
		/var/lib/apt/lists/* \
		/var/log/apt/* \
		/var/cache/debconf \
		/var/cache/apt/archives/* \
		/etc/php/7.3/fpm/conf.d/20-xdebug.ini \
		/etc/apt/trusted.gpg.d/php.gpg \
	# Install locale
	&& sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen \
	&& DEBIAN_FRONTEND=noninteractive dpkg-reconfigure locales \
	&& update-locale LANG=en_US.UTF-8 \
	&& mkdir -p /run/php \
	&& chmod 777 /run/php

ENV LANG en_US.UTF-8

# Copy configs
COPY ./php-fpm.conf /etc/php/7.3/fpm/
COPY ./pool.d /etc/php/7.3/fpm/pool.d/

# Launch fpm
CMD ["php-fpm7.3"]

EXPOSE 9000

WORKDIR /var/www/html/
