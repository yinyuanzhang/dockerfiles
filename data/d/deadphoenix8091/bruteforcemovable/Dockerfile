FROM alpine:latest
LABEL maintainer="deadphoenix8091"

RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories && \
    apk upgrade --no-cache && \
    apk --no-cache add \
        tzdata supervisor nginx php7 php7-fpm php7-pear \
        php7-xml php7-redis php7-bcmath \
        php7-pdo php7-pdo_mysql php7-mysqli php7-mbstring php7-gd php7-mcrypt \
        php7-openssl php7-apcu php7-gmagick php7-xsl php7-zip php7-sockets \
        php7-ldap php7-phar php7-iconv php7-json php7-intl php7-memcached \
        php7-oauth php7-imap php7-gmp \
        g++ make autoconf && \
    cp /usr/share/zoneinfo/UTC /etc/localtime && \
    echo "UTC" > /etc/timezone && \
    mkdir -p /run/nginx


RUN mkdir -p /etc/nginx/sites-enabled

COPY ./docker/nginx.site.conf /etc/nginx/conf.d/default.conf
COPY ./docker/supervisord.conf /etc/supervisord.conf
COPY ./ /app

RUN sed -e 's/;clear_env = no/clear_env = no/' -i /etc/php7/php-fpm.d/www.conf

RUN cd /app && \
    php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \
    php -r "if (hash_file('sha384', 'composer-setup.php') === 'a5c698ffe4b8e849a443b120cd5ba38043260d5c4023dbf93e1558871f1f07f58274fc6f4c93bcfd858c6bd0775cd8d1') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;" && \
    php composer-setup.php && \
    php -r "unlink('composer-setup.php');" && \
    php composer.phar install

ENTRYPOINT ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisord.conf"]
