FROM php:7.2-fpm-buster

RUN apt-get update \
  && apt-get install -y gnupg

RUN curl -s https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - \
  && echo "deb http://apt.postgresql.org/pub/repos/apt/ stretch-pgdg main" > /etc/apt/sources.list.d/pgdg.list

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash - \
  && apt-get install -y nodejs

RUN apt-get update \
  && apt-get install -y postgresql-client-9.6 libjpeg62-turbo-dev libpng-dev  \
  libbz2-dev libfreetype6-dev libpq-dev libicu-dev unzip git wget cron gdal-bin libgeos-dev \
  libmagickwand-dev

RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include --with-jpeg-dir=/usr/include \
  && docker-php-ext-install -j$(nproc) \
  gd \
  pdo_pgsql \
  zip \
  bcmath \
  bz2 \
  gettext \
  intl \
  sockets \
  && pecl install apcu \
  && docker-php-ext-enable apcu \
  && pecl install imagick \
  && docker-php-ext-enable imagick \
  && pecl install redis-4.0.2 \
  && docker-php-ext-enable redis

WORKDIR /opt

RUN git clone https://git.osgeo.org/gitea/geos/php-geos.git

WORKDIR /opt/php-geos
RUN ./autogen.sh \ 
  && phpize \
  && ./configure \
  && make -j "$(nproc)" \
  && make install \ 
  && docker-php-ext-enable geos


RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \
  && php -r "copy('https://composer.github.io/installer.sig', 'composer-setup.sig');" \
  && php -r "if (hash_file('SHA384', 'composer-setup.php') === trim(file_get_contents('composer-setup.sig'))) { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;" \
  && php composer-setup.php \
  && php -r "unlink('composer-setup.php');" \
  && mv composer.phar /usr/local/bin/composer
