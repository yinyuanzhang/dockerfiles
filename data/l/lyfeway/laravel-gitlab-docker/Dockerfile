FROM ubuntu:16.04
LABEL maintainer "Lyfeway <lyfeway@gmail.com>"

ARG DEBIAN_FRONTEND=noninteractive

# Initial setup
RUN apt-get update && \
    apt-get install -y \
        software-properties-common \
        python-software-properties

# Add trusted keys
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 4F4EA0AAE5267A6C

RUN apt-get install locales
RUN locale-gen en_US.UTF-8
ENV LANG       en_US.UTF-8
ENV LC_ALL     en_US.UTF-8

# Add repositories through PPA
RUN add-apt-repository -y ppa:ondrej/php && \
    apt-get update

# Install essential packages
RUN apt-get install -y \
    apt-transport-https \
    lsb-release \
    ca-certificates \
    wget \
    curl \
    build-essential \
    git \
    unzip \
    supervisor \
    mysql-client \
    openssh-client

# Install PHP 7.1
RUN apt-get install -y --allow-unauthenticated \
    php7.1-fpm \
    php7.1-cli \
    php7.1-curl \
    php7.1-mysql \
    php7.1-mcrypt \
    php7.1-mbstring \
    php7.1-dom \
    php7.1-xdebug \
    php7.1-tidy \
    php7.1-gd \
    php7.1-zip \
    php7.1-sqlite3 \
    php7.1-gmp

# Install Composer
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \
    php composer-setup.php && \
    mv composer.phar /usr/local/bin/composer && \
    php -r "unlink('composer-setup.php');"

# Install NodeJs
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash - && apt-get install -y nodejs

# Laravel Dusk support
RUN apt-get update && \
    apt-get -y install \
        libxpm4 libxrender1 libgtk2.0-0 libnss3 libgconf-2-4 \
        xvfb gtk2-engines-pixbuf xfonts-cyrillic xfonts-100dpi \
        xfonts-75dpi xfonts-base xfonts-scalable imagemagick x11-apps


RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - 
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
RUN apt update
RUN apt install -y google-chrome-stable



# Display versions
RUN php -v
RUN composer -V
RUN nodejs -v
RUN npm -v
RUN google-chrome --version