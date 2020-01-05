FROM saschaegerer/ubuntu:18.04
ARG DEBIAN_FRONTEND=noninteractive

ENV PHP_VERSION=7.3
RUN set -xe && \
    apt-get update && \
    buildDependencies="\
        software-properties-common \
        build-essential \
        php-pear \
        gpg-agent \
    " && \
    apt-get install --no-install-recommends -y $buildDependencies curl && \
    curl -s https://packages.blackfire.io/gpg.key | APT_KEY_DONT_WARN_ON_DANGEROUS_USAGE=DontWarn apt-key add - && \
    echo "deb https://packages.blackfire.io/debian any main" | tee /etc/apt/sources.list.d/blackfire.list && \
    add-apt-repository ppa:ondrej/php && \
    apt-get update && \
    buildDependencies="$buildDependencies\
        php7.3-dev \
    " && \
    apt-get install --no-install-recommends -y $buildDependencies libfreetype6-dev libxml2-dev libcurl4-openssl-dev libsqlite3-dev libssl-dev libpcre3-dev libpng-dev libjpeg-dev libzip-dev libedit-dev libltdl-dev libpaper-utils ghostscript curl xz-utils binutils blackfire-php php7.3-fpm php7.3-mbstring php7.3-gd php7.3-soap php7.3-zip php7.3-xml dh-php xml-core pkg-php-tools && \
    apt-mark manual libfreetype6-dev libxml2-dev libcurl4-openssl-dev libsqlite3-dev libssl-dev libpcre3-dev libpng-dev libjpeg-dev libzip-dev libedit-dev libltdl-dev libpaper-utils ghostscript curl xz-utils binutils blackfire-php php7.3-fpm php7.3-mbstring php7.3-gd php7.3-soap php7.3-zip php7.3-xml dh-php xml-core pkg-php-tools && \
    pecl update-channels && \
    pecl channel-update pecl.php.net && \
    pecl install xdebug-alpha && \
    pecl clear-cache && \
    apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false $buildDependencies && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY bin/* /usr/local/bin/
COPY my_custom.ini /etc/php/7.3/mods-available/
COPY php-fpm.conf /etc/php/7.3/fpm/pool.d/z_custom.conf

RUN set -xe && \
    mkdir -p /var/www /run/php && \
    echo "zend_extension=xdebug.so\nxdebug.max_nesting_level=1500" >> /etc/php/7.3/mods-available/xdebug.ini && \
    touch /etc/php/7.3/mods-available/blackfire.ini && \
    # make the blackfire and xdebug config file writeable for www-data.
    # this is a bit insecure but ok in that case as this image should only be used in development
    chown -R www-data:www-data /var/www /run/php /etc/php/7.3/mods-available/blackfire.ini /etc/php/7.3/mods-available/xdebug.ini && \
    phpenmod my_custom xdebug && \
    printf 'blackfire.agent_socket="${BLACKFIRE_SOCKET}"\n' >> /etc/php/7.3/mods-available/blackfire.ini && \
    echo "include=/etc/php/7.3/fpm/pool.d/*.conf" >> /etc/php/7.3/fpm/php-fpm.conf

ENTRYPOINT ["tini", "php-entrypoint", "--"]

WORKDIR /var/www
USER www-data

EXPOSE 9000
CMD ["php-fpm7.3"]
