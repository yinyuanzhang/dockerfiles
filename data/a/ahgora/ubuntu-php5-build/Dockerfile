FROM        ubuntu:xenial
MAINTAINER  Ahgora Sistemas

RUN apt-get update &&\
    apt-get upgrade -y &&\
    apt-get install -y software-properties-common

# PHP stuff
RUN LC_ALL=C.UTF-8 add-apt-repository -y ppa:ondrej/php
RUN apt-get update && \ 
    apt-get install -y --no-install-recommends \ 
    apache2 \
    apache2-utils \ 
    autoconf \
    bash \
    binutils \
    bison \
    build-essential \
    ca-certificates \
    cmake \
    fabric \
    flex \
    fonts-droid-fallback \
    fonts-freefont-* \
    fonts-liberation \
    fonts-ubuntu-font-family-console \
    freetds-dev \
    g++ \
    gcc \
    git \
    glibc-source \
    imagemagick \
    language-pack-pt-base \
    libapache2-mod-php5.6 \
    libboost-all-dev \
    libbz2-dev \
    libc6-dev \
    libfontconfig1 \
    libgcc-5-dev \
    libgmp-dev \
    libgmp-dev \
    libintl-perl \
    libpcre3-dev \
    libstdc++-5-dev \
    libstdc++5 \
    libuv1-dev \
    libx11-6 \
    libxext-dev \
    libxext6 \
    libxrender-dev \
    libxrender1 \
    make \
    openssl \
    php-gettext \
    php-mongodb \
    php-pear \
    php5.6 \
    php5.6-cgi \
    php5.6-cli \
    php5.6-common \
    php5.6-curl \
    php5.6-dev \
    php5.6-gd \
    php5.6-iconv \
    php5.6-imap \
    php5.6-intl \
    php5.6-json \
    php5.6-mbstring \
    php5.6-mcrypt \
    php5.6-mssql \
    php5.6-mysql \
    php5.6-soap \
    php5.6-xml \
    php5.6-zip \
    pkg-config \
    software-properties-common \
    ttf-dejavu \
    wget \
    zip \
    zip openssl \
    zlib1g \
    zlib1g-dev \
    zlibc \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && \ 
    apt-get install -y --no-install-recommends \ 
    xfonts-75dpi \
    fontconfig \
    xfonts-base && \
    wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox_0.12.5-1.xenial_amd64.deb &&\
    dpkg -i wkhtmltox_0.12.5-1.xenial_amd64.deb

RUN wget https://github.com/ahgora/confd/blob/master/confd?raw=true -O /usr/local/bin/confd && \
    chmod +x /usr/local/bin/confd && \
    cd /tmp && rm -Rf *

# Instação do NewRelic agent
RUN mkdir -p /opt/newrelic && \
    cd /opt/newrelic && \
    wget http://download.newrelic.com/php_agent/release/newrelic-php5-9.1.0.246-linux.tar.gz  -O newrelic-php5-linux.tar.gz &&\
    tar -zxvf newrelic-php5-linux.tar.gz  && \
    rm newrelic-php5-linux.tar.gz && \
    cd /opt/newrelic/newrelic-php5-9.1.0.246-linux/ && \
    sh newrelic-install install

# Variables for enabling NewRelic
ENV  NR_APP_NAME="PHP Application" \
NR_INSTALL_SILENT=true

RUN \
    ln -s /usr/bin/php /usr/bin/php5 &&\
    phpenmod mcrypt &&\
    phpenmod imap &&\
    a2enmod rewrite &&\
    pecl install mongo &&\
    echo "extension=mongo.so" >> /etc/php/5.6/apache2/php.ini &&\
    echo "extension=mongo.so" >> /etc/php/5.6/cli/php.ini &&\
    pecl install redis-4.3.0 &&\
    echo "extension=redis.so" >> /etc/php/5.6/apache2/php.ini &&\
    echo "extension=redis.so" >> /etc/php/5.6/cli/php.ini &&\
    sed -i 's/^short_open_tag = Off$/short_open_tag = On/' /etc/php/5.6/apache2/php.ini &&\
    locale-gen pt_BR.UTF-8 &&\
    locale-gen en_US.UTF-8

RUN git clone https://github.com/datastax/php-driver.git && cd php-driver && git submodule update --init
WORKDIR /php-driver/lib/cpp-driver/
SHELL ["/bin/bash", "-c"]
RUN mkdir build && pushd build && cmake ../ && make && make install && popd

WORKDIR /php-driver/ext/
RUN ./install.sh
RUN \
    echo 'extension=cassandra.so' >> /etc/php/5.6/apache2/php.ini &&\
    echo 'extension=cassandra.so' >> /etc/php/5.6/cli/php.ini

RUN echo "LoadModule rewrite_module modules/mod_rewrite.so" >> /etc/apache2/httpd.conf


RUN \
    apt-get -y autoremove &&\
    apt-get -y clean &&\
    rm -rf /var/lib/apt/lists/*

WORKDIR /

EXPOSE 80 443 9000

CMD ["/usr/sbin/apachectl", "-D", "FOREGROUND"]
