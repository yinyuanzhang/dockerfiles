FROM bakerdist/magento2-php:2.3-php7.3-cli-alpine

RUN apk --update add --no-cache \
        patch \
        tini \
        git

COPY --from=composer:1.9 /usr/bin/composer /usr/bin/composer

COPY docker-composer-* /usr/local/bin

ENTRYPOINT ["docker-composer-entrypoint"]

CMD ["composer"]

USER www-data

RUN composer global require hirak/prestissimo
