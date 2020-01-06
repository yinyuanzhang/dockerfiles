FROM circleci/php:7.0-node-browsers

RUN sudo apt-get update
RUN sudo apt-get install -y libxml2-dev libbz2-dev libmcrypt-dev libzip-dev
RUN sudo docker-php-ext-install soap
RUN sudo docker-php-ext-install bz2
RUN sudo docker-php-ext-install mcrypt
RUN sudo docker-php-ext-install zip
RUN sudo docker-php-ext-install intl
RUN sudo docker-php-ext-install opcache
RUN sudo rm -rf /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini
RUN sudo npm install -g n
RUN sudo n 6.9.5
