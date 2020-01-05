FROM richbrains/symfony

RUN apk --update --no-cache add \
        wkhtmltopdf \
        nano \
        ttf-freefont \
    && rm -rf /var/cache/apk/*

RUN apk add --no-cache --virtual .mongodb-ext-build-deps autoconf gcc g++ make openssl-dev && \
    pecl install mongodb && \
    pecl clear-cache && \
    apk del .mongodb-ext-build-deps

RUN docker-php-ext-enable mongodb.so && \
    docker-php-source delete