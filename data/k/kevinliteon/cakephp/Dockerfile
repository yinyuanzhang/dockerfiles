FROM php:7.2-fpm


RUN apt-get update && apt-get install -y git libcurl4-gnutls-dev libicu-dev libxml2-dev libsqlite3-dev zlib1g-dev gnupg gnupg2 gnupg1

# php extension
RUN docker-php-ext-install zip curl pdo_sqlite mbstring pdo_mysql intl xml

RUN mkdir /srv/app

VOLUME ["/srv/app"]
WORKDIR "/srv/app"
