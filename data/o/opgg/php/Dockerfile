FROM ubuntu:16.04

#######################################################################################################
# NGINX 인덱스 타겟: /usr/src/php-app[/public/index.php]
# 퍼블릭 이미지입니다. 절대 이 디렉토리나 이미지에 민감한 정보(키나 패스워드, 소스코드 등)는 담지 말길 바랍니다.
#######################################################################################################

################################################
# Install Compilers
RUN apt-get update \
&&  apt-get install -y make git wget software-properties-common python-software-properties

# ADD PPAs / sources
RUN LC_ALL=C.UTF-8 add-apt-repository -y ppa:ondrej/php \
&&  add-apt-repository -y ppa:nginx/stable \
&&  wget -O - https://download.newrelic.com/548C16BF.gpg | apt-key add - \
&&  echo "deb http://apt.newrelic.com/debian/ newrelic non-free" > /etc/apt/sources.list.d/newrelic.list

# Install Packages
RUN apt-get update \
&&  apt-get install -y supervisor nginx curl \
&&  DEBIAN_FRONTEND=noninteractive apt-get install -y php7.1-fpm php-redis php-imagick php-igbinary php-geoip php-apcu php-curl php-gd php-zip php-xml php-mbstring php-mysql \
&&  DEBIAN_FRONTEND=noninteractive apt-get install -y newrelic-php5 newrelic-sysmond

# Base Configuration
## Supervisord
RUN mkdir -p /var/log/supervisor
## PHP
RUN mkdir -p /var/log/php-fpm /run/php

# Clean Ups
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

###############################################################
# Configuration

## Supervisor
COPY dockerconfigs/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY dockerconfigs/logrotate_nginx.conf /etc/logrotate.d/nginx
COPY dockerconfigs/nginx.conf /etc/nginx/sites-available/default

## PHP
ADD dockerconfigs/php /etc/php/7.1
RUN phpenmod newrelic override

#######################
# Work
WORKDIR /usr/src

##################################################################
# Install Composer & Prestissimo
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \
&&  php -r "if (hash_file('SHA384', 'composer-setup.php') === '669656bab3166a7aff8a7506b8cb2d1c292f042046c5a994c43155c0be6190fa0355160742ab2e1c88d40d5be660b410') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;" \
&&  php composer-setup.php --install-dir=/usr/local/bin --filename=composer \
&&  php -r "unlink('composer-setup.php');" \
# 빠른 composer install 을 위함
&&  composer global require hirak/prestissimo

EXPOSE 80
CMD ["/usr/bin/supervisord", "-n"]
