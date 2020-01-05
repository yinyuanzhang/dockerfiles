FROM centos:7.2.1511
MAINTAINER zyp
RUN yum -y install vim lsof wget tar bzip2 unzip vim-enhanced passwd sudo yum-utils hostname net-tools rsync man git make automake cmake patch logrotate python-devel libpng-devel libjpeg-devel pwgen python-pip
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
ENV LANG en_US.UTF-8
RUN mkdir /home/app &&\
        wget --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" https://download.oracle.com/otn-pub/java/jdk/8u201-b09/42970487e3af4f5aa5bca3f542482c60/jdk-8u201-linux-x64.tar.gz -P /home/app

RUN tar zxvf /home/app/jdk-8u201-linux-x64.tar.gz -C /home/app
ENV JAVA_HOME /home/app/jdk1.8.0_201
ENV PATH $JAVA_HOME/bin:$PATH