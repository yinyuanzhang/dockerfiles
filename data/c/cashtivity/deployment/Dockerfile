FROM ubuntu:xenial

RUN apt-get update -y \
    && apt-get install -y software-properties-common \
    && LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php
RUN apt-get update -y \
    && apt-get install -y --no-install-recommends \
    unzip \
    zip \
    git-core \
    curl \
    python-dev \
    graphicsmagick \
    build-essential \
    ca-certificates \
    php7.2-cli \
    php7.2-curl \
    php7.2-gd \
    php7.2-mbstring \
    php7.2-mysql \
    php7.2-sqlite \
    php7.2-xml \
    php7.2-zip \
    php-xdebug \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

## install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

## install nvm, node, npm, gulp
ENV NVM_DIR=/root/.nvm
ENV NODE_VERSION=7.5.0
RUN curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.8/install.sh | bash \
    && . $NVM_DIR/nvm.sh \
    && nvm install $NODE_VERSION \
    && nvm alias default $NODE_VERSION \
    && nvm use default
ENV NODE_PATH $NVM_DIR/versions/node/v$NODE_VERSION/lib/node_modules
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH
RUN npm install -g gulp-cli

