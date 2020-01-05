FROM phusion/baseimage:0.11

LABEL maintainer="Pavel Gavrilenko <paulgavrilenko@gmail.com>"

RUN DEBIAN_FRONTEND=noninteractive
RUN locale-gen en_US.UTF-8

ENV LANGUAGE=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8
ENV LC_CTYPE=en_US.UTF-8
ENV LANG=en_US.UTF-8
ENV TERM xterm

# Add the "PHP 7" ppa
RUN apt-get install -y software-properties-common && \
    add-apt-repository -y ppa:ondrej/php

#
#--------------------------------------------------------------------------
# Software's Installation
#--------------------------------------------------------------------------
#

# Install "PHP Extentions", "libraries", "Software's"
RUN apt-get update && \
    apt-get upgrade -y --option=Dpkg::Options::="--force-confold" && \
    apt-get install -y --allow-downgrades --allow-remove-essential \
        --allow-change-held-packages \
        php7.2-cli \
        php7.2-common \
        php7.2-curl \
        php7.2-json \
        php7.2-xml \
        php7.2-mbstring \
        php7.2-mysql \
        php7.2-zip \
        php7.2-memcached \
        php7.2-gd \
        php7.2-dev \
        pkg-config \
        libcurl4-openssl-dev \
        libedit-dev \
        libssl-dev \
        libxml2-dev \
        git \
        curl \
        vim \
        nano \
        iputils-ping \
    && apt-get clean

RUN apt-get install -yqq \
  apt-utils \
  libzip-dev zip unzip \
  php7.2-zip \
  wget

# MySQL Client:
RUN apt-get update -yqq && \
  apt-get -y install mysql-client

COPY mysql/mysql.cnf /etc/mysql/conf.d/mysql.cnf

# Sendmail client for mailhog:
RUN wget https://github.com/mailhog/mhsendmail/releases/download/v0.2.0/mhsendmail_linux_amd64 \
 && chmod +x mhsendmail_linux_amd64 \
 && mv mhsendmail_linux_amd64 /usr/local/bin/mhsendmail

# Install composer and add its bin to the PATH.
RUN curl -s http://getcomposer.org/installer | php && \
    echo "export PATH=${PATH}:/var/www/vendor/bin" >> ~/.bashrc && \
    mv composer.phar /usr/local/bin/composer

# Add a non-root user to prevent files being created with root permissions on host machine.
ARG PUID=1000
ENV PUID ${PUID}
ARG PGID=1000
ENV PGID ${PGID}

RUN groupadd -g ${PGID} xcdocker
RUN useradd -u ${PUID} -g xcdocker -m xcdocker -G docker_env    
RUN usermod -p "*" xcdocker -s /bin/bash

USER xcdocker

# Install X-DEV tool.

RUN mkdir ~/xdev && \
  cd ~/xdev && \
  composer require xcart/xdev

RUN mkdir ~/box && \
	cd ~/box && \
	composer require kherge/box=2.4

#--------------------------------------------------------------------------
# Home dir setup
#--------------------------------------------------------------------------
#
COPY ssh/config /home/xcdocker/.ssh/config

COPY --chown=xcdocker ./bash/.bash_aliases /home/xcdocker/.bash_aliases

COPY --chown=xcdocker ./bash/bash_autostart /home/xcdocker/tmp_bash_autostart

RUN echo "$(cat /home/xcdocker/tmp_bash_autostart)" >> /home/xcdocker/.bashrc && \
  rm /home/xcdocker/tmp_bash_autostart

COPY --chown=xcdocker ssh/config /home/xcdocker/.ssh/config

RUN mkdir /home/xcdocker/.xdev

COPY --chown=xcdocker xdev/* /home/xcdocker/.xdev/

USER root

COPY ./php/xc5.3/php.ini /etc/php/7.2/cli/php.ini

RUN chown -R xcdocker:xcdocker /home/xcdocker/.ssh