FROM centos:6.6
MAINTAINER base env <kitsudo163@163.com>
RUN yum -y update && yum install -y wget tar perl m4 gcc-c++ unixODBC-devel openssl-devel ncurses-devel && yum clean all
RUN wget http://erlang.org/download/otp_src_18.2.tar.gz && tar xvf otp_src_18.2.tar.gz && cd otp_src_18.2 && ./configure --enable-hipe --enable-threads --enable-smp-support --enable-kernel-poll --without-javac && make && make install && rm -fr /otp_src_18.2*
