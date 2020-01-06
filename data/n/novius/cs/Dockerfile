FROM php:7-alpine

RUN apk add --no-cache \
        bash \
        grep \
        pcre \
        python \
        make \
        gcc \
        g++ \
        git \
        nodejs \
        ruby-bundler \
        ruby-json \
        ruby-io-console \
   && curl -o /usr/local/bin/php-cs-fixer http://cs.sensiolabs.org/download/php-cs-fixer-v2.phar \
   && chmod +x /usr/local/bin/php-cs-fixer \
   && ln -s php-cs-fixer /usr/local/bin/php-cs-fixer-v2 \
   && curl -s https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin/ --filename=composer \
   && addgroup -Sg 1000 ci \
   && adduser -SG ci -u 1000 -h /src ci
