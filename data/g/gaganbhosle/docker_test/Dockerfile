FROM centos
USER root
MAINTAINER Gagan Bhosle "gagan.bhosle@gmail.com"
RUN yum update -y
RUN yum -y install httpd
RUN echo "This is a test for docker_test"> /var/www/html/index.html
EXPOSE 80
CMD ["-D","FOREGROUND"]
ENTRYPOINT ["/usr/sbin/httpd"]
