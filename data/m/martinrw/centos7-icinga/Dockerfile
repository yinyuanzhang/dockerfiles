FROM centos:7

MAINTAINER Martin Wyett

RUN yum install -y wget \
        && yum install -y epel-release \
        && yum install -y python34-pip \
        && yum install -y python34-devel \
        && yum install -y mysql-devel \
        && yum install -y redhat-rpm-config \
        && yum install -y gcc \
        && yum install -y python34-PyMySQL \
        && yum install -y python34-mysql \
        && yum install -y git \
        && pip3 install requests \
        && pip3 install validators \
        && pip3 install mysql-connector-python \
        && pip3 install mysqlclient

RUN rpm --import http://packages.icinga.org/icinga.key \
        && wget --no-check-certificate https://packages.icinga.org/epel/7/release/noarch/icinga-rpm-release-7-1.el7.centos.noarch.rpm \
        && rpm -i icinga-rpm-release-7-1.el7.centos.noarch.rpm \
        && yum install icinga2 nagios-plugins-all -y
