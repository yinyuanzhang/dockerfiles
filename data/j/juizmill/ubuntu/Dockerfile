FROM ubuntu:18.04

MAINTAINER Jesus Vieira de Lima <jesusvieiradelima@gmail.com>

ENV TZ=America/Campo_Grande

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN export DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt -yq upgrade
RUN apt-get install -yq software-properties-common
RUN add-apt-repository -y ppa:ondrej/php
RUN apt-get -yq update
RUN apt-get install -yq vim git net-tools iputils-ping nodejs unzip php7.3 php-pear php7.3-curl php7.3-dev \
php7.3-gd php7.3-mbstring php7.3-zip php7.3-mysql php7.3-xml php7.3-bcmath \
php7.3-intl php7.3-imap php7.3-interbase php7.3-sqlite3 php7.3-soap php7.3-pgsql \
php7.3-fpm php-xdebug php-memcache php-redis

RUN apt install -y npm

RUN sed -i "s/;pm.max_requests =.*/pm.max_requests = 500/" /etc/php/7.3/fpm/pool.d/www.conf
RUN sed -i "s/listen = .*/listen = 9000/" /etc/php/7.3/fpm/pool.d/www.conf

RUN sed -i "s/error_reporting = .*/error_reporting = E_ALL | E_STRICT/" /etc/php/7.3/cli/php.ini
RUN sed -i "s/display_errors = .*/display_errors = On/" /etc/php/7.3/cli/php.ini
RUN sed -i "s/memory_limit = .*/memory_limit = 512M/" /etc/php/7.3/cli/php.ini
RUN sed -i "s/max_execution_time = .*/max_execution_time = 120/" /etc/php/7.3/cli/php.ini
RUN sed -i "s/expose_php = .*/expose_php = Off/" /etc/php/7.3/cli/php.ini
RUN sed -i "s/session.cookie_lifetime = .*/session.cookie_lifetime = 172800/" /etc/php/7.3/cli/php.ini
RUN sed -i "s/gc_maxlifetime = .*/gc_maxlifetime = 172800/" /etc/php/7.3/cli/php.ini
RUN sed -r -i "s/;date.timezone =.*/date.timezone = America\/Campo_Grande/" /etc/php/7.3/cli/php.ini
RUN sed -i "s/short_open_tag = .*/short_open_tag = On/" /etc/php/7.3/cli/php.ini
RUN sed -i "s/post_max_size = .*/post_max_size = 100M/" /etc/php/7.3/cli/php.ini
RUN sed -i "s/upload_max_filesize = .*/upload_max_filesize = 100M/" /etc/php/7.3/cli/php.ini

RUN sed -i "s/error_reporting = .*/error_reporting = E_ALL | E_STRICT/" /etc/php/7.3/fpm/php.ini
RUN sed -i "s/display_errors = .*/display_errors = On/" /etc/php/7.3/fpm/php.ini
RUN sed -i "s/memory_limit = .*/memory_limit = 512M/" /etc/php/7.3/fpm/php.ini
RUN sed -i "s/max_execution_time = .*/max_execution_time = 120/" /etc/php/7.3/fpm/php.ini
RUN sed -i "s/expose_php = .*/expose_php = Off/" /etc/php/7.3/fpm/php.ini
RUN sed -i "s/session.cookie_lifetime = .*/session.cookie_lifetime = 172800/" /etc/php/7.3/fpm/php.ini
RUN sed -i "s/gc_maxlifetime = .*/gc_maxlifetime = 172800/" /etc/php/7.3/fpm/php.ini
RUN sed -r -i "s/;date.timezone =.*/date.timezone = America\/Campo_Grande/" /etc/php/7.3/fpm/php.ini
RUN sed -i "s/short_open_tag = .*/short_open_tag = On/" /etc/php/7.3/fpm/php.ini
RUN sed -i "s/post_max_size = .*/post_max_size = 100M/" /etc/php/7.3/fpm/php.ini
RUN sed -i "s/upload_max_filesize = .*/upload_max_filesize = 100M/" /etc/php/7.3/fpm/php.ini


RUN echo 'zend_extension=xdebug.so \n\
xdebug.scream=0 \n\
xdebug.cli_color=1 \n\
xdebug.show_local_vars=1 \n\
xdebug.max_nesting_level=250 \n\
xdebug.remote_enable = 1 \n\
xdebug.remote_autostart = 1 \n\
xdebug.idekey="VSCODE"'> /etc/php/7.3/cli/conf.d/20-xdebug.ini

RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && php composer-setup.php --install-dir=/usr/local/bin --filename=composer

RUN mkdir -p /usr/share/nginx/html
WORKDIR /usr/share/nginx/html

EXPOSE 9000
CMD ["php"]