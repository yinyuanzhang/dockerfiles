FROM ubuntu:14.04
MAINTAINER snowmoon1242

# reset apt-get sources list
RUN rm -f /etc/apt/sources.list && \
    echo "deb http://jp.archive.ubuntu.com/ubuntu/ trusty main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "deb-src http://jp.archive.ubuntu.com/ubuntu/ trusty main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "deb http://jp.archive.ubuntu.com/ubuntu/ trusty-updates main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "deb-src http://jp.archive.ubuntu.com/ubuntu/ trusty-updates main restricted universe multiverse" >> /etc/apt/sources.list

RUN apt-get update \
&&  apt-get upgrade -y

# install packages
RUN apt-get install -y vim git htop w3m aptitude locales \
 apache2 php5 php-pear php-compat php5-gd php-http-request php-pager php-file php5-curl \
 curl unzip wget libwww-perl

# install pukiwiki
COPY pukiwiki-1_5_0_utf8.zip /var/www/
RUN cd /var/www/ && unzip pukiwiki-1_5_0_utf8.zip
COPY pukiwiki.ini.php /var/www/pukiwiki-1_5_0_utf8/pukiwiki.ini.php
COPY default /etc/apache2/sites-available/000-default.conf

# install XML-TreePP
RUN mkdir /var/XMLTree \
&&  cd /var/XMLTree \
&&  wget http://ftp.riken.jp/pub/lang/CPAN/modules/by-category/13_Internationalization_Locale/Encode/KAWASAKI/XML-TreePP-0.43.tar.gz \
&&  tar zxvf XML-TreePP-0.43.tar.gz \
&&  cd XML-TreePP-0.43 \
&&  perl Makefile.PL \
&&  apt-get install make \
&&  make \
&&  make test \
&&  make install

RUN wget http://ftp.riken.jp/pub/lang/CPAN/modules/by-category/13_Internationalization_Locale/Encode/KAWASAKI/XML-FeedPP-0.43.tar.gz \
&&  tar zxvf XML-FeedPP-0.43.tar.gz \
&&  cd XML-FeedPP-0.43 \
&&  perl Makefile.PL \
&&  apt-get install make \
&&  make \
&&  make test \
&&  make install

#Activate CGI
RUN ln -s /etc/apache2/mods-available/cgid.load /etc/apache2/mods-enabled/ \
&&  ln -s /etc/apache2/mods-available/cgid.conf /etc/apache2/mods-enabled/

#copy cgi file
COPY FeedConv.cgi /usr/lib/cgi-bin/
RUN chown www-data: /usr/lib/cgi-bin/FeedConv.cgi \
&&  chmod +x /usr/lib/cgi-bin/FeedConv.cgi

# start apache & endless
CMD apachectl start && tail -f /dev/null
