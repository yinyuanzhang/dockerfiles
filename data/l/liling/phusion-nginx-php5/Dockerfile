FROM liling/phusion-fundamental:0.9.18.1
MAINTAINER liling@bit.edu.cn

RUN echo 'ssl-cert:x:102:' >> /etc/group ; apt-add-repository ppa:nginx/development ; apt-get update ; apt-get install -y nginx php-pear php5-apcu php5-cli php5-common php5-curl php5-dev php5-fpm php5-gd php5-intl php5-json php5-ldap php5-memcache php5-memcached php5-mongo php5-mysqlnd php5-readline php5-xmlrpc php5-xsl pkg-php-tools ; apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install PHP OCI8
RUN cd /tmp; wget 'https://pecl.php.net/get/oci8-2.0.12.tgz' ; tar xf /tmp/oci8-2.0.12.tgz; cd oci8-2.0.12; phpize; ./configure -with-oci8=shared,instantclient,/usr/lib/oracle/12.1/client64/lib; make; make install; cd /; rm -rf /tmp/oci8*
ADD php_oci8.ini /etc/php5/mods-available/oci8.ini
RUN php5enmod oci8

# Startup Nginx
RUN mkdir /etc/service/nginx
ADD services/nginx.sh /etc/service/nginx/run
RUN chmod +x /etc/service/nginx/run

# Startup php5-fpm
RUN mkdir /etc/service/php5
ADD services/php5-fpm.sh /etc/service/php5/run
RUN chmod +x /etc/service/php5/run

# Allow visit HTTP
EXPOSE 80
