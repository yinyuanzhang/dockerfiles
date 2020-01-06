FROM naonak/docker-apache-php7
MAINTAINER Fabien EVAIN <fevain@rmn.com>

## Laravel
# Based on https://laravel.com/docs/5.3/installation

## Install laravel
RUN composer global require "laravel/installer"

## Finalize

CMD ["apache2-foreground"]