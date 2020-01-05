FROM php:7.2-apache

ARG POSTFIXADMIN_VERSION=3.1
ARG POSTFIXADMIN_SHA512=3bda4e9d4a7308d22edca30d181af76b7153e57b19bda878e32f5eeeb49127f46581c966706bcca13cd31740cadacc584e15830aa157b4655e60d44d66f45ddd

RUN docker-php-ext-install \
    mysqli \
    pdo \
    pdo_mysql

ENV POSTFIXADMIN_VERSION $POSTFIXADMIN_VERSION
ENV POSTFIXADMIN_SHA512 $POSTFIXADMIN_SHA512

RUN set -eu; \
    curl -o postfixadmin.tar.gz -SL "https://github.com/postfixadmin/postfixadmin/archive/postfixadmin-${POSTFIXADMIN_VERSION}.tar.gz"; \
    echo "$POSTFIXADMIN_SHA512 *postfixadmin.tar.gz" | sha512sum -c -; \
    # upstream tarball include ./postfixadmin-postfixadmin-${POSTFIXADMIN_VERSION}/
    tar -xzf postfixadmin.tar.gz -C /usr/src/; \
    mv /usr/src/postfixadmin-postfixadmin-${POSTFIXADMIN_VERSION} /usr/src/postfixadmin; \
    rm postfixadmin.tar.gz; \
    # Does not exist in tarball but is required
    mkdir -p /usr/src/postfixadmin/templates_c; \
    cp -r /usr/src/postfixadmin/* /var/www/html; \
    chown -R www-data:www-data /var/www/html

COPY docker-entrypoint.sh /usr/local/bin/
COPY create-postfixadmin-db.php /var/www/html/

ENV POSTFIX_DB_HOST POSTFIX_DB_NAME POSTFIX_DB_USER POSTFIX_DB_PASSWORD POSTFIXADMIN_SETUP_PASSWORD MYSQL_USER MYSQL_PASS SERVER_NAME

WORKDIR /var/www/html

EXPOSE 80
ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["apache2-foreground"]