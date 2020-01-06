

FROM php:7.4-cli

RUN apt-get update && docker-php-ext-install bcmath

COPY . /Worker
WORKDIR /Worker
CMD [ "php", "./worker.php" ]
