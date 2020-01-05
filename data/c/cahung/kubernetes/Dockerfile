FROM centos:centos7

RUN yum install -y httpd && \
    yum install -y vim

EXPOSE 8080

#ADD listport.conf /etc/httpd/conf.d/listport.conf

CMD ["/usr/sbin/httpd", "-DFOREGROUND"]


