FROM ubuntu:16.04

EXPOSE 80

ENV LANG=C.UTF-8 \
  SMTP_HOST=mailhog \
  SMTP_PORT=25 \
  SMTP_AUTH=off \
  SMTP_USER= \
  SMTP_PASS= \
  SMTP_FROM=noreply@example.com

RUN echo Europe/Paris | tee /etc/timezone \
 && apt-get update \
 && apt-get install -y software-properties-common python-software-properties curl \
 && add-apt-repository -y ppa:ondrej/php \
 && apt-get update \
 && curl -sL https://deb.nodesource.com/setup_9.x | bash - \
 && apt-get install -y --no-install-recommends --allow-unauthenticated apache2 php7.2 libapache2-mod-php7.2 php-memcached \
      php7.2-mbstring php7.2-xml php7.2-mysql php7.2-opcache php7.2-json \
      php7.2-gd php7.2-curl php7.2-ldap php7.2-mysql php7.2-odbc php7.2-soap php7.2-xsl \
      php7.2-zip php7.2-intl php7.2-cli php7.2-xdebug \
      nodejs rsync \
      build-essential \
      unzip git-core ssh curl mysql-client nano vim less \
      msmtp msmtp-mta telnet \
 && rm -Rf /var/cache/apt/* \
 && systemctl disable apache2 \
 && a2enmod rewrite expires \
 && php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \
 && php composer-setup.php \
 && php -r "unlink('composer-setup.php');" \
 && mv composer.phar /usr/local/bin/composer \
 && echo 'export PATH="$PATH:/var/www/vendor/bin"' >> ~/.bashrc \
 && npm install -g grunt-cli \
 && sed -i 's/\/var\/www\/html/\/var\/www\/web/g' /etc/apache2/sites-enabled/000-default.conf \
 && composer global require drush/drush:8.* \
 && ln -s /root/.composer/vendor/bin/drush /usr/bin/drush \
 && phpdismod xdebug \
 && drush dl drush_language-7.x \
 && mkdir -p /var/www/private \
 && chmod -Rf 777 /var/www/private

COPY config/php.ini /etc/php/7.2/apache2/php.ini
COPY config/apache2.conf /etc/apache2/apache2.conf
COPY config/mpm_prefork.conf /etc/apache2/mods-enabled/mpm_prefork.conf
COPY config/scripts /var/scripts

LABEL cron="drush cron" \
      update="sh /var/scripts/update.sh" \
      securityupdates="sh /var/scripts/securityupdates.sh" \
      restore="sh /var/scripts/restore.sh" \
      backup="sh /var/scripts/backup.sh" \
      test="sh /var/scripts/test.sh"

WORKDIR /var/www/web

CMD ["/var/scripts/startup.sh"]
