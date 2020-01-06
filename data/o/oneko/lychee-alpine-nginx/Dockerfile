FROM alpine

RUN apk --no-cache add \
    coreutils \
    supervisor \
    nginx \
    php7 \
    php7-fpm \
    php7-zip \
    php7-gd \
    php7-exif \
    php7-apcu \
    php7-json \
    php7-mbstring \
    php7-mysqli \
    php7-opcache \
    php7-session \
    php7-imagick \
    imagemagick \
    tzdata \
    git


RUN set -x ; \
    addgroup -g 82 -S www-data ; \
    adduser -u 82 -D -S -G www-data www-data && exit 0 ; exit 1

COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY nginx/lychee.conf /etc/nginx/conf.d/default.conf
ENV VIRTUAL_HOST="lychee.lan"
RUN sed -i "s|server_name lychee.lan;|server_name ${VIRTUAL_HOST};|g" /etc/nginx/conf.d/default.conf

ENV PHP_FPM_USER="www-data" \
    PHP_FPM_GROUP="www-data" \
    PHP_FPM_LISTEN_MODE="0660" \
    PHP_MEMORY_LIMIT="1024M" \
    PHP_MAX_UPLOAD="1000M" \
    PHP_MAX_FILE_UPLOAD="600" \
    PHP_MAX_POST="10000M" \
    PHP_MAX_EXECUTION_TIME="3600" \
    PHP_DISPLAY_ERRORS="On" \
    PHP_DISPLAY_STARTUP_ERRORS="On" \
    PHP_ERROR_REPORTING="E_COMPILE_ERROR\|E_RECOVERABLE_ERROR\|E_ERROR\|E_CORE_ERROR" \
    PHP_CGI_FIX_PATHINFO=0

RUN sed -i "s|;listen.owner\s*=\s*nobody|listen.owner = ${PHP_FPM_USER}|g" /etc/php7/php-fpm.conf && \
    sed -i "s|;listen.group\s*=\s*nobody|listen.group = ${PHP_FPM_GROUP}|g" /etc/php7/php-fpm.conf && \
    sed -i "s|;listen.mode\s*=\s*0660|listen.mode = ${PHP_FPM_LISTEN_MODE}|g" /etc/php7/php-fpm.conf && \
    sed -i "s|user\s*=\s*nobody|user = ${PHP_FPM_USER}|g" /etc/php7/php-fpm.conf && \
    sed -i "s|group\s*=\s*nobody|group = ${PHP_FPM_GROUP}|g" /etc/php7/php-fpm.conf && \
    sed -i "s|;log_level\s*=\s*notice|log_level = notice|g" /etc/php7/php-fpm.conf && \
    sed -i "s|display_errors\s*=\s*Off|display_errors = ${PHP_DISPLAY_ERRORS}|i" /etc/php7/php.ini && \
    sed -i "s|max_execution_time\s*=\s*30|max_execution_time = ${PHP_MAX_EXECUTION_TIME}|i" /etc/php7/php.ini && \
    sed -i "s|display_startup_errors\s*=\s*Off|display_startup_errors = ${PHP_DISPLAY_STARTUP_ERRORS}|i" /etc/php7/php.ini && \
    sed -i "s|error_reporting\s*=\s*E_ALL & ~E_DEPRECATED & ~E_STRICT|error_reporting = ${PHP_ERROR_REPORTING}|i" /etc/php7/php.ini && \
    sed -i "s|;*memory_limit =.*|memory_limit = ${PHP_MEMORY_LIMIT}|i" /etc/php7/php.ini && \
    sed -i "s|;*upload_max_filesize =.*|upload_max_filesize = ${PHP_MAX_UPLOAD}|i" /etc/php7/php.ini && \
    sed -i "s|;*max_file_uploads =.*|max_file_uploads = ${PHP_MAX_FILE_UPLOAD}|i" /etc/php7/php.ini && \
    sed -i "s|;*post_max_size =.*|post_max_size = ${PHP_MAX_POST}|i" /etc/php7/php.ini && \
    sed -i "s|;opcache.validate_timestamps=.*|opcache.validate_timestamps=0|i" /etc/php7/php.ini && \
    sed -i "s|;*cgi.fix_pathinfo=.*|cgi.fix_pathinfo= ${PHP_CGI_FIX_PATHINFO}|i" /etc/php7/php.ini && \
    sed -i "s|user\s*=\s*nobody|user = ${PHP_FPM_USER}|g" /etc/php7/php-fpm.d/www.conf && \
    sed -i "s|group\s*=\s*nobody|group = ${PHP_FPM_USER}|g" /etc/php7/php-fpm.d/www.conf && \
    sed -i "s|;clear_env = no|clear_env = no|i" /etc/php7/php-fpm.d/www.conf


ENV TIMEZONE "Europe/Madrid"

RUN cp /usr/share/zoneinfo/${TIMEZONE} /etc/localtime && \
    echo "${TIMEZONE}" > /etc/timezone && \
    sed -i "s|;*date.timezone =.*|date.timezone = ${TIMEZONE}|i" /etc/php7/php.ini

ADD init.sh /
RUN chmod 777 /init.sh && chmod 777 /var/www
ADD supervisord.conf /etc/supervisord.conf
RUN ln -sf /dev/stdout /var/log/nginx/lychee_access.log && ln -sf /dev/stderr /var/log/nginx/lychee_error.log
RUN ln -sf /dev/stderr /var/log/php7/error.log
RUN chown -R www-data:www-data /var/tmp/nginx


USER www-data
WORKDIR /var/www
RUN git clone https://github.com/LycheeOrg/Lychee.git
WORKDIR /var/www/Lychee
RUN git submodule init ; git submodule update

#RUN chown nobody:nobody uploads data && chmod -R 777 uploads/ data/

ADD config.php /var/www/Lychee/data
#RUN chown www-data:www-data /var/www/Lychee/data/config.php

ADD install.php ./php

ENV MYSQL_HOST "localhost"
ENV MYSQL_USER "lychee"
ENV MYSQL_PASSWORD "lychee"
ENV MYSQL_NAME "lychee"
ENV MYSQL_PREFIX ""
USER root
EXPOSE 80
ENTRYPOINT /init.sh
