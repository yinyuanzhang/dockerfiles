FROM alpine:3.7

RUN apk add --update php7 php7-sqlite3 php7-json php7-phar php7-mbstring php7-openssl php7-dom php7-tokenizer php7-xml php7-pdo php7-pdo_sqlite curl git

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin --filename=composer

RUN git clone https://github.com/devfake/flox

WORKDIR flox/backend

RUN composer install
