FROM centos:7

RUN yum update -y && \
    yum install -y git gcc gcc-c++ make redhat-rpm-config libxml2-devel pkgconfig openssl-devel bzip2-devel curl-devel libpng-devel libjpeg-devel libXpm-devel freetype-devel gmp-devel libmcrypt-devel mariadb-devel aspell-devel recode-devel autoconf bison re2c libicu-devel systemd-devel systemtap-sdt-devel

# ENV container docker
# RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == systemd-tmpfiles-setup.service ] || rm -f $i; done); \
# rm -f /lib/systemd/system/multi-user.target.wants/*;\
# rm -f /etc/systemd/system/*.wants/*;\
# rm -f /lib/systemd/system/local-fs.target.wants/*; \
# rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
# rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
# rm -f /lib/systemd/system/basic.target.wants/*;\
# rm -f /lib/systemd/system/anaconda.target.wants/*;

RUN mkdir /lib/x86_64-linux-gnu/ && ln -s /lib/lib64/libsystemd-daemon.so.0 /lib/x86_64-linux-gnu/libsystemd-daemon.so && ldconfig
ADD build-php /usr/bin/build-php
RUN chmod 755 /usr/bin/build-php

RUN /usr/bin/build-php 7.0.15 && \
    /usr/bin/build-php 7.1.0


