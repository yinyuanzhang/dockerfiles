FROM composer

RUN composer global require aerocommerce/cli \
    && docker-php-ext-install pdo_mysql \
    && mkdir /sites

WORKDIR /sites

VOLUME [ "/sites" ]

ENTRYPOINT /tmp/vendor/bin/aero new ${APP_NAME} --docker