FROM php:5.6-apache

LABEL maintainer NetTeam Solutions <kontakt@netteam.pl>

COPY config/higg.conf /etc/apache2/sites-available/higg.conf
COPY config/php.ini /usr/local/etc/php/php.ini

RUN docker-php-source extract \
	&& apt-get update \
	&& apt-get install -y \
		libmcrypt-dev \
		libldap2-dev \
		libfreetype6-dev \
		libjpeg62-turbo-dev \
		libmcrypt-dev \
		libpng12-dev \
		libxml2-dev \
		libxslt-dev \
		libssl-dev \
		libpq-dev \
		libicu-dev \
		libzip-dev

RUN apt-get install -y \
		postgresql-client \
		git

RUN rm -rf /var/lib/apt/lists/*

RUN curl -L -o /tmp/mongo.tar.gz https://github.com/mongodb/mongo-php-driver-legacy/archive/1.6.0.tar.gz \
    && tar xfz /tmp/mongo.tar.gz -C /tmp/ \
    && mkdir -p /usr/src/php/ext/mongo \
    && mv /tmp/mongo-php-driver-legacy-1.6.0/* /usr/src/php/ext/mongo \
    && rm -r /tmp/mongo.tar.gz /tmp/mongo-php-driver-legacy-1.6.0 \
    && cd /usr/src/php/ext/mongo && phpize && ./configure && make all

RUN docker-php-ext-configure pgsql -with-pgsql=/usr/local/pgsql \
	&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
	&& docker-php-ext-install -j$(nproc) bcmath mbstring mcrypt mongo gd pgsql pdo_pgsql xsl intl zip \
	&& docker-php-source delete

RUN pear channel-discover pear.phing.info \
    && pear install [--alldeps] phing/phing

RUN set -xe; \
	a2ensite higg \
	&& a2enmod -q rewrite \
	&& a2enmod -q expires \
	&& a2enmod -q deflate \
	&& a2enmod -q vhost_alias

RUN useradd deploy
