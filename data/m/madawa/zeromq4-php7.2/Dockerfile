#  
# Author        : madawa lakmal
# Date          : 2018/12/12
# Version       : v1
# Last modifier : -

FROM centos:7
MAINTAINER madawalakmal94@gmail.com

RUN yum clean all

WORKDIR /var/www/html

RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys BF357DD4 \
 && curl -o /usr/local/bin/gosu -SL "https://github.com/tianon/gosu/releases/download/1.9/gosu-amd64" \
 && curl -o /usr/local/bin/gosu.asc -SL "https://github.com/tianon/gosu/releases/download/1.9/gosu-amd64.asc" \
 && gpg --verify /usr/local/bin/gosu.asc \
 && rm /usr/local/bin/gosu.asc \
 && chmod 4755 /usr/local/bin/gosu

RUN yum -y install epel-release http://rpms.remirepo.net/enterprise/remi-release-7.rpm && yum clean all

# install php 7.2.

RUN yum --enablerepo=remi-php72 install php php-devel -y --nogpgcheck && yum clean all

RUN sed -i  "0,/enabled=0/{s/enabled=0/enabled=1/}" /etc/yum.repos.d/remi.repo \
 && sed -i ':a;N;$!ba;s/enabled=0/enabled=1/2' /etc/yum.repos.d/remi.repo

RUN yum install -y httpd vim uuid-devel pkgconfig libtool gcc-c++ wget libsodium make git bash-completion mlocate supervisor --nogpgcheck --skip-broken && yum clean all

RUN echo "IncludeOptional vhost.d/*.conf" >> /etc/httpd/conf/httpd.conf \
 && sed -i "s|User apache|User user|" /etc/httpd/conf/httpd.conf \
 && sed -i "s|Group apache|Group user|" /etc/httpd/conf/httpd.conf \
 && sed -i "s|#ServerName www.example.com:80|ServerName server|" /etc/httpd/conf/httpd.conf \
 && sed -i 's/^\([^#]\)/#\1/g' /etc/httpd/conf.d/welcome.conf

RUN sed -i "s|;date.timezone =|date.timezone = Asia/Colombo|" /etc/php.ini

RUN useradd --shell /bin/bash -u 1000 -o -c "" -m user \
 && usermod -aG apache,root user

RUN sed -i "1ialias ls='ls --color'" /home/user/.bashrc \
 && sed -i "2ialias apachectl='gosu root httpd'" /home/user/.bashrc \
 && sed -i "3ialias yum='gosu root yum'" /home/user/.bashrc

RUN chmod 770 /var/log/httpd

COPY index.php /var/www/html/index.php

#install zeromq

WORKDIR /home/user

RUN wget http://download.zeromq.org/zeromq-4.0.3.tar.gz \
 && tar -xvzf zeromq-4.0.3.tar.gz \
 && cd zeromq-4.0.3 \
 && ./configure \
 && make \
 && make install \
 && echo /usr/local/lib > /etc/ld.so.conf.d/local.conf \
 && ldconfig

#install php bind

RUN git clone git://github.com/mkoppanen/php-zmq.git \
 && cd php-zmq \
 && phpize && ./configure \
 && make \
 && make install \
 && echo "extension=zmq.so" >> /etc/php.ini


COPY supervisord.conf /etc/supervisord.d/supervisord.conf

VOLUME ["/etc/httpd/vhost.d", "/var/www/html", "/etc/httpd/conf", "/etc/httpd/conf.d"]

EXPOSE 80 6379 443

COPY run.sh /run.sh

CMD ["/run.sh"]
