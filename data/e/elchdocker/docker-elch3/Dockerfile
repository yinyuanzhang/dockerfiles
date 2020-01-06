FROM ubuntu:18.04

RUN apt-get update -yqq
RUN apt-get install apt-utils -y
RUN apt-get install wget -y
RUN apt-get install language-pack-en git unzip curl -yqq
RUN apt-get install debconf-utils -y
ENV TZ=Europe/Zurich
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get install -y tzdata
RUN apt-get install -y software-properties-common
RUN ln -sf /usr/share/zoneinfo/Europe/Zurich /etc/localtime && dpkg-reconfigure -f noninteractive tzdata
RUN LC_ALL=C.UTF-8 add-apt-repository -y  ppa:ondrej/php
RUN apt-get update -yqq
RUN apt-get install -y php7.3 php7.3-cli php7.3-mbstring php7.3-zip php7.3-mysql php7.3-opcache php7.3-json php7.3-curl php7.3-ldap php7.3-intl php7.3-common php7.3-gd php7.3.soap php7.3-xml php7.3-sqlite3
RUN echo 'memory_limit=1G'> /etc/php/7.3/cli/conf.d/php-memory_limit.ini
RUN curl -sL https://deb.nodesource.com/setup_11.x| bash - && apt-get install nodejs -y

