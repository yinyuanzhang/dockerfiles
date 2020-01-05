# Define versions used to select image versions
# (ARGs declared before FROM can't be used outside of FROMs)
ARG FROM_V8=6.6
ARG FROM_PHP=7.2
# We leave Alpine blank as it's not required, but can be used
ARG FROM_ALPINE=

# Compress libv8 and save for later
FROM alexmasterov/alpine-libv8:$FROM_V8 as v8build
RUN tar cvzf /tmp/libv8.tar.gz -C ${V8_DIR} .

# Build PHP Image
FROM php:${FROM_PHP}-fpm-alpine${FROM_ALPINE}

# Install packages from stable repo's
RUN apk add -u --no-cache curl bash su-exec less

# Copy libv8 from first build stage
COPY --from=v8build /tmp/libv8.tar.gz /tmp/libv8.tar.gz

# Install build dependencies
RUN apk add -u --no-cache --virtual .build-deps \
		$PHPIZE_DEPS \
		zlib-dev \
		g++ \
		make \

	# Install PHP Extensions
	&& apk add -u --no-cache \
		"libmcrypt-dev>=2.5.6" \
		freetype-dev \
		gettext-dev \
		icu-dev \
		imagemagick-dev \
		imagemagick \
		libjpeg-turbo-dev \
		libpng-dev \
		expat-dev \
		libxslt-dev \
		libssh2-dev \
		libzip-dev \
	&& export CFLAGS="$PHP_CFLAGS" CPPFLAGS="$PHP_CPPFLAGS" LDFLAGS="$PHP_LDFLAGS" \
	&& set -x \
	&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
	&& docker-php-ext-configure intl \
	&& docker-php-ext-configure pdo_mysql --with-pdo-mysql \
	&& docker-php-ext-configure xsl --with-xsl \
	&& docker-php-ext-install -j$(nproc) \
		calendar \
		exif \
		gd \
		gettext \
		intl \
		mysqli \
		opcache \
		pcntl \
		pdo_mysql \
		shmop \
		sockets \
		sysvmsg \
		sysvsem \
		sysvshm \
		wddx \
		xsl \
	&& pecl install \
		apcu \
		igbinary \
		imagick \
		mcrypt-1.0.1 \
		msgpack \
		redis \
		ssh2-1.1.2 \
		zip \
	&& docker-php-ext-enable \
		apcu \
		igbinary \
		imagick \
		mcrypt \
		msgpack \
		redis \
		ssh2 \
		zip \

	# XHProf
	&& export XHPROF_COMMIT=758773879899af22b87514e40abd042cbb2ab98c \
	&& export XHPROF_TMP_DIR=/tmp/xhprof-$XHPROF_COMMIT \
	&& curl -L https://github.com/humanmade/xhprof/archive/$XHPROF_COMMIT.zip > /tmp/xhprof.zip \
	&& unzip /tmp/xhprof.zip -d /tmp \
	&& ( \
		cd $XHPROF_TMP_DIR/extension \
		&& phpize \
		&& ./configure \
		&& make \
		&& make install \
	) \
	&& docker-php-ext-enable xhprof \
	&& rm /tmp/xhprof.zip \
	&& rm -R $XHPROF_TMP_DIR \

	# V8JS
	&& export V8_DIR=/usr/local/v8 \
	&& mkdir -p $V8_DIR \
	&& tar xzvf /tmp/libv8.tar.gz -C $V8_DIR \
	&& echo $V8_dir | pecl install v8js-2.1.0 \
	&& docker-php-ext-enable v8js \
	&& rm -rf /tmp/libv8.tar.gz \

	# Validation
	&& php -m \
	# Cleanup
	&& apk del .build-deps

# Install WP-CLI
# ncurses is used to install tput which is used for paging
RUN export WP_CLI_VERSION=2.0.1 \
	&& curl -s -o /usr/local/bin/wp -L https://github.com/wp-cli/wp-cli/releases/download/v$WP_CLI_VERSION/wp-cli-$WP_CLI_VERSION.phar \
	&& curl -s -o /tmp/sha512 -L https://github.com/wp-cli/wp-cli/releases/download/v$WP_CLI_VERSION/wp-cli-$WP_CLI_VERSION.phar.sha512 \
	&& chmod +x /usr/local/bin/wp \
	&& apk --no-cache add ncurses \
	&& [ "$(cat `which wp` | sha512sum | cut -d' ' -f1)" == "$(cat /tmp/sha512)" ] \
	&& rm -rf /tmp/sha512

# Install Cavalcade
RUN export CAVALCADE_COMMIT=3065001de4180d2082543867c9c6e6cfad026814 \
	&& curl -o /tmp/cavalcade.zip -L https://github.com/humanmade/Cavalcade-Runner/archive/$CAVALCADE_COMMIT.zip \
	&& unzip /tmp/cavalcade.zip -d /tmp \
	&& rm /tmp/cavalcade.zip \
	&& mv /tmp/Cavalcade-Runner-$CAVALCADE_COMMIT /etc/cavalcade \
	&& ln -s /etc/cavalcade/bin/cavalcade /usr/local/bin/cavalcade

# Install MySQL utilities
RUN apk add -u --no-cache mysql-client


RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Entrypoint
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

# PHP config
ENV PHP_INI_FILE=/usr/local/etc/php/php.ini
ENV PHP_FPM_CONF_FILE=/usr/local/etc/php-fpm.conf
ENV PHP_FPM_POOL_CONF_FILE=/usr/local/etc/php-fpm.d/www.conf
RUN rm /usr/local/etc/php-fpm.d/*.conf

COPY php.ini $PHP_INI_FILE
COPY fpm.conf $PHP_FPM_CONF_FILE
COPY fpm-pool.conf $PHP_FPM_POOL_CONF_FILE

RUN mkdir -p /var/run/php-fpm \
	&& chown www-data:www-data /var/run/php-fpm /usr/local/etc/php*

USER www-data
EXPOSE 9000
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["php-fpm"]
