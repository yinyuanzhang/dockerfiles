from ubuntu:16.04

ENV DEBIAN_FRONTEND noninteractive

# update
RUN apt-get update && apt-get upgrade -y

# install packages
RUN apt-get install -y software-properties-common curl zip unzip git nano vim netcat

# add repositories
RUN echo "deb http://ppa.launchpad.net/ondrej/php/ubuntu xenial main" > /etc/apt/sources.list.d/ppa_ondrej_php.list && \
  echo "deb http://ppa.launchpad.net/nginx/development/ubuntu xenial main" > /etc/apt/sources.list.d/ppa_nginx_mainline.list && \
  apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E5267A6C && \
  apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C300EE8C && \
  curl -sL https://deb.nodesource.com/setup_8.x | bash -

# update repositories
RUN apt-get update

# install php, nginx, node
RUN apt-get install -y nodejs nginx php7.1-fpm php7.1-cli php7.1-dev php7.1-pgsql php7.1-sqlite3 php7.1-gd \
    php-apcu php7.1-curl php7.1-mcrypt php7.1-imap php7.1-mysql php7.1-readline php-xdebug php-common \
    php7.1-mbstring php7.1-xml php7.1-zip php7.1-bcmath

# configure nginx
COPY utils/nginx.conf /etc/nginx/sites-available/default
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

# install composer
RUN php -r "readfile('http://getcomposer.org/installer');" | php -- --install-dir=/usr/bin/ --filename=composer
RUN mkdir /run/php
COPY utils/php-fpm.conf /etc/php/7.1/fpm/php-fpm.conf
RUN echo 'alias art="php artisan"' >> ~/.bashrc
RUN echo "alias phpunit='./vendor/bin/phpunit'" >> ~/.bashrc

# install yarn
RUN npm i -g yarn
RUN yarn global add npm-check-updates pm2

# install supervisor
RUN apt-get install -y supervisor && mkdir -p /var/log/supervisor
COPY utils/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

COPY utils/init.sh /init.sh

EXPOSE 80 443 3000-3010
VOLUME ["/app"]
CMD ["/init.sh"]
