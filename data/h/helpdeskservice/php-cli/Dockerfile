FROM php:7.2.24-fpm

ARG IBM_DSDRIVER_PACKAGE=ibm_data_server_driver_package_linuxx64_v11.1.tar.gz
ARG IBM_DSDRIVER_ODBC=dsdriver/odbc_cli_driver/linuxamd64/ibm_data_server_driver_for_odbc_cli.tar.gz
ARG ORACLE_INSTANTCLIENT=instantclient-basic-linux.x64-18.3.0.0.0dbru.zip
ARG ORACLE_INSTANTCLIENT_SDK=instantclient-sdk-linux.x64-18.3.0.0.0dbru.zip

ENV DB2DIR=/opt/ibm/clidriver
ENV ORACLE_HOME=/opt/oracle/instantclient_18_3
ENV LD_LIBRARY_PATH=${DB2DIR}:${ORACLE_HOME}

RUN set -xe \
 && usermod -u 82 www-data \
 && groupmod -g 82 www-data \
 && mkdir -p /opt/ibm \
 && mkdir -p /opt/oracle \
 && apt-get update \
 && apt-get install -y --no-install-recommends \
        apt-transport-https \
        dnsutils \
        gnupg \
        libaio1 \
        libbz2-dev \
        libc-client-dev \
        libgmp-dev \
        libicu-dev \
        libjpeg62-turbo \
        libjpeg62-turbo-dev \
        libkrb5-dev \
        libldap2-dev \
        libmcrypt-dev \
        libmcrypt4 \
        libpcre3-dev \
        libpng-dev \
        libpng16-16 \
        libpq-dev \
        libpq5 \
        libtidy-dev \
        libtidy5deb1 \
        libxml2-dev \
        libxslt1-dev \
        libxslt1.1 \
        libzip-dev \
        locales \
        openssh-client \
        procps \
        rsync \
        unzip \
        wget \
 && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
 && curl https://packages.microsoft.com/config/debian/10/prod.list \
        > /etc/apt/sources.list.d/mssql-release.list \
 && echo "en_US.UTF-8 UTF-8" > /etc/locale.gen \
 && locale-gen \
 && apt-get update \
 && ACCEPT_EULA=Y \
    apt-get install -y --no-install-recommends \
        libodbc1 \
        libodbcinstq4-1 \
        msodbcsql17 \
        unixodbc-dev \
 && wget https://s3.eu-central-1.amazonaws.com/for-install/${IBM_DSDRIVER_PACKAGE} \
        -P /tmp \
 && tar -xzvf \
        /tmp/${IBM_DSDRIVER_PACKAGE} \
        ${IBM_DSDRIVER_ODBC} \
 && rm -f /tmp/${IBM_DSDRIVER_PACKAGE} \
 && tar -xzvf \
        ${IBM_DSDRIVER_ODBC} \
        -C /opt/ibm/ \
 && rm -rf ./dsdriver \
 && wget \
        https://s3.eu-central-1.amazonaws.com/for-install/${ORACLE_INSTANTCLIENT} \
        -P /tmp \
 && unzip \
        /tmp/${ORACLE_INSTANTCLIENT} \
        -d /opt/oracle \
 && rm -f /tmp/${ORACLE_INSTANTCLIENT} \
 && wget \
        https://s3.eu-central-1.amazonaws.com/for-install/${ORACLE_INSTANTCLIENT_SDK} \
        -P /tmp \
 && unzip \
        /tmp/${ORACLE_INSTANTCLIENT_SDK} \
        -d /opt/oracle \
 && rm -f /tmp/${ORACLE_INSTANTCLIENT_SDK} \
 && docker-php-ext-configure \
        imap --with-imap-ssl --with-kerberos \
 && docker-php-ext-configure \
        oci8 --with-oci8=instantclient,${ORACLE_HOME} \
 && docker-php-ext-configure \
        pdo_oci --with-pdo-oci=instantclient,${ORACLE_HOME} \
 && docker-php-ext-install -j4 \
        bcmath \
        bz2 \
        calendar \
        exif \
        gd \
        gettext \
        gmp \
        imap \
        intl \
        ldap \
        mysqli \
        oci8 \
        opcache \
        pcntl \
        pdo_mysql \
        pdo_oci \
        pdo_pgsql \
        pgsql \
        shmop \
        soap \
        sockets \
        sysvmsg \
        sysvsem \
        sysvshm \
        tidy \
        wddx \
        xmlrpc \
        xsl \
        zip \
 && pecl download pdo_ibm \
 && tar -xzvf PDO_IBM-*.tgz -C /tmp \
 && rm -f PDO_IBM-*.tgz \
 && cd /tmp/PDO_IBM-* \
 && phpize --clean \
 && phpize \
 && ./configure \
 && make \
 && make install \
 && pecl install \
        ibm_db2 \
        igbinary \
        mcrypt-1.0.1 \
        mongodb \
        oauth \
        pdo_sqlsrv \
        redis \
        sqlsrv \
        xdebug \
 && docker-php-ext-enable \
        ibm_db2 \
        igbinary \
        mcrypt \
        mongodb \
        oauth \
        pdo_ibm \
        pdo_sqlsrv \
        redis \
        sqlsrv \
 && pear channel-discover pear.phing.info \
 && pear install phing/phing \
 && apt-get remove -y \
        libbz2-dev \
        libc-client-dev \
        libgmp-dev \
        libicu-dev \
        libjpeg62-turbo-dev \
        libkrb5-dev \
        libldap2-dev \
        libmcrypt-dev \
        libpcre3-dev \
        libpng-dev \
        libpq-dev \
        libtidy-dev \
        libxml2-dev \
        libxslt1-dev \
        libzip-dev \
        unixodbc-dev \
 && apt-get autoremove -y \
 && apt-get clean all \
 && rm -r /var/lib/apt/lists/* \
 && rm -rf /tmp/*

COPY configs/ /

EXPOSE 9000

CMD ["php-fpm"]