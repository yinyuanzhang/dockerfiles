FROM ubuntu:16.04

ENV	TERM="xterm" \
    LANG='en_US.UTF-8' \
    LANGUAGE='en_US:en' \
    LC_ALL='en_US.UTF-8'

RUN echo "Europe/Zurich" > /etc/timezone

# update package repositories
RUN apt-get update

# install some packages required for next step
RUN apt-get install -y wget curl software-properties-common tzdata debconf locales apt-utils \
  && LC_ALL=C.UTF-8 add-apt-repository -y ppa:ondrej/php

# generate locales & set timezone
RUN locale-gen en_US.UTF-8 \
  && dpkg-reconfigure -f noninteractive tzdata

# add & update package repositories
RUN add-apt-repository 'deb http://archive.ubuntu.com/ubuntu trusty universe' \
  && apt-get update \
  && apt-get upgrade -y

# install from package list & clear chache
RUN apt-get install -y \
    acl \
    apache2 \
    apache2-utils \
    bash-completion \
    curl \
    git \
    graphviz \
    imagemagick \
    iputils-ping \
    libapache2-mod-php7.2 \
    libmagickwand-dev \
    libsqlite3-dev \
    libyaml-dev \
    mysql-client \
    php7.2-common \
    php7.2-geoip \
    php7.2-gettext \
    php7.2-imagick \
    php-pear \
    php-phpseclib \
    php-tcpdf \
    php7.2-xdebug \
    php7.2 \
    php7.2-cli \
    php7.2-common \
    php7.2-curl \
    php7.2-dev \
    php7.2-gd \
    php7.2-intl \
    php7.2-json \
    php7.2-mbstring \
    php7.2-mysql \
    php7.2-readline \
    php7.2-sqlite3 \
    php7.2-xml \
    php7.2-zip \
    poppler-utils \
    realpath \
    sqlite3 \
    ssl-cert \
    sudo \
    supervisor \
    unzip \
    vim \
    nano \
    wget \
    zip \
  && apt-get clean

# install pecl module
RUN  echo '' | pecl install yaml

# install more recent version of nodejs
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash - \
  && apt-get install nodejs \
  && npm install uglifycss uglify-js -g

# add apache php & xdebug configuration
ADD config/php.ini /etc/php/7.2/cli/php.ini
ADD config/php.ini /etc/php/7.2/apache2/php.ini
ADD config/xdebug.ini /etc/php/7.2/mods-available/xdebug.ini
ADD config/application.apache.conf /etc/apache2/sites-available/000-application.conf
ADD config/application-ssl.apache.conf /etc/apache2/sites-available/000-application-ssl.conf

RUN mkdir /app \
  # enable xdebug
  && phpenmod -s ALL xdebug

  # create ssl-cert, enable mod_ssl, mod_vhost_alias, mod_rewrite
RUN make-ssl-cert generate-default-snakeoil --force-overwrite \
  && chmod -f a+rx /etc/ssl/private/* /etc/ssl/certs/* \
  && a2enmod ssl vhost_alias rewrite

  # enable the right apache vhosts
RUN a2dissite default-ssl.conf \
  && a2dissite 000-default.conf \
  && a2ensite 000-application-ssl.conf \
  && a2ensite 000-application.conf

# install composer globally
RUN EXPECTED_SIGNATURE="$(wget -q -O - https://composer.github.io/installer.sig)" \
  && curl -sS https://getcomposer.org/installer -o composer-setup.php \
  && php -r "if (hash_file('SHA384', 'composer-setup.php') === '$EXPECTED_SIGNATURE') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;" \
  && php composer-setup.php --install-dir=/usr/local/bin --filename=composer

# Docker Entrypoints
COPY /docker-entrypoint.sh /
COPY /docker-entrypoint.d /docker-entrypoint.d/
ENTRYPOINT ["/docker-entrypoint.sh"]

# default-command
CMD ["/bin/bash"]

# initial directory when staring the container
WORKDIR /app

# exposed ports.
EXPOSE 80 443 9000

