FROM alpine:edge
MAINTAINER contact@etopian.com

ENV LANG="en_US.UTF-8" \
    LC_ALL="C.UTF-8" \
    LANGUAGE="en_US.UTF-8" \
    TERM="xterm" \
    OUTPUT_FILE_NAME=/phpmyadmin.tar.xz \
    PHP_MYADMIN_VERSION="4.7.4" \
    PMA_SECRET="" \
    PMA_DB="phpmyadmin" \
    PMA_USERNAME="pma" \
    PMA_PASSWORD="password" \
    MYSQL_HOSTNAME="mysql"

RUN apk upgrade && \
    apk --update add \
      php7 php7-mbstring php7-session php7-bcmath php7-cli php7-ctype php7-curl php7-fpm php7-gd php7-json php7-mcrypt php7-mysqli \
      php7-opcache  php7-openssl php7-pdo php7-pdo_mysql php7-phar php7-xml php7-zip php7-zlib ca-certificates \
      nginx mysql-client \
      curl xz sed \
      && \
    curl -L http://files.phpmyadmin.net/phpMyAdmin/${PHP_MYADMIN_VERSION}/phpMyAdmin-${PHP_MYADMIN_VERSION}-all-languages.tar.xz -o ${OUTPUT_FILE_NAME} && \
    TEST_FILE=$(sha1sum ${OUTPUT_FILE_NAME}) && \
    tar -xJpf /phpmyadmin.tar.xz && \
    rm -rf /phpmyadmin.tar.xz && \
    mkdir -p /www/ && \
    mv /phpMyAdmin-*-all-languages /www/phpmyadmin && \
    chown -R nginx: /www/phpmyadmin && \
    sed -E \
        -e "s/^(.+\['compress'\]\s*=\s*).+/\1 true;/" \
        -e "s/^(.+\['blowfish_secret'\]\s*=\s*).+/\1 '${PMA_SECRET}';/" \
        -e "s/^(.+\['host'\]\s*=\s*).+/\1 '${MYSQL_HOSTNAME}';/" \
        -e "s/^.+? (\\$.+\['controluser'\]\s*=\s*).+/\1 '${PMA_USERNAME}';/" \
        -e "s/^.+? (\\$.+\['controlpass'\]\s*=\s*).+/\1 '${PMA_PASSWORD}';/" \
        -e "s/^\/\/ (\\$.+pmadb)/\1/" \
        -e "s/^\/\/ (\\$.+bookmarktable)/\1/" \
        -e "s/^\/\/ (\\$.+relation)/\1/" \
        -e "s/^\/\/ (\\$.+table_info)/\1/" \
        -e "s/^\/\/ (\\$.+table_coords)/\1/" \
        -e "s/^\/\/ (\\$.+pdf_pages)/\1/" \
        -e "s/^\/\/ (\\$.+column_info)/\1/" \
        -e "s/^\/\/ (\\$.+history)/\1/" \
        -e "s/^\/\/ (\\$.+table_uiprefs)/\1/" \
        -e "s/^\/\/ (\\$.+tracking)/\1/" \
        -e "s/^\/\/ (\\$.+userconfig)/\1/" \
        -e "s/^\/\/ (\\$.+recent)/\1/" \
        -e "s/^\/\/ (\\$.+favorite)/\1/" \
        -e "s/^\/\/ (\\$.+users)/\1/" \
        -e "s/^\/\/ (\\$.+usergroups)/\1/" \
        -e "s/^\/\/ (\\$.+navigationhiding)/\1/" \
        -e "s/^\/\/ (\\$.+savedsearches)/\1/" \
        -e "s/^\/\/ (\\$.+central_columns)/\1/" \
      /www/phpmyadmin/config.sample.inc.php > /www/phpmyadmin/config.inc.php && \
      sed -i \
        -e "s/upload_max_filesize = .*/upload_max_filesize = 64M/" \
        -e "s/post_max_size = .*/post_max_size = 64M/"  \
        -e "s/short_open_tag = .*/short_open_tag = Off/" \
        -e "s/;date.timezone =/date.timezone = Africa\/Johannesburg/" \
        -e "s/memory_limit = .*/memory_limit = 512M/" \
        -e "s/max_execution_time = .*/max_execution_time = 300/" \
        -e "s/;default_charset = \"iso-8859-1\"/default_charset = \"UTF-8\"/" \
        -e "s/;realpath_cache_size = .*/realpath_cache_size = 16384K/" \
        -e "s/;realpath_cache_ttl = .*/realpath_cache_ttl = 7200/" \
        -e "s/post_max_size = .*/post_max_size =  64M/" \
        -e "s/upload_max_filesize = .*/upload_max_filesize = 64M/" \
        -e "s/;intl.default_locale =/intl.default_locale = en/" \
        -e "s/serialize_precision = .*/serialize_precision = 100/" \
        -e "s/expose_phpexpose_php = On/expose_php = Off/" \
        -e "s/;error_log = syslog/error_log = \/www\/logs\/php.log/" \
        -e "s/;opcache.enable=.*/opcache.enable=1/" \
        -e "s/;opcache.enable_cli=.*/opcache.enable_cli=1/" \
        -e "s/;opcache.memory_consumption=.*/opcache.memory_consumption=512/" \
        -e "s/;opcache.interned_strings_buffer=.*/opcache.interned_strings_buffer=8/" \
        -e "s/;opcache.max_accelerated_files=.*/opcache.max_accelerated_files=8192/" \
        -e "s/;opcache.revalidate_path=.*/opcache.revalidate_path=1/" \
        -e "s/;opcache.fast_shutdown=.*/opcache.fast_shutdown=1/" \
        -e "s/;opcache.enable_file_override=.*/opcache.enable_file_override=1/" \
        -e "s/;opcache.validate_timestamps=.*/;opcache.validate_timestamps=1/" \
        -e "s/;opcache.revalidate_freq=.*/opcache.revalidate_freq=0/" \
        /etc/php7/php.ini && \
      apk del \
          curl xz sed && \
      rm -rf /tmp/src && \
      rm -rf /var/cache/apk/*

ADD ./files/start.sh /start.sh
ADD ./files/nginx.conf /etc/nginx/nginx.conf
ADD ./files/php-fpm.conf /etc/php7/php-fpm.conf

RUN chmod u+x /start.sh

EXPOSE 80
VOLUME ["/data"]

CMD ["/start.sh"]
