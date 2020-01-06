FROM php:7.0-apache

RUN apt-get update && apt-get install -fy \
        curl \
        git \
        gnupg \
        libicu-dev \
 && curl -sL https://deb.nodesource.com/setup_8.x | bash - \
 && apt-get -fy install \
        nodejs \
    && rm -rf /var/lib/apt/lists/* \
    && docker-php-ext-install pdo_mysql intl

RUN curl -o /usr/local/bin/composer https://getcomposer.org/composer.phar && chmod +x /usr/local/bin/composer

RUN a2enmod rewrite

COPY vhost.conf /etc/apache2/sites-enabled/000-default.conf

COPY entrypoint.sh /usr/local/bin/entrypoint.sh

WORKDIR /var/www/html

RUN git clone https://github.com/1001Pharmacies/qandidate-toggle-ui.git .

RUN npm install
RUN npm install -g bower

RUN chown -R www-data:www-data /var/www/

USER www-data

ADD .env.dist .
RUN cp .env.dist .env \
  && bower install

RUN mv app web

USER root

ENV TOGGLE__API_BASE_URL="http://127.0.0.1:8080"

COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
CMD ["apache2-foreground"]
