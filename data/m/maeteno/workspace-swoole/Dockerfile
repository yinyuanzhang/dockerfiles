FROM hyperf/hyperf:7.2-alpine-cli
LABEL maintainer="Alan <ssisoo@live.cn>"

ARG timezone

ENV TIMEZONE=${timezone:-"Asia/Shanghai"} \
    COMPOSER_VERSION=1.8.6 \
    APP_ENV=test

# update
RUN set -ex \
    && apk update \
    # install mysql
    && apk add mariadb mariadb-client \
    && mysql_install_db --user=mysql --datadir=/var/lib/mysql \
    && cp /usr/share/mariadb/mysql.server /etc/init.d/mysqld \
    && /etc/init.d/mysqld start \
    && /usr/bin/mysqladmin -u root password root \
    # install redis
    && apk add redis \
    && echo "daemonize yes" >> /etc/redis.conf \
    && redis-server /etc/redis.conf \
    # install composer
    && cd /tmp \
    && wget https://github.com/composer/composer/releases/download/${COMPOSER_VERSION}/composer.phar \
    && chmod u+x composer.phar \
    && mv composer.phar /usr/local/bin/composer \
    # show php version and extensions
    && php -v \
    && php -m \
    #  ---------- some config ----------
    && cd /etc/php7 \
    # - config PHP
    && { \
        echo "upload_max_filesize=100M"; \
        echo "post_max_size=108M"; \
        echo "memory_limit=1024M"; \
        echo "date.timezone=${TIMEZONE}"; \
    } | tee conf.d/99-overrides.ini \
    # - config timezone
    && ln -sf /usr/share/zoneinfo/${TIMEZONE} /etc/localtime \
    && echo "${TIMEZONE}" > /etc/timezone \
    # ---------- clear works ----------
    && rm -rf /var/cache/apk/* /tmp/* /usr/share/man \
    && echo -e "\033[42;37m Build Completed :).\033[0m\n"

CMD ["/bin/sh"]
