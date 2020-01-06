FROM php

MAINTAINER Zeyu Ye <Shuliyey@gmail.com>

ARG COMPOSER_VERSION=1.6.5
ARG COMPOSER_SHA=544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061
ARG DOCKERIZE_VERSION=v0.6.1

RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \
  && php -r "if (hash_file('SHA384', 'composer-setup.php') === \"${COMPOSER_SHA}\") { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;" \
  && php composer-setup.php --install-dir=/usr/local/bin --filename=composer --version=${COMPOSER_VERSION}

RUN apt-get update \
  && apt-get install -y libmagickwand-dev zlib1g-dev libpng-dev git-core \
  && pecl install imagick \
  && docker-php-ext-enable imagick \
  && docker-php-ext-install gd \
  && docker-php-ext-install zip \
  && curl -L https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz -o dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
  && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
  && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
  && apt-get clean -y \
  && apt-get autoclean -y \
  && apt-get autoremove -y \
  && rm -rf /var/cache/debconf/*-old \
  && rm -rf /var/lib/apt/lists/*

CMD ["bash"]
