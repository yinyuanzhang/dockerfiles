FROM centos:latest
MAINTAINER Jérôme JURE

#RUN echo "proxy=http://10.9.22.205:808/" >> /etc/yum.conf

RUN yum -y --setopt=tsflags=nodocs update && \
    yum -y --setopt=tsflags=nodocs install httpd && \
    yum -y --setopt=tsflags=nodocs install php && \
    yum clean all

COPY www/ /var/www/html/

RUN sed -i 's/Listen 80/Listen 8080/g' /etc/httpd/conf/httpd.conf

RUN sed -i 's/#ServerName www.example.com:80/ServerName localhost:8080/g' /etc/httpd/conf/httpd.conf

RUN sed -i 's/DirectoryIndex index.html/DirectoryIndex index.php/g' /etc/httpd/conf/httpd.conf

CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]

EXPOSE 8080
