FROM centos:7.2.1511
RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm \
 && rpm -Uvh https://rpms.remirepo.net/enterprise/remi-release-7.rpm
RUN yum -y  update 
RUN yum -y install httpd php php-common php-php php \
        php-pecl-apc \
        php-cli \
        php-pear \
		php-pdo \
        php-mysqlnd \
        php-pgsql \
		php-pecl-mongo \
        php-sqlite \
        php-pecl-memcache \
		php-pecl-memcached \
		php-gd \
        php-mbstring \
        php-mcrypt \
		php-xml \
		php-soap \
		html2ps  
 RUN       chmod -R g+w /var/www/html
 RUN       yum clean all && \
        rm -rf /var/cache/yum 
RUN echo '<?php phpinfo(); ?>' > /var/www/html/index.php
EXPOSE 80 443

CMD /usr/sbin/httpd -c "ErrorLog /dev/stdout" -DFOREGROUND