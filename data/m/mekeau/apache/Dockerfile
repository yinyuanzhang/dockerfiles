FROM centos
MAINTAINER parapracticass@gmail.com

RUN yum -y update && yum clean all && yum -y install httpd && \
yum -y install net-tools && yum clean all

EXPOSE 80

CMD ["/usr/sbin/apachectl", "-D", "FOREGROUND"]
