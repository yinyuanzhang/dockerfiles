FROM edrans/centos7

MAINTAINER Nicolás de la Torre <ntorre@edrans.com>

RUN yum install mariadb-server -y && yum clean all -y && mkdir -p /data/mariadb
ADD my.cnf /etc/my.cnf
RUN chmod 664 /etc/my.cnf
ADD run.sh /run.sh

VOLUME ["/data/mariadb"]
EXPOSE 3306
CMD ["/run.sh"]
