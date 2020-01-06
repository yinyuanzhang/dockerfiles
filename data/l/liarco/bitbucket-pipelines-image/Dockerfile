FROM ubuntu:rolling
MAINTAINER Marco Lipparini

ARG DEBIAN_FRONTEND=noninteractive

# Install main dependencies
RUN apt-get update && \
    apt-get install -y \
        gcc \
        g++ \
        make \
        gnupg \
        curl \
        zip \
        unzip \
        wget \
        openssh-client \
        rsync \
        php7.2-cli \
        php7.2-xml \
        php7.2-mbstring \
        git && \
    curl -sL https://deb.nodesource.com/setup_10.x | bash - && \
    apt-get install -y nodejs && \
    rm -rf /var/lib/apt/lists/*

# Install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Install NodeJS tools
RUN npm install -g yarn sass typescript uglify-es

# Create new user
RUN groupadd -g 999 liarco && \
    useradd -rms /bin/bash -u 999 -g liarco liarco
USER liarco