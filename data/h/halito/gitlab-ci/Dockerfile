FROM php:7.0.14-cli
MAINTAINER halito! <devs@halito.com>

#
# Update Instance
RUN apt-get update -y

#
# Install (un)Zip and GIT
RUN apt-get install -y \
    zip \
    unzip \
    git
    
#
# Install Python
RUN apt-get install -y \
    python \
    python-pip
    
# Install AWSCLI through Python
RUN pip install awscli

#
# Download PHP extension dependencies
RUN apt-get install -y \
    libcurl3-dev \
    libxml2-dev \
    libzzip-dev \
    libfreetype6-dev \
    libjpeg62-turbo-dev \
    libmcrypt-dev \
    libicu-dev \
    libedit-dev \
    && rm -rf /var/lib/apt/lists/*

#
# Install PHP extensions
RUN docker-php-ext-install pdo \
    && docker-php-ext-install pdo_mysql \
    && docker-php-ext-install mysqli \
    && docker-php-ext-install curl \
    && docker-php-ext-install xml \
    && docker-php-ext-install calendar \
    && docker-php-ext-install zip \
    && docker-php-ext-install gd \
    && docker-php-ext-install bcmath \
    && docker-php-ext-install mbstring \
    && docker-php-ext-install mcrypt \
    && docker-php-ext-install intl \
    && docker-php-ext-install readline

#
# Configure PHP extensions (based on extensions)
RUN docker-php-ext-configure gd \
    --with-freetype-dir=/usr/include/ \
    --with-jpeg-dir=/usr/include/

RUN docker-php-ext-configure calendar \
    --enable-calendar

RUN docker-php-ext-configure readline \
    --with-readline

#
# Manually enable PHP extension
RUN docker-php-ext-enable readline

#
# Install Composer
RUN curl -s http://getcomposer.org/installer | php \
    && mv composer.phar /usr/local/bin/composer
    
#    
# Install node.js 8.x
RUN apt-get update -yq \
  && apt-get install curl gnupg -yq \
  && curl -sL https://deb.nodesource.com/setup_8.x | bash \
  && apt-get install nodejs -yq
  
#
# Check node.js install
RUN node -v \
  && npm -v \
  && npm i -g nodemon \
  && nodemon -v

#
# Install yarn
RUN curl -o- -L https://yarnpkg.com/install.sh | bash -s -- --version 1.9.4 \
    && export PATH=$HOME/.yarn/bin:$PATH

ENV PATH "/root/.yarn/bin:$PATH"