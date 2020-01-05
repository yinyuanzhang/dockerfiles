FROM php:fpm-alpine
MAINTAINER Ivan Bojko <ivan.bojko@heptaedre.com>

# Timezone
ENV TIMEZONE Europe/Paris

# Configure Timezone then install some PHP extensions
RUN apk update && \
    apk upgrade && \
    apk add --no-cache openrc tzdata ca-certificates wget python python-dev py-configobj git util-linux procps gcc musl-dev linux-headers libzip-dev libxml2-dev freetype freetype-dev jpeg-dev libjpeg-turbo libjpeg-turbo-dev libpng libpng-dev jpegoptim optipng && \
    cp /usr/share/zoneinfo/${TIMEZONE} /etc/localtime && \
    echo "${TIMEZONE}" > /etc/timezone && \
    apk add --no-cache icu-dev && \
    docker-php-ext-configure intl && \
    docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ --with-png-dir=/usr/include/ && \
    docker-php-ext-install exif gd iconv intl json opcache pdo pdo_mysql xml zip && \
    apk del ca-certificates wget python-dev py-configobj git gcc musl-dev linux-headers tzdata && \
    rm -rf /var/cache/apk/* && \
    ln -sf /srv /var/www/html/

COPY ./log-rotation.sh /log-rotation.sh
COPY ./entrypoint.sh /entrypoint.sh

RUN chmod +x /log-rotation.sh

ENTRYPOINT ["/entrypoint.sh"]

WORKDIR /srv/

# Exact copy of PHP:fpm-alpine Dockerfile
RUN set -ex \
	&& cd /usr/local/etc \
	&& if [ -d php-fpm.d ]; then \
		# for some reason, upstream's php-fpm.conf.default has "include=NONE/etc/php-fpm.d/*.conf"
		sed 's!=NONE/!=!g' php-fpm.conf.default | tee php-fpm.conf > /dev/null; \
		cp php-fpm.d/www.conf.default php-fpm.d/www.conf; \
	else \
		# PHP 5.x doesn't use "include=" by default, so we'll create our own simple config that mimics PHP 7+ for consistency
		mkdir php-fpm.d; \
		cp php-fpm.conf.default php-fpm.d/www.conf; \
		{ \
			echo '[global]'; \
			echo 'include=etc/php-fpm.d/*.conf'; \
		} | tee php-fpm.conf; \
	fi \
	&& { \
		echo '[global]'; \
		echo 'error_log = /proc/self/fd/2'; \
		echo; \
		echo '[www]'; \
		echo '; if we send this to /proc/self/fd/1, it never appears'; \
		echo 'access.log = /proc/self/fd/2'; \
		echo; \
		echo 'clear_env = no'; \
		echo; \
		echo '; Ensure worker stdout and stderr are sent to the main error log.'; \
		echo 'catch_workers_output = yes'; \
	} | tee php-fpm.d/docker.conf \
	&& { \
		echo '[global]'; \
		echo 'daemonize = no'; \
		echo; \
		echo '[www]'; \
		echo 'listen = 9000'; \
	} | tee php-fpm.d/zz-docker.conf

EXPOSE 9000
CMD ["php-fpm"]
