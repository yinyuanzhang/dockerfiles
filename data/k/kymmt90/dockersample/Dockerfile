FROM centos:latest
MAINTAINER 0.1 kymmt90@gmail.com
RUN yum -y install httpd
ADD html/ /var/www/html
EXPOSE 80
CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]
