FROM amazeeio/php:7.2-cli-drupal

ENV WEBROOT=docroot \
    COMPOSER_ALLOW_SUPERUSER=1 \
    COMPOSER_CACHE_DIR=/tmp/.composer/cache

ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz

RUN apk update \
    && apk del nodejs nodejs-current yarn \
    && apk add nodejs-npm patch rsync jq --no-cache --repository http://dl-3.alpinelinux.org/alpine/v3.7/main/

# Add common drupal config.
RUN mkdir /bay
COPY docker/services.yml /bay
COPY docker/redis-unavailable.services.yml /bay
COPY docker/settings.php /bay
