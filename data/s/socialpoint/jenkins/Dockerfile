FROM socialpoint/jenkins:base

LABEL maintainer "Backend Team <backend@socialpoint.es>"

RUN DEBIAN_FRONTEND=noninteractive apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    apt-transport-https \
    lsb-release \
    ca-certificates \
    && wget -O /etc/apt/trusted.gpg.d/php.gpg https://packages.sury.org/php/apt.gpg \
    && echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" > /etc/apt/sources.list.d/php.list \
    && rm -rf /var/lib/apt/lists/*

RUN DEBIAN_FRONTEND=noninteractive apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y --no-install-recommends install \
    php7.1-fpm \
    php7.1-bcmath \
    php7.1-bz2 \
    php7.1-gd \
    php7.1-dev \
    php7.1-curl \
    php7.1-mbstring \
    php-pear \
    php7.1-xml \
  && update-alternatives --set php /usr/bin/php7.1 \
    && update-alternatives --set phar /usr/bin/phar7.1 \
    && update-alternatives --set phar.phar /usr/bin/phar.phar7.1 \
    && update-alternatives --set phpize /usr/bin/phpize7.1 \
    && update-alternatives --set php-config /usr/bin/php-config7.1 \
  && pecl install \
    igbinary \
    apcu \
    apcu_bc-beta \
    opcache \
    redis \
  && rm -rf /var/lib/apt/lists/*

RUN printf "extension=igbinary.so\n\
extension=apcu.so\n\
extension=apc.so \n\
extension=redis.so \n\
memory_limit = -1\n\
apc.enable_cli = 1\n\
opcache.enable_cli = 1" > /etc/php/7.1/cli/conf.d/10-pear.ini 

# Composer
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer