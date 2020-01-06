FROM ubuntu:xenial

ENV OS_LOCALE="en_US.UTF-8"
RUN apt-get update && apt-get install -y locales && locale-gen ${OS_LOCALE}
ENV LANG=${OS_LOCALE} \
    LANGUAGE=en_US:en

ENV APACHE_CONF_DIR=/etc/apache2 \
    PHP_CONF_DIR=/etc/php/7.1 \
    PHP_DATA_DIR=/var/lib/php

	# Add php and apache2 to apt repo
RUN	buildDeps='software-properties-common python-software-properties' \
	&& apt-get install --no-install-recommends -y $buildDeps \
	&& add-apt-repository -y ppa:ondrej/php \
	&& add-apt-repository -y ppa:ondrej/apache2 \
	&& apt-get update
	
    	# Install dependencies
RUN	apt-get install -y curl
RUN	apt-get install -y apache2
RUN	apt-get install -y libapache2-mod-php7.1
RUN	apt-get install -y php7.1-common
RUN	apt-get install -y php7.1-cli
RUN	apt-get install -y php7.1-readline
RUN	apt-get install -y php7.1-mbstring
RUN	apt-get install -y php7.1-zip
RUN	apt-get install -y php7.1-intl
RUN	apt-get install -y php7.1-xml
RUN	apt-get install -y php7.1-json
RUN	apt-get install -y php7.1-curl
RUN	apt-get install -y php7.1-mcrypt
RUN	apt-get install -y php7.1-gd
RUN	apt-get install -y php7.1-pgsql
RUN	apt-get install -y php7.1-mysql
RUN	apt-get install -y php7.1-mongodb
RUN	apt-get install -y php7.1-sqlite
RUN	apt-get install -y php7.1-xdebug
RUN	apt-get install -y php7.1-bcmath
RUN	apt-get install -y php-pear
    	
	# Apache settings
RUN 	cp /dev/null ${APACHE_CONF_DIR}/conf-available/other-vhosts-access-log.conf \
	&& rm ${APACHE_CONF_DIR}/sites-enabled/000-default.conf ${APACHE_CONF_DIR}/sites-available/000-default.conf \
	&& a2enmod proxy_http rewrite headers php7.1
	
	# PHP settings
RUN	phpenmod mcrypt
	
	# Install composer
RUN	curl -sS https://getcomposer.org/installer | php -- --version=1.4.1 --install-dir=/usr/local/bin --filename=composer
	
	# Cleaning
RUN	apt-get purge -y --auto-remove $buildDeps locales \
	&& apt-get autoremove -y \
	&& rm -rf /var/lib/apt/lists/*
	
	# Forward request and error logs to docker log collector
RUN	ln -sf /dev/stdout /var/log/apache2/access.log \
	&& ln -sf /dev/stderr /var/log/apache2/error.log \
	&& chown www-data:www-data ${PHP_DATA_DIR} -Rf

RUN mkdir /var/www/app
WORKDIR /var/www/app
