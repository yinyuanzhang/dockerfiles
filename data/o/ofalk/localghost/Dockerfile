FROM docker.io/centos

MAINTAINER Oliver Falk <oliver@linux-kernel.at>

RUN ln -sf /dev/stdout /var/log/messages
RUN yum -y install httpd php bash; yum clean all; systemctl enable httpd.service
RUN mkdir -p /var/www/html
COPY html /var/www/html
EXPOSE 80
CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]
