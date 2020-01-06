FROM centos

MAINTAINER Magecom
# Install required repos, update, and then install PHP-FPM
RUN yum install -y epel-release
RUN yum install -y http://dl.iuscommunity.org/pub/ius/stable/CentOS/7/x86_64/ius-release-1.0-14.ius.centos7.noarch.rpm
RUN yum -y update; yum clean all
RUN yum -y install php70u \
                   php70u-pdo \
                   php70u-mysqlnd \
                   php70u-opcache \
                   php70u-xml \
                   php70u-mbstring \
                   php70u-json \
                   php70u-mcrypt \
                   php70u-gd \
                   php70u-devel \
                   php70u-xmlrpc \
                   php70u-bcmath \
                   php70u-mysql \
                   php70u-pear \
                   php70u-intl \
                   php70u-soap \
                   php70u-fpm \
                   gcc-c++ make git sudo cronie wget openssl-devel mhash which nginx ntp psmisc 
RUN pecl install mongodb
RUN echo "extension=mongodb.so" > /etc/php.d/20-mongo.ini
# Install composer
RUN php -r "readfile('https://getcomposer.org/installer');" | php
RUN mv composer.phar /usr/local/bin/composer
#### Configure and secure PHP
#add scripts
RUN cd /srv && wget https://phar.phpunit.de/phpunit.phar && chmod a+x phpunit.phar && mv phpunit.phar /usr/local/bin/phpunit
ADD start.sh /start.sh
RUN chmod +x /start.sh
ADD nginx.conf /etc/nginx/nginx.conf
RUN sed -i "s/;date.timezone =.*/date.timezone = CET/" /etc/php.ini && \
    sed -i "s/user =.*/user = apache/" /etc/php-fpm.d/www.conf && \
    sed -i "s/group =.*/group = apache/" /etc/php-fpm.d/www.conf && \
    sed -i "s/memory_limit = .*/memory_limit = 2G/" /etc/php.ini && \
    sed -i '/^post_max_size = /cpost_max_size = 40M' /etc/php.ini && \
    sed -i '/^upload_max_filesize = /cupload_max_filesize = 40M' /etc/php.ini && \
    sed -i '/^; max_input_vars = /cmax_input_vars = 100000' /etc/php.ini && \
    sed -i '/^max_input_time = /cmax_input_time = 600' /etc/php.ini && \
    sed -i '/^max_execution_time = /cmax_execution_time = 600' /etc/php.ini && \
    sed -i '/^listen = /clisten = 0.0.0.0:9001' /etc/php-fpm.d/www.conf && \
    sed -i '/^listen.allowed_clients/c;listen.allowed_clients =' /etc/php-fpm.d/www.conf && \ 
    sed -i '/\/var\/lib\/php\/fpm\/session/cphp_value\[session\.save_path\] =\/tmp' /etc/php-fpm.d/www.conf
WORKDIR /var/www
# Set TERM env to avoid error message "TERM environment variable not set"
ENV TERM xterm
#### PORTS
EXPOSE 80
CMD ["/start.sh"]
