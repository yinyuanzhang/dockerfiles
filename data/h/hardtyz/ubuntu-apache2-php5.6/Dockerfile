FROM ubuntu:16.04

#Install dependencies
 
RUN export LANG=C.UTF-8 && \
    apt-get update -y && \
    apt-get install -y software-properties-common python-software-properties && \
    add-apt-repository -y -u ppa:ondrej/php && \
    apt-get install -y cron supervisor  git apache2 php5.6 php5.6-gd \
    php5.6-cli php5.6-curl php-geoip php-imagick php5.6-imap php5.6-ldap \
    php5.6-mcrypt php5.6-pgsql php5.6-xmlrpc libapache2-mod-php5.6 php5.6-xml \
    php5.6-mbstring php5.6-cgi php5.6-fpm php5.6-soap php5.6-zip \
    php5.6-bcmath php-pear postgresql-client wget unzip composer bzip2 libfontconfig1 libfontconfig1-dev libfreetype6 libfreetype6-dev && \
    wget http://downloads3.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz && \
    tar -xzvf ioncube_loaders_lin_x86-64.tar.gz && \ 
    rm -rf ioncube_loaders_lin_x86-64.tar.gz && \
    export extension_dir=$("php" -r "echo ini_get('extension_dir');") && \
    cp ioncube/ioncube_loader_lin_7.1.so $extension_dir && \
    rm -rf ioncube && \
    echo 'zend_extension = "'$extension_dir'/ioncube_loader_lin_5.6.so"' > /etc/php/5.6/apache2/conf.d/00-ioncube.ini && \
    apt-get remove --purge -y software-properties-common && \
	apt-get autoremove -y && \
	apt-get clean && \
	apt-get autoclean && \
	echo -n > /var/lib/apt/extended_states && \
	rm -rf /var/lib/apt/lists/* && \
	rm -rf /usr/share/man/?? && \
	rm -rf /usr/share/man/??_* && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN composer global require "codeception/codeception" && \
    ln -sf /root/.composer/vendor/bin/codecept /usr/bin/ && \
    pear install channel://pear.php.net/XML_Serializer-0.21.0

RUN a2enmod php5.6 && a2enconf php5.6-fpm && a2enconf php5.6-cgi && a2enmod rewrite && \
    phpenmod mcrypt && \
    mkdir ~/.ssh/

ADD docker/init.sh /init.sh
ADD docker/envvars /etc/apache2/envvars
RUN chmod 755 /*.sh && \
    /bin/bash /etc/apache2/envvars && \
    chmod +x /etc/apache2/envvars

EXPOSE 80
CMD ["/init.sh"]
