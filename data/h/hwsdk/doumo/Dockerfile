# vim:set ft=dockerfile:
FROM centos:6

COPY ./CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo

RUN yum -y update \
    && yum -y upgrade \
    && yum -y install epel-release \
    && sed -e 's!^mirrorlist=!#mirrorlist=!g' \
         -e 's!^#baseurl=!baseurl=!g' \
         -e 's!//download\.fedoraproject\.org/pub!//mirrors.ustc.edu.cn!g' \
         -e 's!http://mirrors\.ustc!https://mirrors.ustc!g' \
         -i /etc/yum.repos.d/epel.repo /etc/yum.repos.d/epel-testing.repo \
    && yum -y install yum-utils vim-enhanced tmux \
    && yum clean all \
    && rm -fr /tmp/*

RUN yum -y update \
    && yum -y install ncurses-devel libxml2-devel libuuid-devel libidn-devel protobuf-devel centos-release-scl lua-static tolua++-devel jansson-devel libcurl-devel jsoncpp-devel \
    && yum -y groupinstall "Development tools" \
    && yum clean all \
    && rm -fr /tmp/*

RUN yum -y update \
    && yum -y install python27 \
    && ln -sf /opt/rh/python27/root/usr/lib64/libpython2.7.so /usr/lib/libpython2.7.so \
    && yum clean all \
    && rm -fr /tmp/*

#RUN cd /tmp \
#    && curl https://cdn.mysql.com/archives/mysql-5.0/mysql-5.0.96.tar.gz -O \
#    && tar xf mysql-5.0.96.tar.gz \
#    && cd mysql-5.0.96 \
#    && ./configure --prefix=/usr/local \
#        --with-charset=utf8 \
#        --with-collation=utf8_general_ci \
#        --with-extra-charsets=complex \
#        --enable-assembler \
#        --with-pthread \
#        --enable-thread-safe-client \
#    && make -j3 \
#    && make install \
#    && rm -fr /tmp/*
RUN rpm -ivh https://dev.mysql.com/get/mysql80-community-release-el6-1.noarch.rpm \
    && yum-config-manager --disable mysql80-community \
    && yum-config-manager --enable mysql57-community \
    && yum -y update \
    && yum -y install mysql mysql-devel \
    && yum clean all \
    && rm -fr /tmp/*

RUN cd /tmp \
    && git clone https://github.com/fredericgermain/LeakTracer.git \
    && cd LeakTracer \
    && sed -i 's&/usr/bin/ls&/bin/ls&g' Makefile \
    && make \
    && make install PREFIX=/usr/local \
    && rm -fr /tmp/*

COPY bashrc /root/.bashrc
COPY tmux.conf /root/.tmux.conf

WORKDIR /work
#ENTRYPOINT [ "/usr/bin/scl", "enable", "python27", "/bin/bash" ]
