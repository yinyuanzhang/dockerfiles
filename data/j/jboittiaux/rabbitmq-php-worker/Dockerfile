FROM composer:1.6

ENV APP_HOME /app

ENV RABBITMQ_HOST ''
ENV RABBITMQ_PORT 5672
ENV RABBITMQ_USER 'guest'
ENV RABBITMQ_PASS 'guest'

RUN apk upgrade --update && apk add \
        imap-dev \
        openssl-dev \
    && docker-php-ext-install bcmath \
    && docker-php-ext-configure imap \
    && docker-php-ext-configure imap --with-imap --with-imap-ssl \
    && docker-php-ext-install imap

COPY default-app $APP_HOME
RUN cp /app/config.php.dist /app/config.php

COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

WORKDIR "$APP_HOME"

ENTRYPOINT ["/docker-entrypoint.sh"]

EXPOSE 8080

CMD ["php", "index.php"]
