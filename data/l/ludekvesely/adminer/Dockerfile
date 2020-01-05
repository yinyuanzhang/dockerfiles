FROM alpine:3.8

RUN	addgroup -S adminer && \
    adduser -S -G adminer adminer && \
    mkdir -p /var/adminer && \
    chown -R adminer:adminer /var/adminer

RUN apk add --no-cache \
    curl \
    php7 \
    php7-opcache \
    php7-pdo \
    php7-pdo_mysql \
    php7-pdo_odbc \
    php7-pdo_pgsql \
    php7-pdo_sqlite \
    php7-session

WORKDIR /var/adminer

ARG ADMINER_VERSION=4.7.1
ARG ADMINER_FLAVOUR="-en"
ARG ADMINER_CHECKSUM="7897ac51d8e50c550acae4204d0139cb2a5d0b6c11ca506978b237f8fe540fd1"

RUN curl -L https://github.com/vrana/adminer/releases/download/v${ADMINER_VERSION}/adminer-${ADMINER_VERSION}${ADMINER_FLAVOUR}.php -o adminer.php && \
    echo "${ADMINER_CHECKSUM}  adminer.php"|sha256sum -c - && \
    wget https://raw.github.com/vrana/adminer/master/plugins/plugin.php && \
    test -s plugin.php && \
    wget https://raw.github.com/vrana/adminer/master/plugins/tables-filter.php && \
    test -s tables-filter.php

COPY index.php /var/adminer/index.php
COPY adminer.css /var/adminer/adminer.css

EXPOSE 8080

USER adminer
CMD [ "php", "-S", "[::]:8080", "-t", "/var/adminer" ]

