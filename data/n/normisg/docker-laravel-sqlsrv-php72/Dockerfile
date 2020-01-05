FROM ubuntu:16.04

MAINTAINER Normunds Galejs (normisg@gmail.com)

ARG DEBIAN_FRONTEND=noninteractive
ARG PHP_VERSION=7.2
ARG COMPOSER_ALLOW_SUPERUSER=1

# update distro and install common dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
        ca-certificates \
        curl \
        git \
        locales \
        unzip \
        vim && \
    echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen && \
    apt-get -y autoremove && \
    rm -rf /var/lib/apt/lists/*

# install sqlsrv client
RUN apt-get update && apt-get install -y --no-install-recommends \
        apt-transport-https && \
    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get install -y --no-install-recommends \
        msodbcsql \
        mssql-tools \
        unixodbc-dev &&\
    echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile && \
    echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc && \
    apt-get -y autoremove && \
    rm -rf /var/lib/apt/lists/*    

# install apache
RUN apt-get update && apt-get install -y --no-install-recommends \
        apache2 && \
    apt-get -y autoremove && \
    rm -rf /var/lib/apt/lists/* && \
    mkdir -p /var/www/public && \
    a2enmod rewrite
COPY ./etc/apache2/sites-available/000-default.conf /etc/apache2/sites-available/000-default.conf

# add PHP repository
RUN apt-get update && apt-get install -y --no-install-recommends \
        python-software-properties \
        software-properties-common && \
    LC_ALL=C.UTF-8 add-apt-repository -y -u ppa:ondrej/php && \
    apt-get -y autoremove && \
    rm -rf /var/lib/apt/lists/*

# install PHP
RUN apt-get update && apt-get install -y --no-install-recommends \
        libapache2-mod-php${PHP_VERSION} \
        php${PHP_VERSION}-bcmath \
        php${PHP_VERSION}-bz2 \
        php${PHP_VERSION}-cli \
        php${PHP_VERSION}-common \
        php${PHP_VERSION}-curl \
        php${PHP_VERSION}-dba \
        php${PHP_VERSION}-dev \
        php${PHP_VERSION}-gd \
        php${PHP_VERSION}-imap \
        php${PHP_VERSION}-intl \
        php${PHP_VERSION}-ldap \
        php${PHP_VERSION}-mbstring \
        php${PHP_VERSION}-memcache \
        php${PHP_VERSION}-mysql \
        php${PHP_VERSION}-odbc \
        php${PHP_VERSION}-recode \
        php${PHP_VERSION}-soap \
        php${PHP_VERSION}-sqlite \
        php${PHP_VERSION}-tidy \
        php${PHP_VERSION}-xml \
        php${PHP_VERSION}-xmlrpc \
        php${PHP_VERSION}-xsl \
        php${PHP_VERSION}-zip \
        php-pear && \
        apt-get -y autoremove && \
    rm -rf /var/lib/apt/lists/*

# install Microsoft SQL Server Driver for PHP
RUN apt-get update && apt-get install -y --no-install-recommends \
        g++ \
        make && \
        pecl install sqlsrv pdo_sqlsrv && \
        echo "extension=sqlsrv.so" >> /etc/php/${PHP_VERSION}/mods-available/sqlsrv.ini && \
        echo "extension=pdo_sqlsrv.so" >> /etc/php/${PHP_VERSION}/mods-available/pdo_sqlsrv.ini && \
        phpenmod sqlsrv pdo_sqlsrv && \
        apt-get -y remove g++ make && \
        apt-get -y autoremove && \
    rm -rf /var/lib/apt/lists/*

# install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

WORKDIR /var/www/public

EXPOSE 80

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]