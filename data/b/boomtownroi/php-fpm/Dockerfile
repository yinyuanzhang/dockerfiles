FROM php:7.3-fpm-stretch

LABEL maintainer BoomTown CNS Team <consumerteam@boomtownroi.com>

ENV ALLOW_DEBUG true

# A list of packages required for acquiring and building modules and tools
# which will be required by the final container.
ENV COMPILE_TIME_DEPS \
	automake \
	byacc \
	cpp \
	git \
	libc-client-dev \
	libicu-dev \
	libkrb5-dev \
	libmagickwand-dev \
	libmcrypt-dev \
	libmemcached-dev \
	libpng-dev \
	libpspell-dev \
	librecode-dev \
	libtidy-dev \
	libxml2-dev \
	libxslt-dev

# apt-get update must be run to populate the list of packages before anything
# can be installed. Combining the update, install, and removal into a single
# layer the final size of the layer is minimized.
RUN apt-get update && \
	apt-get install -y --no-install-recommends \
	${COMPILE_TIME_DEPS} \
	netcat && \
	rm -rf /var/lib/apt/lists/*

# The PHP image provides its own special tools for configuring and installing
# PHP modules in a Docker container.
RUN docker-php-ext-configure imap --with-kerberos --with-imap-ssl

RUN docker-php-ext-install -j2 \
	gd \
	imap \
	intl \
	mysqli \
	pspell \
	recode \
	tidy \
	xmlrpc \
	xsl

# Some PHP modules are only available through PECL. While pecl can accept a
# list of packages, splitting the calls leads to more helpful error messages if
# anything actually fails to install.
RUN pecl install imagick-3.4.4 && \
	pecl install mcrypt-1.0.2 && \
	pecl install memcached-3.1.3 && \
	pecl install xdebug-2.7.2

# Install latest development version of Swig that has support for PHP7
RUN cd / && \
	git clone https://github.com/swig/swig.git && \
	cd swig && \
	sh ./autogen.sh && \
	./configure && \
	make && \
	make install

# Install & configure the 51Degrees extension
RUN cd / && \
	git clone https://github.com/51Degrees/Device-Detection.git && \
	cd Device-Detection/php/pattern && \
	phpize && \
	./configure PHP7=1 && \
	make install

# Overide PHP config options for xdebug and 51Degress
COPY config/* $PHP_INI_DIR/conf.d/

# Clean up all build dependencies and outside files.
RUN cd / && \
	rm -rf swig && \
	rm -rf Device-Detection && \
	apt-get remove -y ${COMPILE_TIME_DEPS} && \
	apt-get clean

# Copy local modifications to the container's root filesystem.
COPY root /

RUN docker-php-ext-enable \
	imagick \
	mcrypt \
	memcached \
	opcache \
	xdebug

RUN cp "$PHP_INI_DIR/php.ini-development" "$PHP_INI_DIR/php.ini"

# TODO: Reimplement when setting for QA/Prod
# RUN phpdismod xdebug

VOLUME /opt/51Degrees
