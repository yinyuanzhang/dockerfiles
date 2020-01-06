FROM php:7.0.14-cli
MAINTAINER Pedro Mata-Mouros

# Update apt repos for Nodejs and Yarn
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list

# Dependencies:
# . git        => Composer
# . ruby-dev   => Sass
# . rubygems   => Sass
# . zlib1g-dev => PHP zip library
RUN apt-get update && \
    apt-get install -y \
        build-essential \
        emacs24-nox \
        git \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        # libmcrypt-dev \
        libpng12-dev \
        man \
        mysql-client \
        nodejs \
        ruby-dev \
        rubygems \
        vim \
        yarn \
        zlib1g-dev \

# Dependencies:
# . bcmath     => AMQP libs
# . sockets    => Monolog
# . zip        => ?
#    && docker-php-ext-install -j$(nproc) iconv mbstring mcrypt pdo_mysql zip \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd \
#    && docker-php-ext-install exif
    && docker-php-ext-install -j$(nproc) zip pdo_mysql sockets bcmath

# Install Composer and make it available in the PATH
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin/ --filename=composer

# Install frontend tools
RUN gem install sass
RUN yarn global add @angular/cli@^6.0.7
RUN yarn global add cpx
RUN yarn global add grunt
RUN yarn global add grunt-cli    # For the legacy app
RUN yarn global add replace
RUN yarn global add uglifycss@0.0.21
RUN yarn global add uglifyjs@^2.4.10

COPY ./php.ini /usr/local/etc/php/

COPY ./init /home/www-data/init
RUN chmod 775 /home/www-data/init
RUN chown -R www-data:www-data /home/www-data

# Make sure the www-data user has the same UID as the user sharing the volume on the host
# TODO: This needs to be replaced with a var somehow (no way of doing this inside Dockerfile,
# so something needs to "compile" this)
RUN usermod -u 1000 www-data -s /bin/bash

# Doing "USER www-data" inccurs in permission problems when we do "npm install"
# Check https://github.com/docker/docker/issues/4614
RUN /bin/su www-data

CMD tail -F /var/log/error.log
