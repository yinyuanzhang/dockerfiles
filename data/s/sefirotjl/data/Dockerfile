FROM busybox:latest
MAINTAINER Jorge Renteria <jorge@renteria.com.mx>

#USER root

RUN mkdir -p /var/lib/mysql && mkdir /var/www/html
#RUN chown -R docker:docker /var/lib/mysql && mkdir /var/www/html
#RUN chmod -R 700 /var/lib/mysql && mkdir /var/www/html

VOLUME ["/var/lib/mysql", "/var/www/html"]

