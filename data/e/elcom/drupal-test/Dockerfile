FROM drupal:8
MAINTAINER LWB

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes --no-install-recommends \
    git mysql-client sendmail vim libldap2-dev && \
    rm -rf /var/lib/apt/lists

RUN docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ && \
    docker-php-ext-install ldap
RUN echo 'sendmail_path=sendmail -t -i' >> /usr/local/etc/php/php.ini
RUN echo 'memory_limit = -1' >> /usr/local/etc/php/php.ini

COPY composer.json /var/www/
COPY ScriptHandler.php /var/www/scripts/composer/

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer && \
    cd /var/www && \
    composer install --no-interaction --no-progress --optimize-autoloader --prefer-dist && \
    phpcs --config-set installed_paths /var/www/vendor/drupal/coder/coder_sniffer

RUN mkdir -p /opt/drush && \
    cd /opt/drush && \
    composer init --require=drush/drush:8.* -n && \
    composer config bin-dir /usr/local/bin && \
    composer install
