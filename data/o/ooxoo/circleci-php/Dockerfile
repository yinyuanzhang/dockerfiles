FROM ooxoo/php:7.2-cli-alpine3.8

ENV PHP_MEMORY_LIMIT=2G
ENV PHP_DATE_TIME_ZONE=Europe/Amsterdam

RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"; \
    php -r "if (hash_file('SHA384', 'composer-setup.php') === '93b54496392c062774670ac18b134c3b3a95e5a5e5c8f1a9f115f203b75bf9a129d5daa8ba6a13e2cc8a1da0806388a8') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"; \
    php composer-setup.php; \
    php -r "unlink('composer-setup.php');"; \
    mv composer.phar /usr/local/bin/composer;

RUN apk update; \
    apk add \
        openssh-client \
        git \
        unzip;

RUN apk add \
        g++ \
        make \
        autoconf; \
        pecl install xdebug; \
    apk del \
        g++ \
        make \
        autoconf; \
    rm -rf /tmp/*
