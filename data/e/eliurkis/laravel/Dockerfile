FROM circleci/php:7.3-node-browsers
LABEL maintainer="Eliurkis Diaz <eliurkis@gmail.com>"

RUN sudo apt-get update && sudo apt-get install -y libsqlite3-dev zlib1g-dev libpng-dev \
    && sudo docker-php-ext-install -j$(nproc) zip gd pdo_mysql exif bcmath sockets
