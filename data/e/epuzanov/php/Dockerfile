FROM opensuse:leap

MAINTAINER Egor Puzanov

RUN mkdir -p /usr/lib/locale /var/www/html /usr/lib/cgi-bin && \
    zypper --no-gpg-checks --gpg-auto-import-keys addrepo -f https://download.opensuse.org/repositories/server:php:extensions:php7/openSUSE_Leap_42.3/server:php:extensions:php7.repo && \
    zypper --gpg-auto-import-keys --non-interactive ref && \
    zypper -n in apache2 apache2-mod_php7 curl git glibc-i18ndata libldap-data \
        ncat php7 php7-APCu php7-calendar php7-ctype php7-curl php7-exif \
        php7-fileinfo php7-fpm php7-gd php7-iconv php7-intl php7-ldap \
        php7-mbstring php7-memcached php7-mysql php7-opcache php7-pcntl \
        php7-pgsql php7-phar php7-posix php7-readline php7-sockets php7-sqlite \
        php7-sysvmsg php7-sysvsem php7-sysvshm php7-tokenizer php7-wddx \
        php7-xmlreader php7-xmlwriter php7-xsl php7-zlib rsvg-view unixODBC && \
    zypper clean -a && \
    localedef -i en_US -f UTF-8 en_US.UTF-8 && \
    sed -i "s/RC_LANG=\".*\"/RC_LANG=\"en_US.UTF-8\"/g" /etc/sysconfig/language && \
    sed -i "s/APACHE_MODULES=\"/APACHE_MODULES=\"php7 macro rewrite proxy proxy_fcgi /g" /etc/sysconfig/apache2 && \
    sed -i "s/APACHE_SERVER_FLAGS=\"/APACHE_SERVER_FLAGS=\"SSL /g" /etc/sysconfig/apache2 && \
    sed -i "s/\/srv\/www\/htdocs/\/var\/www\/html/g" /etc/apache2/default-server.conf && \
    sed -i "s/\/srv\/www\/cgi-bin/\/usr\/lib\/cgi-bin/g" /etc/apache2/default-server.conf && \
    ln -sfT /dev/stderr /var/log/apache2/error_log && \
    ln -sfT /dev/stdout /var/log/apache2/access_log && \
    ln -s /etc/apache2/vhosts.d /etc/apache2/sites-enabled && \
    mv /etc/php7/fpm/php-fpm.conf.default /etc/php7/fpm/php-fpm.conf && \
    mv /etc/php7/fpm/php-fpm.d/www.conf.default /etc/php7/fpm/php-fpm.d/www.conf && \
    sed -i "s/;error_log = .*/error_log = \/proc\/self\/fd\/2/g" /etc/php7/fpm/php-fpm.conf && \
    sed -i "s/;daemonize = yes/daemonize = no/g" /etc/php7/fpm/php-fpm.conf && \
    sed -i "s/user = .*/user = wwwrun/g" /etc/php7/fpm/php-fpm.d/www.conf && \
    sed -i "s/group = .*/group = www/g" /etc/php7/fpm/php-fpm.d/www.conf && \
    sed -i "s/listen = .*/listen = 80/g" /etc/php7/fpm/php-fpm.d/www.conf && \
    sed -i "s/;clear_env = no/clear_env = no/g" /etc/php7/fpm/php-fpm.d/www.conf && \
    sed -i "s/;access.log = .*/access.log = \/proc\/self\/fd\/2/g" /etc/php7/fpm/php-fpm.d/www.conf && \
    sed -i "s/;catch_workers_output = yes/catch_workers_output = yes/g" /etc/php7/fpm/php-fpm.d/www.conf && \
    echo "TLS_REQCERT never" >> /etc/openldap/ldap.conf

COPY opcache.ini /etc/php7/conf.d/opcache.ini
COPY httpd-foreground /usr/sbin/httpd-foreground
WORKDIR /var/www/html

EXPOSE 80 443

CMD ["httpd-foreground", "-DFOREGROUND"]
