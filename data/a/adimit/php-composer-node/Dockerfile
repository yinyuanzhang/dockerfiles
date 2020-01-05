FROM alpine:3.6

MAINTAINER Aleksandar Dimitrov <a.dimitrov@seidemann-web.com>

RUN apk update \
 && apk add nodejs nodejs-npm ca-certificates php5 php5-openssl php5-phar php5-json php5-xml php5-mysqli php5-dom php5-pdo php5-curl php5-zlib php5-ctype php5-pcntl git curl \
 && ln -s /usr/bin/php5 /usr/bin/php

RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \
 && php -r "if (hash_file('SHA384', 'composer-setup.php') === '669656bab3166a7aff8a7506b8cb2d1c292f042046c5a994c43155c0be6190fa0355160742ab2e1c88d40d5be660b410') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;" \
 && php composer-setup.php \
 && php -r "unlink('composer-setup.php');" \
 && mv composer.phar /usr/bin/composer

RUN composer global require --dev deployer/deployer:~4.3.0 deployer/recipes:~4.0.7

VOLUME /app
WORKDIR /app
