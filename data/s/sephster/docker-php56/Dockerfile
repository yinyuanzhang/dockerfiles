FROM centos:7
MAINTAINER Andrew Millington "a.j.millington@abdn.ac.uk"
ENV REFRESHED_AT 2017-10-02

ADD ./oracle-instantclient12.1-basic-12.1.0.2.0-1.x86_64.rpm /tmp/oracle-instantclient12.1-basic-12.1.0.2.0-1.x86_64.rpm
ADD ./oracle-instantclient12.1-devel-12.1.0.2.0-1.x86_64.rpm /tmp/oracle-instantclient12.1-devel-12.1.0.2.0-1.x86_64.rpm

RUN yum install -y /tmp/oracle-instantclient12.1-basic-12.1.0.2.0-1.x86_64.rpm
RUN yum install -y /tmp/oracle-instantclient12.1-devel-12.1.0.2.0-1.x86_64.rpm

ENV LD_LIBRARY_PATH=/usr/lib/oracle/12.1/client64/lib/
ENV ORACLE_HOME=/usr/lib/oracle/12.1/client64/lib/

RUN yum update -y 
RUN yum install httpd mod_ssl wget epel-release -yq
RUN wget http://rpms.famillecollet.com/enterprise/remi-release-7.rpm
RUN rpm -Uvh remi-release-7*.rpm
RUN yum-config-manager --enable remi-php56
RUN yum update -y
RUN yum install php \
				php-mysqlnd \
				php-bcmath \
				php-xml \
				php-gd \
				php-imap \
				php-ldap \
				php-mbstring \
				php-mcrypt \ 
				php-mssql \
				php-pdo \
				php-opcache \
				php-soap \
				php-devel \
				gcc \ 
				gcc-c++ \
				autoconf \
				automake \
				php-pear \
                php-redis \
				php-oci8 -y
RUN pecl install Xdebug

# Add the oracle library to apache
RUN echo 'LD_LIBRARY_PATH=/usr/lib/oracle/12.1/client64/lib' >> /etc/sysconfig/httpd

# Turn off EnableSendFile in httpd.conf
RUN sed -i 's/EnableSendfile on/EnableSendfile off/g' /etc/httpd/conf/httpd.conf

# Allow the .htaccess file to override Apache settings
RUN sed -i 's/AllowOverride None/AllowOverride All/g' /etc/httpd/conf/httpd.conf

# Create HTTPS certs
RUN openssl genrsa -out ca.key 2048
RUN openssl req -new -nodes -subj "/C=UK/ST=Aberdeenshire/L=Aberdeen/O=AccApps/CN=abdn.ac.uk" -key ca.key -out ca.csr
RUN openssl x509 -req -days 365 -in ca.csr -signkey ca.key -out ca.crt
RUN cp ca.crt /etc/pki/tls/certs
RUN cp ca.key /etc/pki/tls/private/ca.key
RUN cp ca.csr /etc/pki/tls/private/ca.csr
RUN sed -i 's/SSLCertificateFile \/etc\/pki\/tls\/certs\/localhost.crt/SSLCertificateFile \/etc\/pki\/tls\/certs\/ca.crt/g' /etc/httpd/conf.d/ssl.conf
RUN sed -i 's/SSLCertificateKeyFile \/etc\/pki\/tls\/private\/localhost.key/SSLCertificateKeyFile \/etc\/pki\/tls\/private\/ca.key/g' /etc/httpd/conf.d/ssl.conf

# Install Composer
RUN wget https://getcomposer.org/installer && php installer && php composer.phar && mv composer.phar /usr/local/bin/composer
ENV COMPOSER_HOME=/usr/local/composer 

# Install PHP Code Sniffer
RUN composer global require "squizlabs/php_codesniffer=*"
ENV PATH=/usr/local/composer/vendor/bin/:${PATH}

# Copy the php ini file
COPY ./php.ini /etc/

EXPOSE 80
EXPOSE 443
EXPOSE 1521

# Simple startup script to avoid some issues observed with container restart 
ADD run-httpd.sh /run-httpd.sh
RUN chmod -v +x /run-httpd.sh

CMD ["/run-httpd.sh"]
