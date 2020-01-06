FROM torstens/letsencrypt-apache-ubuntu
MAINTAINER Torsten Schlabach <tschlabach@gmx.net>

#Install packages as described here http://www.ilias.de/docu/goto_docu_pg_64272_367.html
#no mysql-client and no mysql-server, because they should run in a separate Docker container
RUN apt-get update && apt-get install -y \
	wget \
	zip \
#	apache2 \ #already installed in baseimage
	php7.2 \
	php7.2-gd \
	php7.2-mysql \
	php7.2-curl \
	php7.2-zip \
	php-pear \
#	php-auth \
#	php-auth-http \
	php7.2-xsl \
	htmldoc \
	imagemagick \
	mysql-client \
	sendmail
#	openjdk-7-jdk #not needed most times, install it with apt-get install -y openjdk-7-jdk if you need 

RUN pear install Auth
RUN pear install Auth_HTTP

WORKDIR /data
ADD resources /data/resources/base

#Disable old settings
#RUN sed -i 's/max_execution_time/;max_execution_time/g' /etc/php7.2/apache2/php.ini \
#&& sed -i 's/memory_limit/;memory_limit/g' /etc/php7.2/apache2/php.ini \

#&& sed -i 's/error_reporting/;error_reporting/g' /etc/php7.2/apache2/php.ini \
#&& sed -i 's/display_errors/;display_errors/g' /etc/php7.2/apache2/php.ini \

#&& sed -i 's/post_max_size/;post_max_size/g' /etc/php7.2/apache2/php.ini \
#&& sed -i 's/upload_max_filesize/;upload_max_filesize/g' /etc/php7.2/apache2/php.ini \

#&& sed -i 's/session.gc_probability/;session.gc_probability/g' /etc/php7.2/apache2/php.ini \
#&& sed -i 's/session.gc_divisor/;session.gc_divisor/g' /etc/php7.2/apache2/php.ini \
#&& sed -i 's/session.gc_maxlifetime/;session.gc_maxlifetime/g' /etc/php7.2/apache2/php.ini \
#&& sed -i 's/session.hash_function/;session.hash_function/g' /etc/php7.2/apache2/php.ini \

#&& sed -i 's/allow_url_fopen/;allow_url_fopen/g' /etc/php7.2/apache2/php.ini \

#Insert new settings, as described here http://www.ilias.de/docu/goto_docu_pg_6531_367.html
#&& cat /data/resources/base/phpinisettings >> /etc/php7.2/apache2/php.ini

#Then download ilias, unzip it and restart apache2
RUN wget https://github.com/ILIAS-eLearning/ILIAS/archive/v5.3.5.tar.gz -O /data/resources/base/ilias.tar.gz \
&& tar xzvf /data/resources/base/ilias.tar.gz -C /var/www/html/ \
&& mv /var/www/html/ILIAS-5.3.5 /var/www/html/ilias \
&& rm /data/resources/base/ilias.tar.gz

RUN chown -R www-data:www-data /var/www/html/ilias \
&& mkdir /opt/iliasdata \
&& chown www-data:www-data /opt/iliasdata \
&& chmod 751 /opt/iliasdata \

&& mkdir /data/share \
&& chown www-data:www-data /data/share \
&& chmod 751 /data/share \

&& chown www-data:www-data /data/resources/base/entrypoint.sh \
&& chmod 751 /data/resources/base/entrypoint.sh \

&& chown www-data:www-data /data/resources/base/createiliasdump.sh \
&& chmod 751 /data/resources/base/createiliasdump.sh \
&& chown www-data:www-data /data/resources/base/restoreilias.sh \
&& chmod 751 /data/resources/base/restoreilias.sh \

#Problem in LetsEncrypt when changing the DocumentRoot...
#&& sed -i 's|/var/www/html|/var/www/html/ilias|g' /etc/apache2/sites-enabled/000-default.conf \
#...so we do a http redirect to /ilias
&& rm /var/www/html/index.html \ 
&& echo "<?php header('Location: ilias'); ?>" > /var/www/html/index.php 

ENV apachestartmode="FOREGROUND" \
    createdump="no" \
    restorefromdump="no"

EXPOSE 80 443	
	
ENTRYPOINT ["/data/resources/base/entrypoint.sh"]

