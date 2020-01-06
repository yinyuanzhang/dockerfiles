FROM php:7.3-alpine

RUN apk update && \
    apk upgrade && \
    apk add bash su-exec && \
    # install app
    curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

ADD / /app/
COPY resources/run.sh /run.sh

RUN cd /app && \
    composer install --no-dev --no-interaction --no-progress && \
    composer dump-autoload --optimize --no-dev --classmap-authoritative && \
    composer clear-cache && \
    chmod +x /app/bin/app && \
    chmod +x /run.sh

ENTRYPOINT ["/run.sh", "php", "/app/bin/app"]
