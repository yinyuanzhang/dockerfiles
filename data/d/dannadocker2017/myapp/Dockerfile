FROM centos
MAINTAINER Danna
RUN yum install httpd -y
RUN echo 'Myapp v1' > /var/www/html/index.html
RUN echo '20170310' > /var/www/html/index.html
EXPOSE 80
CMD ["/user/sbin/httpd", "-D", "FOREGROUND"]
