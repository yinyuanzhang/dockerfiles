FROM buhuipao/centos7-ssh:v0.1.1

MAINTAINER buhuipao <chenhua22@outlook.com>

RUN yum install epel-release -y &&\
    rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-7.rpm

RUN yum --enablerepo=remi,remi-php70 install -y php-fpm php-common \
        php-opcache php-pecl-apcu php-cli php-pear\
        php-pdo php-mysqlnd php-pecl-memcache php-pecl-memcached\
        php-gd php-mbstring php-mcrypt php-xml php-tokenizer php-openssl

#设置为前台运行，防止退出容器关闭服务
RUN sed -ri 's/^daemonize = yes$/daemonize = no/g' /etc/php-fpm.conf
RUN rm -f /etc/php.ini /etc/php-fpm.d/www.conf

COPY ./php.ini /etc/php.ini
COPY ./www.conf /etc/php-fpm.d/www.conf

RUN echo -e "#!/bin/bash\n/usr/sbin/sshd\n/usr/sbin/php-fpm\nsystemctl enable php-fpm.service" > /root/init.sh
RUN chmod u+x /root/init.sh

EXPOSE 22 9000

CMD ["/root/init.sh"]
