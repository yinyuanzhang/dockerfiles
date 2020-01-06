FROM debian:stretch-slim

LABEL net.vudunet.php.version="7.0-0.1.1"
LABEL net.vudunet.php.author="Claude Juif"
LABEL net.vudunet.php.description="Provide php-fpm 7.0 and cli based on Debian stretch"
LABEL maintainer="claude.juif@gmail.com"

# Install PHP 7.0 from official repository
RUN set -ex; \
  apt update -q -y; \
  DEBIAN_FRONTEND=noninteractive apt upgrade -q -y; \
  DEBIAN_FRONTEND=noninteractive apt install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    git \
    xz-utils \
    dirmngr \
    gnupg \
    zip \
    unzip \
    libicu-dev \
    python3-pip \
    acl \
    nano \
    libfcgi0ldbl \
    wget; \
  wget -q -O /etc/apt/trusted.gpg.d/php.gpg https://packages.sury.org/php/apt.gpg; \
  echo "deb https://packages.sury.org/php/ stretch main" > /etc/apt/sources.list.d/php.list; \
  apt update -q -y; \
  DEBIAN_FRONTEND=noninteractive apt install -y \
    php7.0-apcu \
    php7.0-bcmath \
    php7.0-cli \
    php7.0-curl \
    php7.0-fpm \
    php7.0-gd \
    php7.0-intl \
    php7.0-json \
    php7.0-mcrypt \
    php7.0-mysql \
    php7.0-opcache \
    php7.0-readline \
    php7.0-soap \
    php7.0-xml \
    php7.0-zip \
    php7.0-mbstring \
    php7.0-imagick; \
    rm -rf /var/lib/apt/lists/*; \
    ln -s /usr/sbin/php-fpm7.0 /usr/sbin/php-fpm; \
    mkdir /etc/php/template.d; \
    mkdir /composer; \
    chmod -R 777 /composer; \
    pip3 install envtpl

ADD install-composer.sh /install-composer.sh
ADD entrypoint.sh /entrypoint.sh
ADD template.d /etc/php/template.d
ADD www.conf.tpl /www.conf.tpl
ADD ping.sh /ping.sh

# Configuring php-fpm
RUN set -ex; \
  { \
    echo '[global]'; \
    echo 'error_log = /proc/self/fd/2'; \
    echo 'daemonize = no'; \
    echo 'include=/etc/php/7.0/fpm/pool.d/*.conf'; \
  } | tee /etc/php/7.0/fpm/php-fpm.conf; \
  /install-composer.sh

WORKDIR /var/www/app

ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 9000

CMD ["php-fpm"]
