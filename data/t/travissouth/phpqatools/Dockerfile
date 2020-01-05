FROM travissouth/composer:1.8.5
RUN apk add --update nodejs
RUN apk update \
    && apk add --no-cache libmcrypt libmcrypt-dev openssh-client icu-dev \
    libxml2-dev freetype-dev libpng-dev libjpeg-turbo-dev g++ make autoconf \
    && pecl install xdebug \
    && echo "zend_extension=$(find /usr/local/lib/php/extensions/ -name xdebug.so)" > \
    /usr/local/etc/php/conf.d/xdebug.ini \
    && echo "xdebug.remote_enable=on" >> /usr/local/etc/php/conf.d/xdebug.ini \
    && echo "xdebug.remote_autostart=off" >> /usr/local/etc/php/conf.d/xdebug.ini && php -m
RUN composer global require travis-south/phpqatools:5.0.0 \
	behat/mink-extension \
	behat/mink-goutte-driver \
	behat/mink-selenium2-driver \
	behat/mink-zombie-driver \
	drupal/coder \
    rregeer/phpunit-coverage-check
RUN /tmp/vendor/bin/phpcs --config-set installed_paths \
    /tmp/vendor/drupal/coder/coder_sniffer
ENV PATH="/tmp/vendor/bin:${PATH}"
WORKDIR /app
ENTRYPOINT []
