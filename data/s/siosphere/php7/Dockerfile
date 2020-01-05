FROM centos:7

RUN yum install -y epel-release && \
    rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm && \
    yum update -y && \
    yum install -y which git gcc make php70w php70w-devel php70w-opcache php70w-bcmath php70w-gd php70w-mbstring php70w-mysqlnd php70w-mcrypt php70w-pecl-imagick php70w-soap zeromq zeromq-devel zlib-devel libmemcached-devel && \
    yes '' | pecl install -f zmq-beta

WORKDIR /root/

RUN git clone https://github.com/php-memcached-dev/php-memcached && \
    cd php-memcached && \
    git checkout -b php7 origin/php7 && \
    yes '' | phpize && ./configure && yes '' | make && make install && \
    rm -f /etc/php.d/memcached.ini

COPY ./conf/memcached.ini /etc/php.d/50-memcached.ini
COPY ./conf/zmq.ini /etc/php.d/zmq.ini

RUN ln -sf /dev/stdout /var/log/httpd/access_log && \
    ln -sf /dev/stderr /var/log/httpd/error_log

CMD httpd -DFOREGROUND
