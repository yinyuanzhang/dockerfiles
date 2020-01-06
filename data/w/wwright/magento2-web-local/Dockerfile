FROM ubuntu:16.04

MAINTAINER Will Wright <will@magesmith.com>

# disable interactive functions
ARG DEBIAN_FRONTEND=noninteractive

RUN export LC_ALL=en_US.UTF-8 && export LANG=en_US.UTF-8 && \
    apt-get update && \
    apt-get install -y --allow-unauthenticated software-properties-common ntp build-essential build-essential binutils \
    zlib1g-dev python-pip language-pack-en-base curl wget git acl lzop unzip nano && \
    add-apt-repository ppa:ondrej/php && \
    apt-get update && \
    apt-get install -y --allow-unauthenticated \
    openssh-server mysql-client mcrypt expat xsltproc apache2 apache2-utils libapache2-mod-php \
    php7.1 php7.1-curl php7.1-common php7.1-gd php7.1-mcrypt \
    php7.1-dev php7.1-opcache php7.1-json php7.1-mysql php7.1-readline php7.1-xsl php7.1-xmlrpc \
    php7.1-intl php7.1-zip php7.1-soap php7.1-cli php7.1-xml php7.1-mbstring php7.1-bcmath php-redis \
    php7.1-bz2 php7.1-imagick php7.1-xdebug telnet \
    && phpenmod mcrypt xsl imagick \
    && a2enmod headers rewrite ssl expires php7.1 \
    && update-alternatives --set php /usr/bin/php7.1 \
    && update-alternatives --set phar /usr/bin/phar7.1 \
    && update-alternatives --set phar.phar /usr/bin/phar.phar7.1 \
    && update-alternatives --set phpize /usr/bin/phpize7.1 \
    && update-alternatives --set php-config /usr/bin/php-config7.1 \

#
#   Install Composer
#
    && curl -sSL https://getcomposer.org/composer.phar -o /usr/bin/composer \
    && chmod +x /usr/bin/composer \
#
#   Install n98-magerun
#
    && cd ~ && wget https://files.magerun.net/n98-magerun2.phar && \
    chmod +x ./n98-magerun2.phar && \
    cp ./n98-magerun2.phar /usr/local/bin/

#
#   Delete prepackaged defaults
#
RUN rm -rf /etc/apache2/ports.conf /etc/apache2/sites-enabled/* /var/lib/apt/lists/*

#
#   Run apache in foreground
#
COPY files/apache2-foreground /usr/local/bin/
RUN chmod +x /usr/local/bin/apache2-foreground

#
#   Inject config files at the end to optimize build cache
#
COPY etc/apache2/sites-available /etc/apache2/sites-available
COPY etc/apache2/ports.conf /etc/apache2/ports.conf

#
#   Xdebug setup
#
COPY etc/php/7.1/mods-available/xdebug.ini etc/php/7.1/mods-available/xdebug.ini
RUN touch /var/log/xdebug.log && chmod a+rwx /var/log/xdebug.log
RUN phpenmod xdebug

RUN a2ensite site site-ssl && service apache2 restart

RUN chown -R www-data:www-data /var/www/html

COPY configs/apache2/php.ini /etc/php/7.1/apache2/php.ini
COPY configs/cli/php.ini /etc/php/7.1/cli/php.ini

COPY provision/magento /usr/local/bin/magento
COPY provision/xmagento /usr/local/bin/xmagento
COPY provision/n98magerun2 /usr/local/bin/n98magerun2
COPY provision/xn98magerun2 /usr/local/bin/xn98magerun2

RUN chmod a+x /usr/local/bin/magento /usr/local/bin/xmagento /usr/local/bin/n98magerun2 /usr/local/bin/xn98magerun2

EXPOSE 80
WORKDIR /var/www/html/current
CMD bash /usr/local/bin/apache2-foreground