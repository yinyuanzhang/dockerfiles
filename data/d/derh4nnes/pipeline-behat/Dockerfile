FROM debian:stretch
ARG PHPVERSION=7.3
MAINTAINER Sascha Hannes

RUN apt-get update && apt-get install -y \
    software-properties-common \
    git \
    curl \
    wget \
    unzip \
    gnupg \
    screen \
    mysql-client \
    apt-transport-https \
    lsb-release \
    ca-certificates \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/*

RUN wget -q https://packages.sury.org/php/apt.gpg -O- | apt-key add -
RUN echo "deb https://packages.sury.org/php/ stretch main" | tee /etc/apt/sources.list.d/php.list
RUN apt-get update && apt-get install -y \
    "php$PHPVERSION" \
    "php$PHPVERSION-common" \
    "php$PHPVERSION-cli" \
    "php$PHPVERSION-xml" \
    "php$PHPVERSION-gd" \
    "php$PHPVERSION-dom" \
    "php$PHPVERSION-json" \
    "php$PHPVERSION-pdo" \
    "php$PHPVERSION-mysql" \
    "php$PHPVERSION-curl" \
    "php$PHPVERSION-mbstring" \
    sqlite3 \
    "php$PHPVERSION-sqlite" \
    openssl \
    libxi6 \
    libgconf-2-4 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/*

COPY php_more_upload.ini "/etc/php/$PHPVERSION/cli/php_more_upload.ini"

# Install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Install presitissimo
RUN composer global require hirak/prestissimo \
    && composer clear-cache

# Install PHPUnit
RUN composer global require phpunit/phpunit:^6 mikey179/vfsstream:~1.2 \
    && composer clear-cache

# Install Behat
RUN composer global require drupal/drupal-extension:^3.2 behat/mink:~1.7 behat/mink-goutte-driver:~1.2 behat/behat:^3.0 \
    && composer clear-cache

# Install PHPStan
RUN composer global require phpstan/phpstan \
    && composer clear-cache

RUN mkdir project
RUN mkdir project/docroot
