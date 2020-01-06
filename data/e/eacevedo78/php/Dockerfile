# Copyright (c) 2012-2016 Codenvy, S.A.
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v1.0
# which accompanies this distribution, and is available at
# http://www.eclipse.org/legal/epl-v10.html
# Contributors:
# Codenvy, S.A. - initial API and implementation

FROM eclipse/stack-base:ubuntu
ENV DEBIAN_FRONTEND noninteractive
ENV ORACLE_HOME /opt/instantclient_12_2
ENV PHP_INI /etc/php/7.2/apache2

ADD instantclient-basic-linux.x64-12.2.0.1.0.zip /opt/
ADD instantclient-sdk-linux.x64-12.2.0.1.0.zip /opt
RUN cd /opt/ && sudo unzip instantclient-basic-linux.x64-12.2.0.1.0.zip && sudo rm instantclient-basic-linux.x64-12.2.0.1.0.zip
RUN cd /opt && sudo unzip instantclient-sdk-linux.x64-12.2.0.1.0.zip && sudo rm instantclient-sdk-linux.x64-12.2.0.1.0.zip
RUN sudo ln -s /opt/instantclient_12_2/libclntsh.so.12.1 /opt/instantclient_12_2/libclntsh.so && \
    sudo add-apt-repository ppa:ondrej/php

RUN sudo apt-get update && \
    sudo apt-get install -y libaio1 php7.2 php7.2-cli \
    apache2 \
    php-mcrypt \
    php7.2-curl \
    php7.2-mysql \
    php7.2-pgsql \
    php7.2-gd \
    libapache2-mod-php7.2 \
    php7.2-json \
    php7.2-cgi \
    php7.2-sqlite3 \
    php7.2-mbstring \
    php7.2-xml \
    php7.2-dev \
    php7.2-zip \
    php-pear

RUN sudo printf "instantclient,/opt/instantclient_12_2" | sudo pecl install oci8

RUN sudo printf ";configuracion oci8 para php\n;priority=20\nextension=oci8.so" > 20-oci8.ini && \
    sudo mv 20-oci8.ini /etc/php/7.2/mods-available && \
    sudo ln -s /etc/php/7.2/mods-available/20-oci8.ini /etc/php/7.2/apache2/conf.d/20-oci8.ini && \
    sudo ln -s /etc/php/7.2/mods-available/20-oci8.ini /etc/php/7.2/cli/conf.d/20-oci8.ini

RUN sudo sed -i 's/\/var\/www\/html/\/projects/g'  /etc/apache2/sites-available/000-default.conf && \
    sudo sed -i 's/\/var\/www/\/projects/g'  /etc/apache2/apache2.conf && \
    sudo sed -i 's/None/All/g' /etc/apache2/sites-available/000-default.conf && \
    echo "ServerName localhost" | sudo tee -a /etc/apache2/apache2.conf && \
    sudo a2enmod rewrite

RUN curl -sS https://getcomposer.org/installer | sudo php -- --install-dir=/usr/local/bin --filename=composer && \
    sudo chown -R user:users ~/.composer && \
    composer global require bamarni/symfony-console-autocomplete && \
    ~/.composer/vendor/bamarni/symfony-console-autocomplete/symfony-autocomplete --shell bash composer | sudo tee /etc/bash_completion.d/composer && \
    sudo wget -qO /usr/local/bin/phpunit https://phar.phpunit.de/phpunit.phar && sudo chmod +x /usr/local/bin/phpunit && \
    sudo apt-get clean && \
    sudo apt-get -y autoremove && \
    sudo apt-get -y clean && \
    sudo rm -rf /var/lib/apt/lists/*

RUN curl -sL https://deb.nodesource.com/setup_9.x | sudo bash - && \
    sudo apt-get update && \
    sudo apt-get install -y nodejs

RUN sudo composer global require "laravel/installer"

ENV PATH /home/user/.composer/vendor/bin:$PATH

EXPOSE 80 8000

CMD sudo chown -R www-data:www-data /projects && \
    sudo chmod -R 777 /projects && \
    tail -f /dev/null
