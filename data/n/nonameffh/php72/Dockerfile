FROM nonameffh/php72:latest

LABEL maintainer="Aleksey Tarasov <nonameffh@gmail.com>"

## add packages
RUN pecl install xdebug \
    && php-enable-extension xdebug.so \
    && php-source delete