FROM nginx:1.17-alpine

ENV APP_PATH=/var/www/html \
    HOST=example.com \
    APP_MAGE_MODE=production \
    PHPFPM_HOST=localhost \
    PHPFPM_PORT=9000

RUN apk add --no-cache --virtual .build-deps \
        shadow \
    && adduser -S -D -H -u 82 -h /var/cache/nginx -s /sbin/nologin -G www-data -g www-data www-data \
    && usermod -a -G www-data nginx \
    && mkdir -p ${APP_PATH} \
    && chown -R nginx:www-data ${APP_PATH} \
    && apk del .build-deps

COPY docker-nginx-*.template /etc/nginx/conf.d/
COPY docker-nginx-snippets/ /etc/nginx/snippets/
COPY docker-nginx-entrypoint /usr/local/bin/

WORKDIR ${APP_PATH}

ENTRYPOINT [ "docker-nginx-entrypoint" ]

CMD [ "nginx", "-g", "daemon off;" ]
