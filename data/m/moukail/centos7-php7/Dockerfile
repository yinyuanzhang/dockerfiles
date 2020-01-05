FROM centos:7
MAINTAINER Ismail Moukafih <info@moukafih.nl>

ENV NGINX_VER=1.17.6
ENV HTTPD_VER=2.4.41
ENV PHP_72_VER=7.2.25
ENV PHP_73_VER=7.3.12
ENV PHP_74_VER=7.4.0
ENV XDEBUG_VER=2.8.0
ENV PHPREDIS_VER=5.1.1
ENV OAUTH_VER=2.0.3
ENV NODEJS_VER=13.3.0
ENV SSL_VER=1.1.1d
ENV ZEROMQ_VER=4.3.2
ENV AMQP_VER=1.9.4
ARG COLS

RUN yum clean all && yum -y update

RUN yum -y -q install wget mc git nano net-tools make gcc gcc-c++ openssl-devel bison unzip iproute libuuid-devel zlib-devel cronie which
#RUN yum -y install bison-devel apr-devel apr-util-devel
RUN yum -y install libxslt libxslt-devel libxml2 libxml2-devel gd gd-devel pcre-devel
#RUN yum -y install bison-devel apr-devel apr-util-devel GeoIP GeoIP-devel
#sudo yum install -y kernel-devel perl autoconf automake

###################*###################*################# PHP #################*###################*####################
RUN yum -y install libcurl-devel gd-devel libicu-devel epel-release libxslt-devel autoconf file libtool pkgconfig
#  libmcrypt libmcrypt-devel uuid-devel
ADD install_ssh.sh /
RUN chmod +x /install_ssh.sh
RUN /install_ssh.sh ${SSL_VER} ${ZEROMQ_VER} ${COLS}

ADD install_nodejs.sh /
RUN chmod +x /install_nodejs.sh
RUN /install_nodejs.sh ${NODEJS_VER}

ADD install_nginx.sh /
RUN chmod +x /install_nginx.sh
RUN /install_nginx.sh ${NGINX_VER} ${COLS}

ADD install_apache.sh /
RUN chmod +x /install_apache.sh
RUN /install_apache.sh ${HTTPD_VER} ${COLS}

ADD install_php.sh /
RUN chmod +x /install_php.sh

ADD install_php_apache.sh /
RUN chmod +x /install_php_apache.sh

ADD install_php_fpm.sh /
RUN chmod +x /install_php_fpm.sh

ADD install_php_cli.sh /
RUN chmod +x /install_php_cli.sh

ADD install_php_ext.sh /
RUN chmod +x /install_php_ext.sh

RUN /install_php.sh ${PHP_72_VER} 7.2 ${XDEBUG_VER} ${PHPREDIS_VER} ${OAUTH_VER} 1.9.3 ${COLS}
RUN /install_php.sh ${PHP_73_VER} 7.3 ${XDEBUG_VER} ${PHPREDIS_VER} ${OAUTH_VER} ${AMQP_VER} ${COLS}
RUN /install_php.sh ${PHP_74_VER} 7.4 ${XDEBUG_VER} ${PHPREDIS_VER} ${OAUTH_VER} ${AMQP_VER} ${COLS}

RUN  rm -Rf /*.sh /*.log

EXPOSE 80

#ADD public /var/www/site

WORKDIR /moukafih/www
