FROM centos
MAINTAINER Johnsonwang
RUN yum install httpd -y
RUN yum clean all
RUn echo 'myapp v2' > /var/www/html/index.html
EXPOSE 80
CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]
