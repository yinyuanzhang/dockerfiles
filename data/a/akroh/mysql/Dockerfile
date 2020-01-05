FROM akroh/centos:6

MAINTAINER Andrew Kroh (andy@crowbird.com)

RUN yum -y install mysql-server && yum clean all

RUN rm -rf /var/lib/mysql && mkdir -p /var/lib/mysql

VOLUME /var/lib/mysql

COPY docker-entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 3306

CMD ["mysqld"]
