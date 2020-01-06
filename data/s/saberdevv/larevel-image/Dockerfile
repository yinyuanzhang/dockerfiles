FROM php:7.1.3-cli

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update -qq

RUN apt install -y -q \
  git \
  zip \
  unzip \
  zlib1g-dev \
  build-essential \
  autoconf \
  libz-dev

RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
RUN php -r "if (hash_file('sha384', 'composer-setup.php') === 'a5c698ffe4b8e849a443b120cd5ba38043260d5c4023dbf93e1558871f1f07f58274fc6f4c93bcfd858c6bd0775cd8d1') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"
RUN php composer-setup.php --install-dir=bin --filename=composer
RUN php -r "unlink('composer-setup.php');"

RUN docker-php-ext-install -j$(nproc) \
  bcmath \
  zip

RUN pecl install grpc

RUN docker-php-ext-enable grpc

EXPOSE 8000