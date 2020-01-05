FROM liling/phusion-fundamental:0.9.18.1
MAINTAINER liling@bit.edu.cn

RUN mkdir -p /var/lock/apache2 /var/run/apache2

RUN echo 'ssl-cert:x:102:' >> /etc/group
RUN apt-get update; apt-get install -y php-pear php5-cli php5-common php5-curl php5-gd php5-intl php5-json php5-mysql php5-xmlrpc php5-xsl libapache2-mod-php5 php5-dev

RUN a2enmod rewrite
COPY 000-default.conf /etc/apache2/sites-available/000-default.conf

# Install PHP OCI8
RUN cd /tmp; wget 'https://pecl.php.net/get/oci8-2.0.12.tgz' ; tar xf /tmp/oci8-2.0.12.tgz; cd oci8-2.0.12; phpize; ./configure -with-oci8=shared,instantclient,/usr/lib/oracle/12.1/client64/lib; make; make install; cd /; rm -rf /tmp/oci8*
ADD php_oci8.ini /etc/php5/mods-available/oci8.ini
RUN php5enmod oci8

# Startup Apache
RUN mkdir /etc/service/apache2
ADD services/apache2.sh /etc/service/apache2/run
RUN chmod +x /etc/service/apache2/run

# Allow visit HTTP
EXPOSE 80

# Clean up
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
ENV LC_ALL zh_CN.UTF-8
