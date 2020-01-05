FROM centos:latest

RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm \
 && rpm -Uvh https://rpms.remirepo.net/enterprise/remi-release-7.rpm

# normal updates
RUN yum -y update

# php && httpd
RUN yum -y install php72 php72-php php72-php-opcache php72-php-bcmath php72-php-cli php72-php-common php72-php-gd php72-php-intl php72-php-json php72-php-mbstring php72-php-pdo php72-php-pdo-dblib php72-php-pear php72-php-pecl-mcrypt php72-php-xml php72-php-mysql php72-php-soap php72-php-pecl-zip httpd php72-php-pecl-memcached

# tools
RUN yum -y install epel-release memcached at



# pagespeed
#RUN curl -O https://dl-ssl.google.com/dl/linux/direct/mod-pagespeed-stable_current_x86_64.rpm \
# && rpm -U mod-pagespeed-*.rpm
#RUN chown -R apache:apache /var/log/pagespeed/
#RUN chown -R apache:apache /var/cache/mod_pagespeed/
RUN yum clean all \
 && ln -s /bin/php72 /bin/php

RUN usermod -u 1000 apache && ln -sf /dev/stdout /var/log/httpd/access_log && ln -sf /dev/stderr /var/log/httpd/error_log
RUN unlink /etc/localtime && ln -s /usr/share/zoneinfo/Asia/Bangkok /etc/localtime
RUN mkdir /etc/httpd/sites-enabled


RUN mkdir -p /var/www/html/

COPY mod_deflate.conf /etc/httpd/conf.d/mod_deflate.conf



RUN rm /etc/httpd/conf.d/welcome.conf \
    && sed -i -e "s/Options\ Indexes\ FollowSymLinks/Options\ -Indexes\ +FollowSymLinks/g" /etc/httpd/conf/httpd.conf \
    && sed -i "s/\/var\/www\/html/\/var\/www/g" /etc/httpd/conf/httpd.conf \
    && echo "FileETag None" >> /etc/httpd/conf/httpd.conf \
    && sed -i -e "s/expose_php\ =\ On/expose_php\ =\ Off/g" /etc/opt/remi/php72/php.ini \
    && sed -i -e "s/\;error_log\ =\ php_errors\.log/error_log\ =\ \/var\/log\/php_errors\.log/g" /etc/opt/remi/php72/php.ini \
    && echo "ServerTokens Prod" >> /etc/httpd/conf/httpd.conf \
    && echo "ServerSignature Off" >> /etc/httpd/conf/httpd.conf \
    && echo "IncludeOptional sites-enabled/*.conf" >> /etc/httpd/conf/httpd.conf

EXPOSE 80

CMD ["apachectl", "stop"]
CMD ["httpd", "-D", "FOREGROUND"]

#EXPOSE 80
WORKDIR /var/www/html/