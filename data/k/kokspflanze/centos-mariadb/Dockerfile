FROM centos:latest

MAINTAINER "KoKsPfLaNzE" <kokspflanze@protonmail.com>

ENV container docker

# we want some config changes
COPY config/MariaDB.repo /etc/yum.repos.d/

# normal updates
RUN yum -y update

# tools
RUN yum -y install MariaDB-server MariaDB-client

EXPOSE 3306

RUN systemctl enable mariadb

CMD ["/usr/sbin/init"]