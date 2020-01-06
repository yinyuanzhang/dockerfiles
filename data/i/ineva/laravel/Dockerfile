FROM php:5.6.26-apache
MAINTAINER Steven <s@beeeye.cn>

# 安装gd依赖
RUN apt-get update && \
    apt-get install -y iptables libfreetype6-dev libjpeg62-turbo-dev libmcrypt-dev libpng12-dev libcurl3-dev libbz2-dev && \
    rm -rf /var/lib/apt/lists/* && \
    docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ && \
    docker-php-ext-install gd pdo_mysql mysqli mcrypt pdo mbstring zip opcache curl bz2 bcmath calendar mysql hash && \
    a2enmod rewrite && \
    mkdir -p /var/www/log && rm -f /etc/apache2/sites-enabled/*

# 安装Composer
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \
    php composer-setup.php --install-dir=/bin php composer-setup.php --filename=composer && \
    php -r "unlink('composer-setup.php');"

# 安装PageSpeed
RUN curl -O https://dl-ssl.google.com/dl/linux/direct/mod-pagespeed-stable_current_amd64.deb && dpkg -i *.deb && rm *.deb
