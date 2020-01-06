FROM ubuntu:12.04

MAINTAINER smrmkt

# install apache
RUN apt-get update
RUN apt-get install -y apache2

# config env
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACH_PID_FILE /var/run/apache2.pid

# place app
ADD . /var/www

# open port
EXPOSE 80

# launch apache
CMD ["/usr/sbin/apache2", "-D", "FOREGROUND"]

