FROM debian:stretch-slim

RUN apt-get update \
    && apt-get install curl wget zip tar ruby python python-pip apt-transport-https lsb-release ca-certificates -y

# Node
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash \
    && apt-get update && apt-get install nodejs -y

# PHP
RUN wget -O /etc/apt/trusted.gpg.d/php.gpg https://packages.sury.org/php/apt.gpg \
    && echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" | tee /etc/apt/sources.list.d/php.list \
    && apt-get update && apt-get install php7.2 -y

# Yarn
RUN curl -o- -L https://yarnpkg.com/install.sh | bash

# Composer
COPY ./composer.sh /tmp/composer.sh
RUN cd tmp && sh ./composer.sh && mv composer.phar /usr/local/bin/composer