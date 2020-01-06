FROM centos:latest
MAINTAINER dayreiner

ENV MARIADB_MAJOR=10.1

# MariaDB Repo
COPY config/MariaDB.repo /etc/yum.repos.d/MariaDB.repo

# Install required packages and MariaDB Vendor Repo
RUN yum -y update && yum clean all && yum -y install epel-release && \
    rpm --import https://yum.mariadb.org/RPM-GPG-KEY-MariaDB && \
    groupadd -g 250 -r mysql && useradd -u 250 -r -g mysql mysql && \
    yum -y install MariaDB-server MariaDB-client galera less which socat pwgen && yum clean all && \
    mkdir /docker-entrypoint-initdb.d

RUN rm -rf /var/lib/mysql && mkdir /var/lib/mysql

COPY config/server.cnf /etc/my.cnf.d/server.cnf
COPY scripts/docker-entrypoint.sh /docker-entrypoint.sh

EXPOSE 3306
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["mysqld"]
