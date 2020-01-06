FROM php:5-apache
MAINTAINER dubrox <dubrox@gmail.com>

# Enables apache rewrite
RUN a2enmod rewrite

# Installing NodeJs installation pre-requisites
RUN apt-get update && apt-get install -my wget gnupg

# Loading NodeJs v10 apt sources
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -

# Loading yarn sources
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
    echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list

# Setting up needed libraries and programs
RUN apt-get update && \
    apt-get install -y \
        # Alphabetical sort
        # following best practices for readability
        build-essential \
        curl \
        git \
        libbz2-dev \
        libcurl4-openssl-dev \
        libc-client-dev \
        libfreetype6-dev \
        libgmp-dev \
        libicu-dev \
        libjpeg62-turbo-dev \
        libkrb5-dev \
        libldap2-dev \
        libldb-dev ssmtp \
        libmcrypt-dev \
        libmemcached-dev \
        libncurses5-dev \
        libpng-dev \
        libpspell-dev \
        libssl-dev \
        libxml2-dev \
        libxslt1-dev \
        mysql-client \
        nodejs \
        wget \
        zlib1g-dev \
        && \
    # Removing apt cache lists to reduce the image size
    rm -rf /var/lib/apt/lists/* && \
    # Creating needed libraries softlinks
    ln -s /usr/include/x86_64-linux-gnu/gmp.h /usr/include/gmp.h && \
    ln -s /usr/lib/x86_64-linux-gnu/libldap.so /usr/lib/libldap.so && \
    ln -s /usr/lib/x86_64-linux-gnu/liblber.so /usr/lib/liblber.so

# MySQL Utilities
RUN wget https://dev.mysql.com/get/Downloads/Connector-Python/mysql-connector-python_2.1.5-1debian8.2_all.deb && \
    wget https://dev.mysql.com/get/Downloads/MySQLGUITools/mysql-utilities_1.6.5-1debian8_all.deb && \
    dpkg -i mysql-connector-python_2.1.5-1debian8.2_all.deb && \
    dpkg -i mysql-utilities_1.6.5-1debian8_all.deb

# Setting up php extensions
RUN docker-php-ext-configure gd \
        --enable-gd-native-ttf \
        --with-jpeg-dir=/usr/lib/x86_64-linux-gnu \
        --with-png-dir=/usr/lib/x86_64-linux-gnu \
        --with-freetype-dir=/usr/lib/x86_64-linux-gnu && \
    docker-php-ext-configure imap --with-kerberos --with-imap-ssl && \
    docker-php-ext-install -j$(nproc) \
        bcmath \
        bz2 \
        calendar \
        ctype \
        curl \
        dom \
        exif \
        ftp \
        gd \
        gettext \
        gmp \
        hash \
        iconv \
        imap \
        intl \
        json \
        ldap \
        mbstring \
        mcrypt \
        mysql \
        mysqli \
        pcntl \
        pdo \
        pdo_mysql \
        posix \
        pspell \
        session \
        soap \
        sockets \
        tokenizer \
        xml \
        xmlreader \
        xmlrpc \
        xsl \
        zip

# Installing composer
ENV COMPOSER_ALLOW_SUPERUSER 1
RUN php -r "readfile('https://getcomposer.org/installer');" > composer-setup.php && \
    php composer-setup.php --install-dir=/usr/bin --filename=composer && \
    php -r "unlink('composer-setup.php');"

# Installing gulp and bower
RUN npm install --global \
    gulp \
    gulp-cli \
    bower

# Installing x-debug
RUN pecl install xdebug-2.5.5 && \
    docker-php-ext-enable xdebug && \
    touch /var/log/xdebug.log && \
    chmod 0777 /var/log/xdebug.log

