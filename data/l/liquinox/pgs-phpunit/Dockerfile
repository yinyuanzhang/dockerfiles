FROM phpunit/phpunit:5.0.3
MAINTAINER Daniel McCoy <danielmccoy@gmail.com>

RUN apt-get update && apt-get install -y libpq-dev && docker-php-ext-install pdo pdo_pgsql
