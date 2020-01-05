FROM ghifari160/apache:16.04

LABEL MAINTAINER "Ghifari160 <ghifari160@ghifari160.com>"

# Disable interactive functions
ENV DEBIAN_FRONTEND noninteractive

RUN apt update && \

# Install Git and Make
    apt install -y git make && \

# Install build prerequisite
    apt install -y autoconf automake libtool gcc g++ build-essential \
        libxml2-dev apache2-dev && \

# Build and install Bison v2.7
    wget http://ftp.gnu.org/pub/gnu/bison/bison-2.7.tar.gz -O bison-2.7.tar.gz && \
    tar -xvzf bison-2.7.tar.gz && cd /bison-2.7 && ./configure \
        --prefix=/usr/local/bison \
        --with-libiconv-prefix=/usr/local/libiconv && \
    make && make install && export PATH=$PATH:/usr/local/bison/bin && \

# Download PHP v5.5.38 source code
    cd / && \
    git clone -b PHP-5.5.38 --single-branch https://github.com/php/php-src.git && \

# Build and install PHP v5.5.38
    cd /php-src && ./buildconf --force && \
    ./configure --with-apxs2=/usr/bin/apxs2 --enable-maintainer-zts && \
    make && make install && \

# Clean up build environment
    rm -rf /php-src/* /bison-2.7/* /bison-2.7.tar.gz && \

# Uninstall build prerequisites
    apt remove --autoremove -y autoconf automake libtool gcc g++ \
        build-essential libxml2-dev apache2-dev && \

# Uninstall Git and Make
    apt remove --autoremove -y git make && \

# Clean up APT
    apt clean && rm -rf /var/lib/apt/lists/* && \

# Configure PHP
    wget https://gist.githubusercontent.com/Ghifari160/bc9a6b56a12706bfeb1292380347cc51/raw/php.ini -O /usr/local/lib/php.ini && \

# Configure Apache2 mod-php
    wget https://gist.githubusercontent.com/Ghifari160/a5c8778c192c34363178a9dc065029f3/raw/php.conf -O /etc/apache2/conf-available/php.conf && \
    a2enconf php

# Add the custom default page
RUN rm /var/www/html/index.html
ADD index.php /var/www/html/index.php
