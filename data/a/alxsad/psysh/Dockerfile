FROM composer/composer:php7
MAINTAINER Alex Davidovich <alxsad@gmail.com>

WORKDIR /tmp

RUN composer selfupdate && \
    composer require "psy/psysh" --prefer-source --no-interaction && \
    ln -s /tmp/vendor/bin/psysh /usr/local/bin/psysh

VOLUME ["/app"]
WORKDIR /app

ENTRYPOINT ["/usr/local/bin/psysh"]
CMD ["--help"]
