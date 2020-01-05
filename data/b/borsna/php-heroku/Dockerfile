FROM php

RUN apt-get update && apt-get install -y \
      unzip \
      zlib1g-dev \
      git \
    && rm -rf /var/lib/apt/lists/* && \
    docker-php-ext-install zip
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer