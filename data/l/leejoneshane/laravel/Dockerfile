FROM alpine:3.7

ENV FETCH no
ENV INIT no
ENV DOMAIN server.tld
ENV MAIL admin@admin.com
ENV WEB_PASSWORD password
ENV TZ Asia/Taipei
ENV APP_KEY base64:fx/bpfXs+pQ3j7eeZP5gkqWxBtbhUpaqELdpQeeP/N8=
ENV DB_HOST db
ENV DB_PORT 3306
ENV DB_DATABASE laravel
ENV DB_USERNAME root
ENV DB_PASSWORD password
ENV REDIS_HOST redis
ENV REDIS_PORT 6379
ENV REDIS_PASSWORD null
ENV CACHE_DRIVER redis
ENV SESSION_DRIVER redis
ADD docker-entrypoint.sh /usr/local/bin/
ADD gencerts.sh /usr/local/bin/
WORKDIR /var/www/localhost/htdocs

RUN chmod 755 /usr/local/bin/*.sh \
    && apk update \
    && apk add --no-cache bash sudo git zip mc curl certbot acme-client openssl ca-certificates findutils openldap-clients \
                          mysql-client nodejs apache2 apache2-ssl python php7-apache2 php7-ldap php7-xmlwriter php7-opcache \
                          php7-curl php7-openssl php7-json php7-phar php7-dom php7-mysqlnd php7-pdo_mysql php7-iconv \
                          php7-mcrypt php7-ctype php7-xml php7-mbstring php7-tokenizer php7-session php7-fileinfo php7-zlib \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone \
    && mkdir /run/apache2 \
    && sed -ri \
           -e 's!^DocumentRoot "/var/www/localhost/htdocs"$!DocumentRoot "/var/www/localhost/htdocs/public"!g' \
           -e 's!^<Directory "/var/www/localhost/htdocs">$!<Directory "/var/www/localhost/htdocs/public">!g' \
           -e 's!^#(LoadModule rewrite_module .*)$!\1!g' \
           -e 's!^(\s*AllowOverride) None.*$!\1 All!g' \
           -e 's!^(\s*CustomLog)\s+\S+!\1 /proc/self/fd/1!g' \
           -e 's!^(\s*ErrorLog)\s+\S+!\1 /proc/self/fd/2!g' \
           "/etc/apache2/httpd.conf" \
       \
    && sed -ri \
           -e 's!^DocumentRoot "/var/www/localhost/htdocs"$!DocumentRoot "/var/www/localhost/htdocs/public"!g' \
           -e 's!^ServerName .*$!ServerName localhost!g' \
           "/etc/apache2/conf.d/ssl.conf" \
       \
    && sed -ri \
           -e 's!^(max_execution_time = )(.*)$!\1 72000!g' \
           -e 's!^(post_max_size = )(.*)$!\1 1024M!g' \
           -e 's!^(upload_max_filesize = )(.*)$!\1 1024M!g' \
           -e 's!^(memory_limit = )(.*)$!\1 2048M!g' \
           -e 's!^;(opcache.enable=)(.*)!\1 1!g' \
           -e 's!^;(opcache.memory_consumption=)(.*)!\1 1280!g' \
           -e 's!^;(opcache.max_accelerated_files=)(.*)!\1 65407!g' \
           -e 's!^;(opcache.validate_timestamps=)(.*)!\1 0!g' \
           -e 's!^;(opcache.save_comments=)(.*)!\1 1!g' \
           -e 's!^;(opcache.fast_shutdown=)(.*)!\1 0!g' \
           "/etc/php7/php.ini" \
       \
    && rm -f index.html \
    && curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin --filename=composer \
    && /usr/bin/composer create-project --no-progress --prefer-dist laravel/laravel /var/www/localhost/htdocs \
    && composer require predis/predis \
                        laravel/socialite \
                        laravel/passport \
                        guzzlehttp/guzzle \
                        appstract/laravel-opcache \
                        tcg/voyager \
    && chown -R apache:apache /var/www \
    && sed -ri \
           -e '/^DB_HOST=/d' \
           -e '/^DB_PORT=/d' \
           -e '/^DB_DATABASE=/d' \
           -e '/^DB_USERNAME=/d' \
           -e '/^DB_PASSWORD=/d' \
           -e '/^REDIS_HOST=/d' \
           -e '/^REDIS_PORT=/d' \
           -e '/^REDIS_PASSWORD=/d' \
           -e '/^CACHE_DRIVER=/d' \
           -e '/^SESSION_DRIVER=/d' \
           /var/www/localhost/htdocs/.env \
    && cp -Rp /var/www/localhost/htdocs /root

VOLUME /var/www/localhost/htdocs
EXPOSE 80 443 
CMD ["docker-entrypoint.sh"]
