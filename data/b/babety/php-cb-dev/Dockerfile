FROM centos:7
RUN yum update -y && \
    yum install -y epel-release

RUN yum install -y wget
RUN wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo && \
    wget -O /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-7.repo && \
    yum clean all && \
    yum makecache
#php版本号
ENV PHP_VERSION=php72

RUN yum install -y http://rpms.remirepo.net/enterprise/remi-release-7.rpm && \
    yum install -y yum-utils && \
    yum-config-manager --enable remi-${PHP_VERSION} && \
    yum -y update


RUN yum install -y supervisor sudo

RUN yum install -y php php-fpm php-gd php-json php-mbstring php-mysqlnd php-xml php-xmlrpc php-opcache php-zip


RUN useradd -M -d /opt/app -s /bin/false www
RUN mkdir -p /opt/app && \
    chown www:www /opt/app

RUN usermod -u 2000 www
RUN groupmod -g 2000 www

RUN mkdir -p /run/php-fpm && \
    chown www:www /run/php-fpm

RUN mkdir -p /var/lib/php/session && \
    chown www:www /var/lib/php/session

RUN yum clean all

#VOLUME /app/service

#EXPOSE 9000

COPY php-fpm-conf /etc/php-fpm-conf
COPY supervisord-php-fpm.ini /etc/supervisord.d/supervisord-php-fpm.ini

CMD ["/usr/bin/supervisord"]

### 以下为项目扩展


RUN cd /tmp && \
    curl -sS https://getcomposer.org/installer | php && \
    mv composer.phar /usr/bin/composer

#RUN yum install -y php-mbstring
#
ENV COMPOSER_PHP_PACKAGES_ACCOUNT=CaiBeiTV
ENV COMPOSER_PHP_PACKAGES_PASSWORD=X0EeuAOM
ENV COMPOSER_DEPEND_PHP_PACKAGES_ACCOUNT=CaiBeiTV
ENV COMPOSER_DEPEND_PHP_PACKAGES_PASSWORD=X0EeuAOM
ENV COMPOSER_GIT_CAIBEITV_COM_ACCOUNT=zhipeng@66plat.com
ENV COMPOSER_GIT_CAIBEITV_COM_PASSWORD=844FcoEIUg4v

RUN sudo -u www composer config --global repositories.caibeitv composer https://php-packages.caibeitv.com && \
    sudo -u www composer config --global --auth http-basic.php-packages.caibeitv.com ${COMPOSER_PHP_PACKAGES_ACCOUNT} ${COMPOSER_PHP_PACKAGES_PASSWORD} && \
    sudo -u www composer config --global repo.caibeitv_depend composer https://depend-php-packages.caibeitv.com && \
    sudo -u www composer config --global --auth http-basic.depend-php-packages.caibeitv.com ${COMPOSER_DEPEND_PHP_PACKAGES_ACCOUNT} ${COMPOSER_DEPEND_PHP_PACKAGES_PASSWORD} && \
    sudo -u www composer config --global --auth http-basic.git.caibeitv.com ${COMPOSER_GIT_CAIBEITV_COM_ACCOUNT} ${COMPOSER_GIT_CAIBEITV_COM_PASSWORD}

# 66plat.com
RUN sudo -u www composer config --global repositories.bala composer https://composer.66plat.com && \
    sudo -u www composer config --global repositories.packagist composer https://composer-depend.66plat.com

COPY shells /root/shells


