FROM phpdockerio/php74-fpm:latest

USER root

# Fix debconf warnings upon build
ARG DEBIAN_FRONTEND=noninteractive

# Setup
RUN  apt-get update \
    && apt-get install  -y \
    apt-transport-https \
    ca-certificates \
    curl make \
    gnupg-agent \
    software-properties-common \
    && apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*

# Node Repo
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash -

# Yarn Repo
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
    && echo "deb https://dl.yarnpkg.com/debian/ rc main" | tee /etc/apt/sources.list.d/yarn.list

# Docker Repo
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg |  apt-key add - \
    && add-apt-repository \
    "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) \
    stable"

RUN add-apt-repository universe \
    && add-apt-repository multiverse \
    && add-apt-repository restricted

# Install selected extensions and other stuff - blackfire-php
RUN apt-get update \
    && apt-get -y --no-install-recommends install \
        php-pear php7.4-dev php-memcached php7.4-mysql php7.4-pgsql php7.4-opcache \
        php7.4-pdo php7.4-sqlite php-redis php-xdebug php7.4-bcmath php7.4-bz2 \
        php7.4-gd php7.4-gmp php-imagick php7.4-imap php7.4-redis \
        php7.4-intl php7.4-pspell php7.4-soap php-ssh2 php-yaml \
    && apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*

# Install Yarn / Node
RUN apt-get update \
    && apt-get -y install nodejs yarn \
    && apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*
    
# Install PNPM
RUN curl -L https://unpkg.com/@pnpm/self-installer | node

# Install git
RUN apt-get update \
    && apt-get -y install git \
    && apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*

# Install others
RUN apt-get update \
    && apt-get -y install vim htop supervisor cron graphviz aspell aspell-de \
    && apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/* 

# Install ZSH - Deactivate dirty file parsing, it slows zsh extremly down
RUN apt-get update \
    && apt-get install -y zsh fonts-powerline fonts-firacode \
    && chsh -s /usr/bin/zsh \
    && apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*\
    && sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)" \
    && git config --global --add oh-my-zsh.hide-dirty 1

# Install Docker
RUN apt-get update \
    && apt-get install  -y docker docker-ce docker-ce-cli containerd.io \
    && apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*

# Install Symfony CLI
RUN curl -sS https://get.symfony.com/cli/installer | bash

# Install Docker-Compose
RUN curl -L https://github.com/docker/compose/releases/download/1.25.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose \
    && chmod +x /usr/local/bin/docker-compose

# Install PHP-Ast
RUN pecl install ast && printf "\nextension=ast.so\n" >> /etc/php/7.4/fpm/php.ini \ 
    && printf "\nextension=ast.so\n" >> /etc/php/7.4/cli/php.ini \
    && export PHAN_ALLOW_XDEBUG=1

# Blackfire
#RUN version=$(php -r "echo PHP_MAJOR_VERSION.PHP_MINOR_VERSION;") \
#    && curl -A "Docker" -o /tmp/blackfire-probe.tar.gz -D - -L -s https://blackfire.io/api/v1/releases/probe/php/linux/amd64/74 \
#    && mkdir -p /tmp/blackfire \
#    && tar zxpf /tmp/blackfire-probe.tar.gz -C /tmp/blackfire \
#    && mv /tmp/blackfire/blackfire-*.so $(php -r "echo ini_get('extension_dir');")/blackfire.so \
#    && printf "extension=blackfire.so\nblackfire.agent_socket=tcp://blackfire:8707\n" > /etc/php/7.4/fpm/conf.d/90-blackfire.ini \
#    && rm -rf /tmp/blackfire /tmp/blackfire-probe.tar.gz

# Cron Start
RUN service cron start

# Globals Composer
RUN composer global require hirak/prestissimo laravel/installer

# Globals Yarn
RUN yarn global add @vue/cli @vue/cli-service-global

# Globals NPM
RUN pnpm add --global @vue/cli @vue/cli-service-global
