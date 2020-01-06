FROM centos:6

RUN yum -y update && yum clean all && yum -y upgrade

RUN yum install -y epel-release && yum install -y vim httpd git

EXPOSE 80

ENTRYPOINT service httpd restart && bash
