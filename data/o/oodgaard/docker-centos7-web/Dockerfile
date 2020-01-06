############################################################
# Dockerfile to build CentOS 7 - Nginx + PHP-FPM (php 5.6)
# and clients for pgsql, mongodb, memcache, xdebug, yaml
############################################################

FROM centos:7

# File Author / Maintainer
MAINTAINER Otto Odgaard <oodgaard@ultraserve.com.au>

# Add the ngix and PHP dependent repository
ADD nginx.repo /etc/yum.repos.d/nginx.repo

# Add repos to get php 5.6 from
RUN rpm -Uvh https://mirror.webtatic.com/yum/el7/epel-release.rpm
RUN rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm

# Enable the MongoDB repo
ADD mongodb.repo /etc/yum.repos.d/mongodb.repo

RUN yum -y update

# Installing nginx
RUN yum -y install nginx

# Installing PHP
RUN yum -y install php56w-opcache php56w-fpm php56w-pear php56w-pecl-memcache php56w-pgsql php56w-process php56w-soap php56w-xml
RUN yum -y install libmongo-devel libyaml-devel php56w-devel mongodb-org-mongos php56w-pecl-xdebug

# Install minimum devleopment tools
RUN yum -y install gcc gcc-c++ automake make gmake openssl-devel

# Install mongo and yaml php extentions
RUN pecl channel-update pecl.php.net
RUN printf "\r" | pecl install --force mongo
RUN pecl install yaml

ADD mongo.ini /etc/php.d/
ADD yaml.ini /etc/php.d/

# Create PHPs default session directory
RUN mkdir /var/lib/php/session
RUN chmod 1777 /var/lib/php/session

# Installing supervisor
RUN yum install -y python-setuptools && yum clean all
RUN easy_install pip
RUN pip install supervisor

# Adding the configuration file for nginx
ADD nginx.conf /etc/nginx/nginx.conf

# Adding the configuration file of the Supervisor
ADD supervisord.conf /etc/

# Mounted from the Host
VOLUME ["/var/www", "/etc/php.ini", "/etc/hosts", "/etc/resolv.conf"]

# Executing supervisord
CMD ["supervisord", "-n"]
