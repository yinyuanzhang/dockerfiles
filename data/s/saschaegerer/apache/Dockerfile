FROM saschaegerer/ubuntu:18.04
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install --no-install-recommends -y apache2 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    a2enmod rewrite expires headers mime

ENV APACHE_CONFDIR /etc/apache2
ENV APACHE_ENVVARS $APACHE_CONFDIR/envvars
ENV APACHE_CONF_WEBMASTER webmaster@localhost
RUN set -ex && \
    touch "$APACHE_ENVVARS" && \
    # convert lines like
    #   export APACHE_RUN_USER=www-data
    # into
    #   : ${APACHE_RUN_USER:=www-data}
    #   export APACHE_RUN_USER
    # so that they can be overridden at runtime ("-e APACHE_RUN_USER=...")
    sed -ri 's/^export ([^=]+)=(.*)$/: ${\1:=\2}\nexport \1/' "$APACHE_ENVVARS" && \
    \
    # setup directories and permissions
    . "$APACHE_ENVVARS" && \
    for dir in \
        "$APACHE_LOCK_DIR" \
        "$APACHE_RUN_DIR" \
        "$APACHE_LOG_DIR" \
        /var/www/html \
    ; do \
        rm -rvf "$dir" && \
        mkdir -p "$dir" && \
        chown -R "$APACHE_RUN_USER:$APACHE_RUN_GROUP" "$dir"; \
    done

# Apache + PHP requires preforking Apache for best results
RUN a2dismod mpm_event && a2enmod mpm_prefork proxy_fcgi

# logs should go to stdout / stderr
RUN set -ex && \
    . "$APACHE_ENVVARS" && \
    ln -sfT /dev/stderr "$APACHE_LOG_DIR/error.log" && \
    ln -sfT /dev/stdout "$APACHE_LOG_DIR/access.log" && \
    ln -sfT /dev/stdout "$APACHE_LOG_DIR/other_vhosts_access.log"

# PHP files should be handled by PHP, and should be preferred over any other file type
RUN { \
        echo '<FilesMatch \.php$>'; \
        echo '\tSetHandler application/x-httpd-php'; \
        echo '</FilesMatch>'; \
        echo; \
        echo 'DirectoryIndex disabled'; \
        echo 'DirectoryIndex index.php index.html'; \
        echo; \
        echo '<Directory /var/www/>'; \
        echo '\tOptions -Indexes'; \
        echo '\tAllowOverride All'; \
        echo '</Directory>'; \
    } | tee "$APACHE_CONFDIR/conf-available/custom-php.conf" && \
    a2enconf custom-php && \
    mkdir /var/www/public && \
    chown -R www-data:www-data /var/www

COPY apache2-foreground apache2-entrypoint /usr/local/bin/
COPY apache2-default.conf $APACHE_CONFDIR/sites-available/000-default.conf
COPY conf-vhost $APACHE_CONFDIR/conf-vhost

WORKDIR /var/www/

EXPOSE 80

ENTRYPOINT ["tini", "apache2-entrypoint", "--"]

CMD ["apache2-foreground"]
