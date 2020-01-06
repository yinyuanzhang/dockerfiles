FROM php:7.2-apache-stretch
MAINTAINER Sascha Hannes

# Install git
RUN apt-get update && apt-get install -y git zsh

# Install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

RUN composer global require phpunit/phpunit:^6 mikey179/vfsStream:~1.2 drupal/drupal-extension:^3.2 behat/mink:~1.7 behat/mink-goutte-driver:~1.2 behat/behat:^3.0 phpstan/phpstan hirak/prestissimo

RUN mkdir project
RUN mkdir project/docroot


ENTRYPOINT ["docker-php-entrypoint"]
WORKDIR /var/www/html

EXPOSE 80
CMD ["apache2-foreground"]