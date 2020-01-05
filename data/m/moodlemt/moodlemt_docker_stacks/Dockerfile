FROM moodlemt/moodlemt_docker_stacks:apache24
MAINTAINER Manuel Peño <mpenobarrio@gmail.com>

ENV REFRESHED_AT 2018-10-04_16-26

RUN yum -y install yum-utils; yum clean all

# 1. Installs PHP 5.6 (centos6 default repo comes with 5.3)
WORKDIR /tmp
# 1.1. Repo EPEL
RUN \
	wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm && \
	yum -y install epel-release-latest-7.noarch.rpm
# 1.2. Repo REMI
RUN \
	wget http://rpms.famillecollet.com/enterprise/remi-release-7.rpm && \
	rpm -Uvh remi-release-7.rpm

RUN yum-config-manager --enable remi-php71
RUN yum -y --enablerepo=remi,remi-php71 install php; yum clean all
RUN yum -y --enablerepo=remi,remi-php71 install mod_php php-gd php-mysql php-mcrypt; yum clean all
RUN yum -y --enablerepo=remi,remi-php71 install php-mbstring php-xmlrpc php-soap php-intl php-zip; yum clean all
RUN yum -y --enablerepo=remi,remi-php71 install php-opcache; yum clean all
RUN sed -i 's/opcache.enable=1/opcache.enable=0/g' /etc/php.d/*opcache.ini

# 2. Installs MySQL community client 5.6 (centos6 default repo comes with 5.1)
RUN wget http://repo.mysql.com/mysql57-community-release-el7-11.noarch.rpm -O /tmp/mysql-com.rpm
RUN rpm -ivh /tmp/mysql-com.rpm ; rm -rf /tmp/mysql-com.rpm
RUN yum-config-manager --disable mysql5* ; yum-config-manager --enable mysql56-community
RUN yum -y install mysql-community-client

# 3. Common log files creation with permission
RUN mkdir -p /var/log/httpd && mkdir -p /var/log/php
RUN touch /var/log/httpd/access_log && touch /var/log/httpd/error_log && touch /var/log/httpd/ssl_request_log
RUN touch /var/log/php/php.log
RUN chown -R apache:root /var/log/httpd/* && chown -R apache:root /var/log/php/* && chmod -R 770 /var/log/httpd/* && chmod -R 770 /var/log/php/*

# 4. Installs Xdebug
RUN yum -y --enablerepo=remi,remi-php71 install php-pear php-devel; yum clean all
RUN yum -y --enablerepo=remi,remi-php71 install gcc curl-devel zlib-devel pcre-devel; yum clean all
RUN pecl install xdebug-2.6.0

## 5. Enables XDebug and PHP specific directives for logging if variable ENABLE_DEVEL is set to 'yes'
ARG ENABLE_DEVEL='no'
ADD confs/90-xdebug.ini.hidden /etc/php.d/90-xdebug.ini.hid
ADD confs/php71.ini /etc/php71.ini
ADD confs/php71debug.ini /etc/php71debug.ini
ADD docker-entrypoint.sh /entrypoint.sh
RUN chmod -v +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

# 6. Installs Grunt for developing amd, css, etc. in Moodle
# La siguiente linea actualiza al repositorio de la ultima verion 8 que haya (si alguna vez queremos pasar a version 10, usar https://rpm.nodesource.com/setup_10.x)
RUN curl -SsL https://rpm.nodesource.com/setup_8.x | bash
# En la version nodejs 8 el npm ya viene incorporado, por lo que no hace falta especificar 'npm' en el yum
RUN yum -y install nodejs
RUN npm set strict-ssl false
RUN npm install -g grunt-cli

# CMD inherited from apache
CMD ["/run-httpd.sh"]
