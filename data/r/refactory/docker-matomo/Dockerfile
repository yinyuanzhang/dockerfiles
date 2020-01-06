FROM php:7.2-fpm-alpine3.7

MAINTAINER Sebastiaan van Parijs <info@rfy.nl>

ENV MATOMO_URL="https://matomo.rfy.cloud/"
ENV CRONTAB_EMAIL="maintenance@rfy.io"

ARG MATOMO_VERSION=3.7.0
ARG PHP_REDIS_VERSION="3.1.6"
ARG PHP_YAML_VERSION="2.0.2"
ARG PHP_APCU_VERSION="5.1.12"
ARG PHP_GEOIP_VERSION="1.1.1"
ARG S6_VERSION="1.21.2.2"

# Basic build-time metadata as defined at http://label-schema.org
LABEL org.label-schema.docker.dockerfile="/Dockerfile" \
	org.label-schema.license="MIT" \
	org.label-schema.name="Matomo Alpine Docker Image" \
	org.label-schema.url="https://github.com/rfyio/docker-matomo" \
	org.label-schema.vcs-url="https://github.com/rfyio/docker-matomo" \
	org.label-schema.vcs-type="Git"

RUN set -x \
	&& apk update \
	&& apk add tar rsync curl sed bash python py-pip py-setuptools groff geoip-dev mysql-client nginx optipng freetype libjpeg-turbo-utils icu-dev pwgen sudo s6 \
	&& apk del py-pip py-setuptools \
	&& apk add --virtual .phpize-deps $PHPIZE_DEPS libtool freetype-dev libpng-dev libjpeg-turbo-dev yaml-dev \
	&& docker-php-ext-configure gd \
		--with-gd \
		--with-freetype-dir=/usr/include/ \
		--with-png-dir=/usr/include/ \
		--with-jpeg-dir=/usr/include/ \
	&& docker-php-ext-install \
		gd \
		pdo \
		pdo_mysql \
		mbstring \
		mysqli \
		opcache \
		zip \
	&& pecl install redis-${PHP_REDIS_VERSION} yaml-${PHP_YAML_VERSION} APCu-${PHP_APCU_VERSION} geoip-${PHP_GEOIP_VERSION} \
	&& docker-php-ext-enable redis \
		apcu \
		geoip \
	&& apk del .phpize-deps \
	&& rm -rf /var/cache/apk/*

# Copy configuration
COPY root /
RUN sed -i "s/MATOMO_URL/\$MATOMO_URL/g" /etc/crontabs/matomo-archive \
	&& sed -i "s/CRONTAB_EMAIL/\$CRONTAB_EMAIL/g" /etc/crontabs/matomo-archive

RUN set -ex; \
	apk add --no-cache --virtual .fetch-deps \
		gnupg \
	; \
	\
	curl -fsSL -o piwik.tar.gz \
		"https://builds.matomo.org/piwik-${MATOMO_VERSION}.tar.gz"; \
	curl -fsSL -o piwik.tar.gz.asc \
		"https://builds.matomo.org/piwik-${MATOMO_VERSION}.tar.gz.asc"; \
	export GNUPGHOME="$(mktemp -d)"; \
#	gpg --keyserver ha.pool.sks-keyservers.net --recv-keys 814E346FA01A20DBB04B6807B5DBD5925590A237; \
#	gpg --batch --verify piwik.tar.gz.asc piwik.tar.gz; \
#	gpgconf --kill all; \
#	rm -rf "$GNUPGHOME" piwik.tar.gz.asc; \
	tar -xzf piwik.tar.gz -C /data/; \
	rm piwik.tar.gz; \
	apk del .fetch-deps

RUN set -ex; \
	curl -fsSL -o /data/piwik/misc/GeoIPCity.dat.gz http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz; \
	gunzip /data/piwik/misc/GeoIPCity.dat.gz

# Download s6
ADD https://github.com/just-containers/s6-overlay/releases/download/v${S6_VERSION}/s6-overlay-amd64.tar.gz /tmp/

RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C / && rm /tmp/s6-overlay-amd64.tar.gz \
	&& deluser www-data \
	&& delgroup cdrw \
	&& addgroup -g 80 www-data \
	&& adduser -u 80 -G www-data -s /bin/bash -D www-data -h /data \
	&& rm -Rf /home/www-data \
	&& sed -i -e "s#listen = 9000#listen = /var/run/php-fpm.sock#" /usr/local/etc/php-fpm.d/zz-docker.conf \
	&& echo "clear_env = no" >> /usr/local/etc/php-fpm.d/zz-docker.conf \
	&& echo "listen.owner = www-data" >> /usr/local/etc/php-fpm.d/zz-docker.conf \
	&& echo "listen.group = www-data" >> /usr/local/etc/php-fpm.d/zz-docker.conf \
	&& echo "listen.mode = 0660" >> /usr/local/etc/php-fpm.d/zz-docker.conf \
	&& chown 80:80 -R /var/lib/nginx \
	&& echo 'www-data ALL=(ALL) NOPASSWD: ALL' > /etc/sudoers.d/www \
	&& /bin/bash -c "source /init-php-conf.sh" \

# Expose ports
EXPOSE 80

# Define working directory
WORKDIR /data

ENTRYPOINT ["/init"]