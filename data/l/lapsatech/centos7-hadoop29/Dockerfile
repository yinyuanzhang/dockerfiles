FROM lapsatech/centos7-oracle-jdk8:latest
MAINTAINER "Vadim Isaev" <vadim.o.isaev@gmail.com>

RUN mkdir /opt/hadoop-alt/
WORKDIR /opt/hadoop-alt/

RUN curl -L -C - -O http://apache-mirror.rbc.ru/pub/apache/hadoop/common/hadoop-2.9.1/hadoop-2.9.1.tar.gz && tar xvf hadoop-2.9.1.tar.gz
RUN ln -s hadoop-2.9.1 latest
RUN ln -s latest default
WORKDIR /opt/
RUN ln -s hadoop-alt/default hadoop

COPY hadoop.sh /etc/profile.d/
RUN yum install -y which vim; yum clean all

RUN mkdir /data
