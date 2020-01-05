FROM php:7.4-fpm

LABEL maintainer="itsDamien <damien@itsdamien.com>"

WORKDIR /root

RUN echo "rm -rf /var/lib/apt/lists/*" > /usr/bin/apt-clean && chmod +x /usr/bin/apt-clean

RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc make gnupg apt-utils libc6-dev procps \
    && pecl channel-update pecl.php.net \
    && apt-get install -y --no-install-recommends \
    cron \
    htop \
    nano \
    ncdu \
    curl \
    unzip \
    wget \
    git \
    python \
    python-pip \
    && pip install setuptools --no-cache-dir \
    && apt-clean

###########################################################################
# Add french language
###########################################################################

RUN apt-get update \
    && apt-get install -y --no-install-recommends locales \
    && apt-clean \
    && sed -i "s/# fr_FR.UTF-8 UTF-8/fr_FR.UTF-8 UTF-8/g" /etc/locale.gen \
    && /usr/sbin/locale-gen

###########################################################################
# Wkhtmltopdf
###########################################################################

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    fontconfig \
    libxrender1 \
    libxext6 \
    xfonts-75dpi \
    xfonts-base \
    libjpeg-dev \
    && apt-clean \
    && wget -q https://downloads.wkhtmltopdf.org/0.12/0.12.5/wkhtmltox_0.12.5-1.stretch_amd64.deb \
    && dpkg -i wkhtmltox_0.12.5-1.stretch_amd64.deb \
    && rm wkhtmltox_0.12.5-1.stretch_amd64.deb

###########################################################################
# Image Optimizer
###########################################################################

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    libjpeg-dev \ 
    libpng-dev \
    jpegoptim \
    optipng \
    pngquant \
    gifsicle \
    && apt-clean

###########################################################################
# PHP EXTENSION: PDO MySQL
###########################################################################

RUN docker-php-ext-install pdo_mysql

###########################################################################
# PHP EXTENSION: GD
###########################################################################

RUN apt-get update \
    && apt-get install -y --no-install-recommends libfreetype6-dev libjpeg-dev \
    && apt-clean \
    && docker-php-ext-configure gd --with-jpeg --with-freetype \
    && docker-php-ext-install gd

###########################################################################
# PHP EXTENSION: Socket
###########################################################################

RUN docker-php-ext-install sockets

###########################################################################
# PHP EXTENSION: Calendar
###########################################################################

RUN docker-php-ext-install calendar

###########################################################################
# PHP EXTENSION: Zip
###########################################################################

RUN apt-get update \
    && apt-get install -y --no-install-recommends libzip-dev \
    && apt-clean \
    && docker-php-ext-install zip

###########################################################################
# PHP EXTENSION: SOAP
###########################################################################

RUN mv /etc/apt/preferences.d/no-debian-php /tmp/no-debian-php \
    && apt-get update \
    && apt-get install -y --no-install-recommends libxml2-dev php-soap \
    && apt-clean \
    && mv /tmp/no-debian-php /etc/apt/preferences.d/no-debian-php \
    && docker-php-ext-install soap

###########################################################################
# PHP EXTENSION: PCNTL
###########################################################################

RUN docker-php-ext-install pcntl

###########################################################################
# PHP EXTENSION: OPcache
###########################################################################

RUN docker-php-ext-install opcache

ENV PHP_OPCACHE_VALIDATE_TIMESTAMPS="0" \
    PHP_OPCACHE_MAX_ACCELERATED_FILES="16229" \
    PHP_OPCACHE_MEMORY_CONSUMPTION="192" \
    PHP_OPCACHE_INTERNED_STRINGS_BUFFER="64" \
    PHP_OPCACHE_MAX_WASTED_PERCENTAGE="10"

COPY ./opcache.ini /usr/local/etc/php/conf.d/opcache.ini

###########################################################################
# PHP EXTENSION: Xdebug
###########################################################################

#/usr/local/lib/php/extensions/no-debug-non-zts-20190902/xdebug.so
RUN pecl install xdebug

###########################################################################
# PHP EXTENSION: BCMATH
###########################################################################

RUN docker-php-ext-install bcmath

###########################################################################
# PHP EXTENSION: EXIF
###########################################################################

RUN docker-php-ext-install exif

###########################################################################
# PHP EXTENSION: mbstring
###########################################################################

RUN apt-get update \
    && apt-get install -y --no-install-recommends libonig-dev \
    && apt-clean
RUN docker-php-ext-install mbstring

###########################################################################
# PHP Tools
###########################################################################

# Composer
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \
    && php -r "if (hash_file('SHA384', 'composer-setup.php') === trim(file_get_contents('https://composer.github.io/installer.sig'))) { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;" \
    && php composer-setup.php --install-dir=/usr/local/bin --filename=composer \
    && php -r "unlink('composer-setup.php');"
ENV COMPOSER_ALLOW_SUPERUSER 1
RUN composer global require hirak/prestissimo

# Sqreen
# RUN curl -s https://8dc0b36f0ea6f2f21b721765e10a7e02768cd1825b4551f4:@packagecloud.io/install/repositories/sqreen/sqreen/script.deb.sh | bash \
#     && apt-get update \
#     && apt-get install -y --no-install-recommends sqreen-agent sqreen-php-extension \
#     && apt-clean \
#     && sqreen-installer set_ini token tmp \
#     && sqreen-installer set_ini socket_path tmp \
#     && sqreen-installer set_ini launch_daemon 0 \
#     && sqreen-installer set_ini disable tmp \
#     && sed -i "s/sqreen.token.*/sqreen.token=\${SQREEN_TOKEN}/" /usr/local/etc/php/conf.d/50-sqreen.ini \
#     && sed -i "s/sqreen.socket_path.*/sqreen.socket_path=\${SQREEN_SOCKET_PATH}/" /usr/local/etc/php/conf.d/50-sqreen.ini \
#     && sed -i "s/sqreen.disable.*/sqreen.disable=\${SQREEN_DISABLE}/" /usr/local/etc/php/conf.d/50-sqreen.ini \
#     && rm /var/log/sqreen/sqreen.log
# ENV SQREEN_DISABLE true

# Datadog PHP Tracer
RUN wget https://github.com/DataDog/dd-trace-php/releases/download/0.36.1/datadog-php-tracer_0.36.1_amd64.deb -O datadog-php-tracer.deb \
    && dpkg -i datadog-php-tracer.deb \
    && rm datadog-php-tracer.deb
ENV DD_TRACE_ENABLED false

###########################################################################
# MySQL Client
###########################################################################

RUN apt-get update \
    && apt-get install -y --no-install-recommends mariadb-client \
    && apt-clean

###########################################################################
# NODE
###########################################################################

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash \
    && apt-get install -y --no-install-recommends nodejs \
    && apt-clean \
    && rm /etc/apt/sources.list.d/nodesource.list

# Fix www-data NPM
RUN mkdir /var/www/.config && chown -R www-data:www-data /var/www/.config

###########################################################################
# Browsershot
###########################################################################

RUN apt-get update \
    && apt-get install -y nodejs gconf-service libasound2 libatk1.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 ca-certificates fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils wget \
    && npm install puppeteer --global --unsafe-perm=true \
    && chmod -R o+rx /usr/lib/node_modules/puppeteer/.local-chromium

###########################################################################
# Finalize
###########################################################################

RUN mkdir /app
COPY ./www.conf /usr/local/etc/php-fpm.d/www.conf
COPY ./php.ini /usr/local/etc/php/php.ini

###########################################################################
# Docker
###########################################################################

WORKDIR /app
EXPOSE 9000
CMD ["php-fpm"]
