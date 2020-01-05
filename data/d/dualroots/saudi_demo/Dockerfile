FROM centos:6

RUN yum -y update && yum clean all && yum -y upgrade

RUN yum install -y epel-release && yum install -y vim httpd git

RUN git clone https://github.com/dualroots/saudi_demo_app.git /var/www/html/

WORKDIR /var/www/html/

EXPOSE 80

ENTRYPOINT git pull origin master && service httpd restart && bash
