FROM ubuntu:18.04

MAINTAINER rahworkx

## Update Ubuntu Software repository
RUN apt-get update && \
    apt-get install -y software-properties-common

## Install Base Tools
RUN apt-get install -y curl \
            nginx \
            git

## Add PHP7.3 Install
ENV DEBIAN_FRONTEND=noninteractive
RUN add-apt-repository ppa:ondrej/php
RUN apt-get update && \ 
    apt-get install -y \
            php7.3 \
            php7.3-cli \
            php7.3-mysql \
            php7.3-gd \
            php7.3-imagick \ 
            php7.3-recode \
            php7.3-tidy \
            php7.3-xmlrpc \
            php7.3-common \
            php7.3-curl \
            php7.3-mbstring \
            php7.3-xml \
            php7.3-bcmath \
            php7.3-bz2 \ 
            php7.3-intl \
            php7.3-json \
            php7.3-readline \
            php7.3-zip

## Install Composer
RUN curl -s https://getcomposer.org/installer | php && \
    mv composer.phar /usr/local/bin/composer

## Install Deployer
RUN curl -LO https://deployer.org/deployer.phar && \
    mv deployer.phar /usr/local/bin/dep && \
    chmod +x /usr/local/bin/dep

## Install NodeJS
RUN apt-get install nodejs -y

## Install NVM
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.34.0/install.sh | bash

## Install Python 3
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update && \
    apt-get install -y \
            software-properties-common \
            python3-distutils \
            python3 \
            python3-pip \
            python3-setuptools \
            groff \
            less \
   && pip3 install --upgrade pip \
   && apt-get clean

## Install AWS-CLI
RUN python3 -m pip --no-cache-dir install --upgrade awscli
ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY
ARG AWS_DEFAULT_REGION

CMD ["nginx", "-g", "daemon off;"]
