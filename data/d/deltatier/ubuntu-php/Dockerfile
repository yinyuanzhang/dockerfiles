FROM ubuntu:16.04

RUN export DEBIAN_FRONTEND=noninteractive && apt-get -y update && apt-get install -y git curl unzip openssh-client software-properties-common language-pack-en-base 
RUN LC_ALL=en_US.UTF-8 add-apt-repository -y ppa:ondrej/php 
RUN export DEBIAN_FRONTEND=noninteractive && apt-get -y update && apt-get install -y \
	php7.2-cli \
	php7.2-bcmath \
	php7.2-curl \
	php7.2-dev \
	php7.2-gd \
	php-geoip \
	php-imagick \
	php7.2-intl \
	php7.2-json \
	php7.2-mbstring \
	php7.2-mysql \	
	php-redis \
	php-smbclient \
	php-sodium \
	php-ssh2 \
	php7.2-soap \	
	php7.2-sqlite3 \
	php-uuid \
	php7.2-xml \
	php7.2-zip \
	php-pear \
	php-xdebug
	
CMD ["php", "-v"]

