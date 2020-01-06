FROM ubuntu:18.04
MAINTAINER roberto.ramos.e@gmail.com
ENV DEBIAN_FRONTEND=noninteractive
ENV USER_CI=www-data
ENV UID=1000
ENV GID=1000

#ENV GIT_NAME="Roberto Ramos"
#ENV GIT_EMAIL="roberto.ramos.e@gmail.com"


RUN apt-get update
RUN apt-get install -y software-properties-common # python-software-properties
# RUN LC_ALL=C.UTF-8 add-apt-repository -y -u ppa:ondrej/php
	
RUN apt-get update && apt-get install -yq --no-install-recommends \
    apt-utils \
    curl \
    # Install git
    git \
    git-flow \
    # Install unzip
    unzip \
    # Install apache
    apache2 \
    # Install php 7.2
    libapache2-mod-php7.2 \
    php7.2-cli \
    php7.2-json \
    php7.2-dev \
	php7.2-common \
    php7.2-curl \
    php7.2-fpm \
    php7.2-gd \
    php7.2-pgsql \
    php7.2-pdo-pgsql \
	php7.2-dba \
	php7.2-bcmath \
	php7.2-bz2 \
    php7.2-ldap \
    php7.2-mbstring \
    php7.2-mysql \
    php7.2-soap \
    php7.2-sqlite3 \
    php7.2-xml \
    php7.2-zip \
    php7.2-intl \
	php7.2-opcache \
	php7.2-mongodb \
    php-pear \
    php-imagick \
    # Install tools
    openssl nano graphicsmagick \
    imagemagick mysql-client iputils-ping \
	ssh sudo locales libcurl3-openssl-dev default-jdk \
	wget libreoffice-writer unoconv \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Install NodeJS
RUN curl -sL https://deb.nodesource.com/setup_10.x -o nodesource_setup.sh && bash nodesource_setup.sh && apt-get install -y nodejs

# Set locales
RUN locale-gen en_US.UTF-8 es_ES.UTF-8

RUN a2enmod rewrite

# Install PHPUnit
WORKDIR /root
RUN wget https://phar.phpunit.de/phpunit-7.0.phar && chmod +x phpunit-7.0.phar && mv phpunit-7.0.phar /usr/local/bin/phpunit

WORKDIR /var/www/html
RUN rm index.html

# Configure user
RUN useradd -ms /bin/bash $USER_CI || usermod -s /bin/bash $USER_CI && mkdir /home/$USER_CI
RUN usermod -a -G www-data $USER_CI && usermod -a -G $USER_CI www-data
RUN chmod -R 747 /home/$USER_CI && chown -Rf $USER_CI:$USER_CI /home/$USER_CI

#USER $USER_CI
#RUN git config --global user.name $GIT_NAME && git config --global user.email $GIT_EMAIL

USER root

RUN usermod -u $UID $USER_CI
RUN groupmod -g $GID $USER_CI

RUN chown -Rf $USER_CI:www-data /var/www
RUN rm /etc/localtime && ln -s /usr/share/zoneinfo/America/Santiago /etc/localtime




VOLUME [ "/var/www/html" ]

EXPOSE 80 443

CMD ["apache2ctl", "-D", "FOREGROUND"]
