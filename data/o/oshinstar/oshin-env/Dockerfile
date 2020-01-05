FROM ubuntu:bionic
MAINTAINER Oshinstar <oshinrd@gmail.com,oshindeveloper@gmail.com, oshindeveloper2@gmail.com>


# update
RUN  apt update && apt-get install -y --no-install-recommends apt-utils systemd

# generic tools
RUN  apt install -y wget net-tools git unzip curl iputils-ping telnet dnsutils nmap \
    software-properties-common apt-transport-https

ENV TZ=America/Santo_Domingo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

#RUN apk add --no-cache tzdata
ENV TZ America/Santo_Domingo

RUN apt update 

# nginx
RUN apt install -y nginx

# Install MySQL
RUN apt-get install -y mysql-client libmysqlclient-dev

# install php
RUN LC_ALL=C.UTF-8  add-apt-repository ppa:ondrej/php
RUN DEBIAN_FRONTEND=noninteractive apt update && apt install -y php7.2 php7.2-fpm \ 
    php7.2-cli php7.2-mysql php7.2-curl php7.2-gd php7.2-zip php7.2-ldap php7.2-xml \ 
    php7.2-mbstring php7.2-intl php7.2-bcmath php7.2-tokenizer php7.2-json php7.2-ctype \
    php7.2-intl 


RUN echo 'listen = /var/run/php/php7.2-fpm.sock' >> /etc/php/7.2/fpm/php-fpm.conf

# start webserver
RUN service php7.2-fpm start
RUN service nginx restart

# install composer
RUN curl -sS https://getcomposer.org/installer -o composer-setup.php
RUN php composer-setup.php --install-dir=/usr/local/bin --filename=composer
RUN composer


# install phpunit
RUN wget https://phar.phpunit.de/phpunit-7.5.5.phar
RUN chmod +x phpunit-7.5.5.phar
RUN mv phpunit-7.5.5.phar /usr/local/bin/phpunit
RUN phpunit --version


# install firefox for tests
RUN apt -y install npm nodejs


#install xdebug (code-coverage)
RUN apt install php7.2-xdebug
# COPY xdebug/xdebug.ini /usr/local/etc/php/conf.d/xdebug-dev.ini

#dumb-init
RUN wget https://github.com/Yelp/dumb-init/releases/download/v1.2.1/dumb-init_1.2.1_amd64.deb
RUN dpkg -i dumb-init_*.deb
