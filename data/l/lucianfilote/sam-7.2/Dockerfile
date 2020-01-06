FROM debian:jessie

MAINTAINER Lucian Filote "lucianovidiu.filote@gameloft.com"

# Setup environment
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -y --fix-missing
RUN apt-get install wget apt-transport-https lsb-release ca-certificates -y
RUN wget -O /etc/apt/trusted.gpg.d/php.gpg https://packages.sury.org/php/apt.gpg
RUN echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" > /etc/apt/sources.list.d/php.list
RUN apt-get update -y
RUN apt-get install wget apache2 mysql-client -y
RUN apt-get install php7.2 -y
RUN apt-get install php7.2-dev -y
RUN apt-get install php7.2-xml -y
RUN apt-get install php7.2-opcache -y
RUN apt-get install php7.2-mysql -y
RUN apt-get install php7.2-zip -y
RUN apt-get install php7.2-curl -y
RUN apt-get install libapache2-mod-php7.2 -y
RUN apt-get install php7.2-mbstring -y
RUN apt-get install php-pear -y
RUN apt-get install curl -y
RUN pecl install timecop-beta
RUN echo "extension=timecop.so" >> /etc/php/7.2/cli/php.ini
RUN php -v
