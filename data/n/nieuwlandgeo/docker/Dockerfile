FROM circleci/php:7.2-cli-node-browsers

USER root

#  https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=866729
RUN mkdir -p /usr/share/man/man7

RUN apt-get update
RUN apt-get install -y apt-utils

RUN apt-get install -y libpq-dev libpng-dev unzip postgresql-client libbz2-dev libicu-dev gdal-bin libgeos-dev libmagickwand-dev openssl

RUN docker-php-ext-install -j$(nproc) gd pdo_pgsql zip bcmath bz2 gettext intl sockets

RUN pecl install imagick \
    && docker-php-ext-enable imagick


RUN sudo apt-get install -y openssl build-essential libfontconfig1 libxrender1 libssl-dev \
    && cd /tmp \
    && sudo wget "https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz" \
    && sudo tar xvf /tmp/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz \
    && sudo mv /tmp/wkhtmltox/bin/* /usr/local/bin \
    && sudo mv /tmp/wkhtmltox/include/* /usr/local/include \
    && sudo mv /tmp/wkhtmltox/lib/* /usr/local/lib \
    && sudo mkdir -p /usr/local/share/man/man1 \
    && sudo mv /tmp/wkhtmltox/share/man/man1/* /usr/local/share/man/man1 \
    && sudo rm -rf /usr/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz \
    && sudo rm -rf /usr/wkhtmltox

RUN apt-get update \
    && apt-get install -y ghostscript

WORKDIR /opt

RUN git clone https://git.osgeo.org/gitea/geos/php-geos.git

WORKDIR /opt/php-geos
RUN ./autogen.sh \ 
    && phpize \
    && ./configure \
    && make -j "$(nproc)" \
    && make install \ 
    && docker-php-ext-enable geos    

RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \
    && php -r "copy('https://composer.github.io/installer.sig', 'composer-setup.sig');" \
    && php -r "if (hash_file('SHA384', 'composer-setup.php') === trim(file_get_contents('composer-setup.sig'))) { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;" \
    && php composer-setup.php \
    && php -r "unlink('composer-setup.php');" \
    && mv composer.phar /usr/local/bin/composer

ADD php.ini /usr/local/etc/php/

RUN mkdir /app \    
    && mkdir /app/var \        
    && mkdir /app/var/jwt \
    && chown -R circleci /app


USER circleci

RUN openssl genrsa -out /app/var/jwt/private_test.pem -aes256 -passout pass:wgp5foo 4096
RUN openssl rsa -passin pass:wgp5foo -pubout -in /app/var/jwt/private_test.pem -out /app/var/jwt/public_test.pem
