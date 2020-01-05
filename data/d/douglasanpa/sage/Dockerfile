# Forked from TrafeX/docker-php-nginx (https://github.com/TrafeX/docker-php-nginx/)

FROM alpine:3.10
LABEL Maintainer="Douglas Andrade <douglasanpa@gmail.com>" \
      Description="Docker image for SAGE."

ENV APP_NAME SAGE - Sistema de Apoio à Gestão de Eventos
ENV DB_HOST mariadb
ENV DB_PORT 3306
ENV DB_DATABASE sage
ENV DB_USERNAME sage
ENV APP_ENV local
ENV OAUTH false

ARG GIT_CI_PASS

COPY wait-for-it.sh start.sh /

RUN apk --no-cache add tzdata gettext git php7 php7-fpm php7-pdo php7-mysqli php7-json php7-openssl php7-curl \
    php7-zlib php7-xml php7-phar php7-intl php7-dom php7-xmlreader php7-ctype php7-simplexml php7-zip \
    php7-mbstring php7-gd php7-xmlwriter php7-tokenizer php7-pdo_mysql php7-memcached php7-ftp php7-iconv php7-fileinfo \
    nginx supervisor curl bash nano jq openssl certbot certbot-nginx mariadb-client procps ca-certificates wget && \
    sed -i 's/memory_limit = 128M/memory_limit = 2048M/g' /etc/php7/php.ini && \
    sed -i 's/upload_max_filesize = 2M/upload_max_filesize = 256M/g' /etc/php7/php.ini && \
    sed -i 's/post_max_size = 8M/post_max_size = 512M/g' /etc/php7/php.ini && \
    curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer && \
    mkdir -p /src && \
    git clone --single-branch --branch master https://gitlab-ci-token:$GIT_CI_PASS@gitlab.com/Douglas_Leandro/sage.git /src && \
    mkdir -p /src/storage/ && \
    cd /src/ && \
    composer install --prefer-dist --no-ansi --no-interaction --no-progress --no-scripts  && \
    composer dump-autoload  && \
    php artisan config:cache  && \
    rm -rf .env.* && \
    rm -rf .git .git* && \
    rm -rf package*  && \
    rm -rf .php* phpunit* && \
    rm -f Procfile && \
    rm -f docker-compose.yml && \
    rm -rf README.md && \
    rm -rf start.ps1 && \
    rm -rf tests && \
    rm -rf update.sh && \
    rm -rf verify* && \
    rm -rf .vscode && \
    rm -rf webpack.mix.js && \
    rm -rf yarn.lock && \
    rm -rf *.sh && \
    rm -rf composer.lock && \
    jq -c 'del(.require)' composer.json > tmp.$$.json && mv tmp.$$.json composer.json && \
    rm -rf resources/assets/js/*-app.js && \
    rm -rf resources/assets/js/jquery.tagsinput-revisited.min.js && \
    chmod u+x /wait-for-it.sh && \
    chmod u+x /start.sh && \
    mkdir -p /src/bootstrap/cache /src/storage /src/storage/framework && \
    cd /src/storage/framework && \
    mkdir -p sessions views cache && \
    chmod 777 /src/storage -R && \
    apk del git tzdata jq

VOLUME ["/src/storage","/etc/letsencrypt/"]

COPY config/crontab /etc/crontabs/root
COPY config/nginx.conf /etc/nginx/nginx.conf
COPY config/fpm-pool.conf /etc/php7/php-fpm.d/zzz_custom.conf
COPY config/php.ini /etc/php7/conf.d/zzz_custom.ini
COPY config/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY config/.env_sage /src/.env_sage

CMD chown root:root /etc/crontabs/root && /usr/sbin/crond -f

WORKDIR /src

EXPOSE 80
EXPOSE 443

ENTRYPOINT /wait-for-it.sh $DB_HOST:$DB_PORT --strict --timeout=120 -- /start.sh
