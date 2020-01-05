FROM ubuntu:18.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y software-properties-common

RUN apt-get update && add-apt-repository ppa:ondrej/php

RUN apt-get update && apt-get install -y \
 curl \
 build-essential \
 git \
 ruby \
 ruby-dev \
 docker-compose \
 mysql-client \
 php7.3-fpm \
 php7.3-bcmath \
 php7.3-cli \
 php7.3-curl \
 php7.3-gd \
 php7.3-mbstring \
 php7.3-xml \
 php7.3-zip \
 xvfb \
 libgtk-3-dev \
 libnotify-dev \
 libgconf-2-4 \
 libnss3 \
 libxss1 \
 libasound2


RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list

# Install JS stuff
RUN apt-get update && apt-get install -y \
 nodejs \
 npm \
 yarn

# Install composer
RUN curl -sS https://getcomposer.org/installer | php -- --filename=composer --install-dir=/usr/bin
ENV COMPOSER_ALLOW_SUPERUSER=1
RUN composer global require hirak/prestissimo
RUN export PATH="$PATH:$HOME/.composer/vendor/bin"

# Install packages
RUN composer global require squizlabs/php_codesniffer
RUN composer global require drupal/coder
RUN ln -s /root/.composer/vendor/bin/phpcs /usr/bin/phpcs
RUN ln -s /root/.composer/vendor/bin/phpcbf /usr/bin/phpcbf
RUN phpcs --config-set installed_paths /root/.composer/vendor/drupal/coder/coder_sniffer
RUN phpcbf --config-set installed_paths /root/.composer/vendor/drupal/coder/coder_sniffer
RUN composer global require phpmd/phpmd 
RUN ln -s /root/.composer/vendor/bin/phpmd /usr/bin/phpmd   

# Install packages
RUN gem install scss_lint

# Get Lint config
RUN git clone https://bitbucket.org/garethhallnz/scss-lint-config.git
RUN cd scss-lint-config/ && git pull
RUN mv scss-lint-config/.scss-lint.yml ~/

# Install Cypress
RUN yarn add cypress

# Show versions
RUN php -v
RUN node -v
RUN npm -v
RUN yarn -v
RUN ruby -v
RUN scss-lint -v
RUN ./node_modules/.bin/cypress -v