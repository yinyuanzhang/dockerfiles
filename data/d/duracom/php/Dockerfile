FROM ubuntu:bionic

# Lets apt-get don't ask questions.
ENV DEBIAN_FRONTEND=noninteractive
ENV ACCEPT_EULA=Y

# Install packages
RUN apt-get update && apt-get install -y gnupg2
RUN echo "deb http://ppa.launchpad.net/ondrej/php/ubuntu bionic main" > /etc/apt/sources.list.d/ondrej.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 4F4EA0AAE5267A6C
RUN apt-get update && apt-get install -y \
apt-transport-https curl \
wget \
ssmtp \
php7.3-fpm \
php-xdebug \
php7.3-soap \
php7.3-xml \
php7.3-mysql \
php7.3-gd \
php7.3-json \
php7.3-odbc \
php7.3-mbstring \
php7.3-zip \
php-imagick \
php7.3-curl \
php7.3-sqlite3 \
php7.3-intl \
git \
unzip \
htop \
php-redis \
npm \
vim \
unixodbc

# Stop the PHP fpm service
RUN service php7.3-fpm stop

# SqlSrv drivers
RUN mkdir /tmp/sqlsrv
RUN wget https://packages.microsoft.com/ubuntu/18.10/prod/pool/main/m/msodbcsql17/msodbcsql17_17.4.2.1-1_amd64.deb -qO /tmp/sqlsrv/msodbcsql17.deb
RUN dpkg -i /tmp/sqlsrv/msodbcsql17.deb
RUN wget https://github.com/microsoft/msphpsql/releases/download/v5.6.1/Ubuntu18-7.3.tar -qO /tmp/sqlsrv/sqlsrv.tar
RUN tar -C /tmp/sqlsrv -xvf /tmp/sqlsrv/sqlsrv.tar --strip-components 1
RUN cp /tmp/sqlsrv/*sqlsrv_73_nts*.so `php -i | grep -e '^extension_dir' | sed -rn 's/.*=> (.*).*$/\1/p'`
RUN rm -rf /tmp/sqlsrv

# Install Composer
RUN wget https://getcomposer.org/composer.phar -qO /usr/bin/composer && chmod +x /usr/bin/composer

# wkhtmltopdf
RUN apt-get -y install fontconfig libxrender1 xfonts-75dpi xfonts-base
RUN wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox_0.12.5-1.bionic_amd64.deb -qLO /tmp/wkhtmltopdf.deb
RUN dpkg -i /tmp/wkhtmltopdf.deb
RUN rm -f /tmp/wkhtmltopdf.deb

# FFMpeg
RUN apt-get update && apt-get -y install ffmpeg --no-install-recommends

# Copy PHP configuration
COPY ./conf/php-fpm.conf /etc/php/7.3/fpm/php-fpm.conf
COPY ./conf/www.conf /etc/php/7.3/fpm/pool.d/www.conf
COPY ./conf/php.ini /etc/php/7.3/fpm/php.ini
COPY ./conf/20-sqlsrv.ini /etc/php/7.3/fpm/conf.d
COPY ./conf/30-pdo_sqlsrv.ini /etc/php/7.3/fpm/conf.d
COPY ./conf/20-sqlsrv.ini /etc/php/7.3/cli/conf.d
COPY ./conf/30-pdo_sqlsrv.ini /etc/php/7.3/cli/conf.d
COPY ./conf/ssmtp.conf /etc/ssmtp/ssmtp.conf
RUN cd /etc/php/7.3/cli; rm php.ini; ln -s ../fpm/php.ini

WORKDIR /wwwroot
CMD php-fpm7.3 -F -R
