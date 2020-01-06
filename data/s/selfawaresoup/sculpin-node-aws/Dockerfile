FROM php:7-alpine

RUN apk update
RUN apk add --update \
    bash \
    git \
    openssl \
    wget \
    unzip \
    curl-dev \
    libxml2-dev \
    rsync \
    zlib-dev \
    libzip-dev \
    nodejs \
    npm \
    python \
    py-pip \
    openssh-client
RUN pip install --upgrade awscli

RUN docker-php-ext-install zip curl xml
ADD https://getcomposer.org/installer /tmp/composer-installer.php
RUN php /tmp/composer-installer.php --install-dir=/usr/local/bin --filename=composer && \
    rm /tmp/composer-installer.php

RUN composer require sculpin/sculpin
RUN ln -s /vendor/bin/sculpin /usr/local/bin/sculpin


