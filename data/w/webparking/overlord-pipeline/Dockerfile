FROM ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -yq --no-install-recommends \
    apt-utils \
    build-essential \
    curl \
    # Install git
    git \
    # Install php
    php7.2-bcmath \
    php7.2-cli \
    php7.2-curl \
    php7.2-dom \
    php7.2-gd \
    php7.2-imagick \
    php7.2-json \
    php7.2-mbstring \
    php7.2-mysql \
    php7.2-soap \
    php7.2-zip \
    # Install tools
    ca-certificates \
    locales \
    mariadb-client \
    openssl \
    unzip \
    # Install libraries
    # libpng-dev for pngquant, for use in build tools
    libpng-dev \
    # libxext6 for PDF rendering
    libxext6 \
    # libxrender1 for PDF rendering
    libxrender1 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Locales
RUN printf 'nl_NL.UTF-8 UTF-8\n' >> /etc/locale.gen && \
    printf 'nl_BE.UTF-8 UTF-8\n' >> /etc/locale.gen && \
    printf 'fr_BE.UTF-8 UTF-8\n' >> /etc/locale.gen && \
    locale-gen

# Composer
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer
RUN composer global require "hirak/prestissimo:^0.3" --prefer-dist --no-progress --no-suggest --classmap-authoritative

# nodejs
COPY --from=node:latest /usr/local/bin/node /usr/local/bin/node
RUN ln -s /usr/local/bin/node /usr/local/bin/nodejs

# yarn
COPY --from=node:latest /opt/yarn-v* /opt/yarn
RUN ln -s /opt/yarn/bin/yarn /usr/local/bin/yarn

# npm
COPY --from=node:latest /usr/local/lib/node_modules /usr/local/lib/node_modules
RUN ln -s /usr/local/lib/node_modules /usr/local/bin/node_modules
RUN ln -s /usr/local/lib/node_modules/npm/bin/npm /usr/local/bin/npm
