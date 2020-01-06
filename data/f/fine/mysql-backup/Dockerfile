FROM centos:7
RUN \cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN yum install -y mysql
RUN mkdir /data
ADD mysql_backup.sh /usr/src/
ADD ./docker-entrypoint.sh /
RUN echo 'Asia/Shanghai' >/etc/timezone
RUN chmod +x /docker-entrypoint.sh
RUN chmod +x /usr/src/mysql_backup.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
