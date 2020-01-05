
FROM centos:6.6
MAINTAINER Larry Liang <ptolemy428@gmail.com>

RUN yum -y update; yum clean all
RUN yum -y install epel-release; yum clean all
RUN yum -y install python-pip; yum clean all

RUN pip install boto

WORKDIR /root/src
