FROM php:7.1-apache

ARG DOCKER_TAG
RUN export DOCKER_TAG=$DOCKER_TAG

COPY / /var/www/html/

# Install PDO MySQL driver
# See https://github.com/docker-library/php/issues/62
RUN docker-php-ext-install pdo mysqli
RUN docker-php-ext-install pdo_mysql

RUN apt-get update && apt-get install -y git

# Workaround for write permission on write to MacOS X volumes
# See https://github.com/boot2docker/boot2docker/pull/534
RUN usermod -u 1000 www-data

# Enable Apache mod_rewrite
RUN a2enmod rewrite

# Enable Apache mod_rewrite
RUN a2enmod headers

# Enable Apache mod_rewrite
RUN a2enmod expires

RUN curl -sL https://sentry.io/get-cli/ | bash
ENV SENTRY_AUTH_TOKEN=a5b8db140a83419b8c5f739ef2488ac858970d14c0fb49d592327156f71e5d27
ENV SENTRY_ORG=nexatlas-s2
ENV SENTRY_PROJECT=backend
RUN sentry-cli releases new $(sentry-cli releases propose-version) --project $SENTRY_PROJECT
RUN sentry-cli releases set-commits $(sentry-cli releases propose-version) --auto
RUN sentry-cli releases finalize $(sentry-cli releases propose-version)
RUN sentry-cli releases deploys $(sentry-cli releases propose-version) new -e $DOCKER_TAG
