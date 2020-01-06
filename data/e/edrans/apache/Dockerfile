FROM edrans/centos7

MAINTAINER Nicolás de la Torre <ntorre@edrans.com>

RUN yum install -y httpd php && yum clean all -y

EXPOSE 80

CMD ["apachectl", "-D", "FOREGROUND"]
