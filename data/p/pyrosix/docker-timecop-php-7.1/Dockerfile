FROM debian:jessie

MAINTAINER Alexandru Voinescu "voinescu.alex@gmail.com"

# Setup environment
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -y --fix-missing

RUN apt-get install wget apt-transport-https lsb-release ca-certificates -y

RUN wget -O /etc/apt/trusted.gpg.d/php.gpg https://packages.sury.org/php/apt.gpg
RUN echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" > /etc/apt/sources.list.d/php.list

RUN apt-get update -y

RUN apt-get install wget apache2 mysql-client -y

RUN apt-get install php7.2 php7.2-dev php7.2-common php-pear php-xml php7.2-opcache php7.2-mysql php7.2-zip php7.2-curl -y

RUN apt-get install php7.1 php7.1-dev php7.1-common php-pear php-xml php7.1-opcache php7.1-mysql php7.1-zip php7.1-curl -y

RUN apt-get install libapache2-mod-php7.2 -y

RUN pecl install timecop-beta

RUN echo "extension=timecop.so" >> /etc/php/7.2/cli/php.ini
RUN echo "extension=timecop.so" >> /etc/php/7.1/cli/php.ini

#Enable php7.1

RUN a2dismod php7.2 php7.1
RUN a2enmod php7.1
RUN service apache2 restart

RUN php -v

RUN update-alternatives --set php /usr/bin/php7.1
RUN update-alternatives --set phar /usr/bin/phar7.1
RUN update-alternatives --set phar.phar /usr/bin/phar.phar7.1
RUN update-alternatives --set phpize /usr/bin/phpize7.1
RUN update-alternatives --set php-config /usr/bin/php-config7.1

RUN php -i

RUN php -v