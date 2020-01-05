FROM centos:7
MAINTAINER Syo Igarashi syonet

ENV IP 192.168.50.50
EXPOSE 8080 443

RUN yum clean all -y
RUN yum update -y
RUN yum upgrade -y
RUN yum install --nogpgcheck git cmake gcc-c++ tar make libXpm-devel freetype-devel gcc bzip2 autoconf -y

RUN rpm -ivh http://ftp.riken.jp/Linux/fedora/epel/7/x86_64/e/epel-release-7-5.noarch.rpm

RUN yum install -y --enablerepo=epel ncurses-devel libxml2 libxml2-devel openssl-devel curl-devel libjpeg libjpeg-devel libpng libpng-devel libmcrypt libmcrypt-devel readline-devel libtidy libtidy-devel libxslt libxslt-devel


#RUN git clone https://github.com/h2o/h2o \
#    && cd h2o \
#    && cmake . \
#    && make h2o \
#    && make install
#    && cd

#COPY h2o.conf /root/h2o/h2o.conf
#RUN h2o -v
RUN pwd
RUN ls -al /root
RUN rm -rf /root/.phpenv


RUN git clone git://github.com/CHH/phpenv.git /root/phpenv \
    && /root/phpenv/bin/phpenv-install.sh

RUN git clone git://github.com/CHH/php-build.git /root/.phpenv/plugins/php-build

ENV PATH $PATH:/root/.phpenv/bin
RUN phpenv -v

RUN phpenv install 7.0.0
RUN phpenv global 7.0.0
RUN phpenv rehash
#RUN php -v
