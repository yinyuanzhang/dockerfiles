FROM eclipse/stack-base:ubuntu
ENV DEBIAN_FRONTEND noninteractive
ENV PHP_INI /etc/php/7.2/apache2

RUN sudo add-apt-repository ppa:ondrej/php

RUN sudo apt-get update && \
    sudo apt-get install -y --no-install-recommends libaio1 php7.2 php7.2-cli bzip2 \
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
    php-pear \
    libbz2-dev \
	  libjpeg-dev \
	  libldap2-dev \
	  libmemcached-dev \
	  libpng-dev 
RUN sudo sed -i 's/\/var\/www\/html/\/projects\/joomla/g'  /etc/apache2/sites-available/000-default.conf && \
    sudo sed -i 's/\/var\/www/\/projects\/joomla/g'  /etc/apache2/apache2.conf && \
    sudo sed -i 's/None/All/g' /etc/apache2/sites-available/000-default.conf && \
    echo "ServerName localhost" | sudo tee -a /etc/apache2/apache2.conf && \
    sudo a2enmod rewrite

ENV JOOMLA_VERSION 3.9.4
ENV JOOMLA_SHA512 fca41b63396c2f5429680297224f3345bc845b3c62a234c82c5c28af477f4a2b176c53d8b4b821b0c71a28a06f3c2a270b42d54396f3cf6075d72e27f136c4d9

# Download package and extract


EXPOSE 80

CMD sudo curl -o joomla.tar.bz2 -SL https://github.com/joomla/joomla-cms/releases/download/${JOOMLA_VERSION}/Joomla_${JOOMLA_VERSION}-Stable-Full_Package.tar.bz2 \
  && sudo mkdir /projects/joomla \
	&& sudo tar -xf joomla.tar.bz2 -C /projects/joomla \
  && sudo rm joomla.tar.bz2 \
  && sudo chmod -R 777 /projects \
	&& tail -f /dev/null
