FROM php:5-alpine

# Build-time metadata as defined at http://label-schema.org
ARG BUILD_DATE
ARG VCS_REF
ARG VERSION
LABEL maintainer="James Zhu <168262+fatindeed@users.noreply.github.com>" \
      org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.name="fatinded/php:xdebug5" \
      org.label-schema.description="PHP5 with Xdebug" \
      org.label-schema.url="https://hub.docker.com/r/fatindeed/php/" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/fatindeed/docker-php" \
      org.label-schema.vendor="James Zhu" \
      org.label-schema.version=$VERSION \
      org.label-schema.schema-version="1.0"

ARG ALPINE_MIRROR

RUN set -e; \
# Switch to mirror if environment variable exists
    if [ -n "$ALPINE_MIRROR" ]; then \
        sed -i 's!http://dl-cdn.alpinelinux.org!'"$ALPINE_MIRROR"'!g' /etc/apk/repositories; \
    fi; \
    apk add --no-cache --virtual .phpize-deps-configure $PHPIZE_DEPS; \
    pecl install xdebug-2.5.5; \
    docker-php-ext-enable xdebug; \
    docker-php-source delete; \
    apk del .phpize-deps-configure; \
    runDeps="$( \
        scanelf --needed --nobanner --format '%n#p' --recursive /usr/local/lib/php/extensions \
        | tr ',' '\n' \
        | sort -u \
        | awk 'system("[ -e /usr/local/lib/" $1 " ]") == 0 { next } { print "so:" $1 }' \
    )"; \
    apk add --no-cache --virtual .php-rundeps $runDeps tzdata; \
    rm -rf /tmp/pear; \
    rm -rf /usr/local/include; \
    rm -rf /var/cache/apk/*; \
# Support timezone environment variable
    { \
        head -n -1 /usr/local/bin/docker-php-entrypoint; \
        echo 'if [ ! -z "$TIMEZONE" ]; then'; \
        echo '    cp "/usr/share/zoneinfo/${TIMEZONE}" /etc/localtime'; \
        echo '    echo "$TIMEZONE" > /etc/timezone'; \
        echo '    echo "date.timezone = $TIMEZONE" > /usr/local/etc/php/conf.d/timezone.ini'; \
        echo 'fi'; \
        echo ; \
        tail -n 1 /usr/local/bin/docker-php-entrypoint; \
    } | tee /tmp/docker-php-entrypoint; \
    chmod a+x /tmp/docker-php-entrypoint; \
    mv /tmp/docker-php-entrypoint /usr/local/bin/; \
# Xdebug config
    { \
        echo 'xdebug.remote_enable = 1'; \
        echo 'xdebug.remote_autostart = 1'; \
        echo 'xdebug.remote_log = /proc/self/fd/2'; \
    } | tee -a /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini;

WORKDIR /home/www-data