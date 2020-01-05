FROM centos:7 
MAINTAINER chlzzz <chlzzz@naver.com>

RUN yum -y install httpd; yum clean all; systemctl enable httpd.service 
RUN echo 'Hello Apache & Docker' > /var/www/html/index.html 

EXPOSE 80 443 

CMD ["/usr/sbin/init"]
