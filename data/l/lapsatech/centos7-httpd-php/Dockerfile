FROM centos:7
MAINTAINER "Vadim Isaev" <vadim.o.isaev@gmail.com>

RUN yum update -y && \
    yum clean all && rm -rf /var/cache/yum

RUN yum install -y \
        httpd php mod_ssl && \
    yum clean all && rm -rf /var/cache/yum

COPY httpd-start.sh /
RUN chmod +x /httpd-start.sh
ENTRYPOINT ["/httpd-start.sh"]

WORKDIR /var/www/html/
RUN rm -rf *
COPY index.php index.php
