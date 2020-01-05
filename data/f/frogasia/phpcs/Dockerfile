FROM cytopia/phpcs:3-php7.3

RUN apk add parallel

RUN curl -sS https://getcomposer.org/installer -o composer-setup.php && \
    php composer-setup.php --install-dir=/usr/local/bin --filename=composer && \
    rm -f composer-setup.php

RUN composer global require phpcompatibility/php-compatibility && \
    phpcs --config-set installed_paths /root/.composer/vendor/phpcompatibility/php-compatibility
