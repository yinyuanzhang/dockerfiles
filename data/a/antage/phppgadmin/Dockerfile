FROM debian:buster

ENV DEBIAN_FRONTEND=noninteractive
RUN \
    apt-get -y -q update \
    && apt-get -y -q --no-install-recommends install \
        curl \
        ca-certificates \
        apache2 \
        php \
        gosu \
	postgresql-client \
        phppgadmin \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && rm /var/log/dpkg.log \
    && rm /var/www/html/index.html \
    && rmdir /var/www/html \
    && curl -#L https://github.com/kelseyhightower/confd/releases/download/v0.16.0/confd-0.16.0-linux-amd64 -o /usr/local/bin/confd \
    && chmod 755 /usr/local/bin/confd \
    && mkdir -p /etc/confd/conf.d \
    && mkdir -p /etc/confd/templates \
    && touch /etc/confd/confd.toml \
    && rm /etc/php/7.3/apache2/conf.d/* \
    && rm /etc/php/7.3/cli/conf.d/* \
    && phpenmod -s ALL opcache pgsql \
    && rm /etc/apache2/conf-enabled/* \
    && rm /etc/apache2/mods-enabled/* \
    && a2enmod mpm_prefork rewrite php7.3 env dir auth_basic authn_file authz_user authz_host access_compat \
    && rm /etc/apache2/sites-enabled/000-default.conf

EXPOSE 8080

ENV LANG=C
ENV APACHE_LOCK_DIR         /var/lock/apache2
ENV APACHE_RUN_DIR          /var/run/apache2
ENV APACHE_PID_FILE         ${APACHE_RUN_DIR}/apache2.pid
ENV APACHE_LOG_DIR          /var/log/apache2
ENV APACHE_RUN_USER         www-data
ENV APACHE_RUN_GROUP        www-data
ENV APACHE_DOCUMENT_ROOT    /usr/share/phppgadmin
ENV APACHE_ALLOW_OVERRIDE   None
ENV APACHE_ALLOW_ENCODED_SLASHES Off
ENV PHP_TIMEZONE            UTC

COPY confd/php.apache2.toml /etc/confd/conf.d/
COPY confd/templates/php.apache2.ini.tmpl /etc/confd/templates/
COPY confd/php.cli.toml /etc/confd/conf.d/
COPY confd/templates/php.cli.ini.tmpl /etc/confd/templates/
COPY confd/apache2.toml /etc/confd/conf.d/
COPY confd/templates/apache2.conf.tmpl /etc/confd/templates/
RUN /usr/local/bin/confd -onetime -backend env
COPY confd/phppgadmin.config.inc.php.toml /etc/confd/conf.d/
COPY confd/templates/phppgadmin.config.inc.php.tmpl /etc/confd/templates/

COPY ports.conf /etc/apache2/ports.conf
COPY apache2-mods/mpm_prefork.conf /etc/apache2/mods-available/mpm_prefork.conf

COPY apache2-mods/php7.3.conf /etc/apache2/mods-available/php7.3.conf

COPY apache2-mods/remoteip.conf /etc/apache2/mods-available/remoteip.conf
RUN a2enmod remoteip

COPY phppgadmin.conf /etc/apache2/conf-available/phppgadmin.conf
RUN a2enconf phppgadmin

COPY docker-entrypoint.sh /

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["apache2"]
