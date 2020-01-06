FROM php:7.2.5-cli-alpine3.7

ADD src /opt/box2

RUN echo "memory_limit=-1" > "$PHP_INI_DIR/conf.d/memory-limit.ini" && \
    echo "date.timezone=${PHP_TIMEZONE:-UTC}" > "$PHP_INI_DIR/conf.d/date_timezone.ini" && \
    echo "phar.readonly=off" >> "$PHP_INI_DIR/conf.d/phar.ini"

RUN curl -LSs https://box-project.github.io/box2/installer.php | php && \
    mv box.phar /usr/local/bin/box && \
    chmod +x /usr/local/bin/box

ENV BOX_MAIN=app.php
ENV BOX_OUTPUT=app.phar
ENV BOX_DIR=src,vendor
ENV BOX_JSON=/app/box.json

WORKDIR /app

ENTRYPOINT ["/opt/box2/entrypoint.sh"]
