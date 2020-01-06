
FROM debian:jessie

ENV DEBIAN_FRONTEND noninteractive

# Install base deps:
RUN apt-get update && apt-get install -y --no-install-recommends --force-yes curl supervisor git mysql-client && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install dotdeb repo:
#RUN curl http://www.dotdeb.org/dotdeb.gpg | apt-key add -
#ADD dotdeb-php55.list /etc/apt/sources.list.d/dotdeb-php55.list

# Install php deps:
RUN apt-get update && apt-get install -y --no-install-recommends --force-yes apache2 php5 php5-curl php5-mysqlnd php5-gd && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN a2dissite 000-default && a2enmod rewrite && a2enmod php5

# Install CLI tools:
RUN curl -sSk https://getcomposer.org/installer | php && mv composer.phar /usr/bin/composer
RUN composer require symfony/var-dumper
RUN mkdir /usr/share/drush && cd /usr/share/drush && composer require drush/drush:dev-master && ln -s /usr/share/drush/vendor/bin/drush /usr/bin/drush

# Configure:
RUN sed -i "/date\.timezone =/c\date.timezone = Europe\/Paris" /etc/php5/cli/php.ini /etc/php5/apache2/php.ini
ADD apache-vhost.conf /etc/apache2/sites-enabled/000-default.conf
ADD supervisor.conf /etc/supervisor/conf.d/supervisor.conf
RUN echo "opcache.memory_consumption = 128" >> /etc/php5/mods-available/opcache.ini

WORKDIR /srv
EXPOSE 80

CMD ["/usr/bin/supervisord"]
