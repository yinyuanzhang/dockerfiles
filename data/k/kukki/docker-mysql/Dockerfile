FROM alpine
MAINTAINER Jimmy Koo <kukkiz@gmail.com>

ENV MYSQL_PASS f#k3Pa55w0Rd

RUN apk add --update mysql mysql-client

WORKDIR /

ADD initdb.sh /initdb.sh
ADD start.sh /start.sh
ADD my.cnf /etc/mysql/my.cnf

RUN mkdir -p /etc/mysql/conf.d && \
    chown -R mysql:mysql /var/lib/mysql && \
    chmod 755 /*.sh 

VOLUME ["/etc/mysql/conf.d", "/var/lib/mysql" ]

EXPOSE 3306

CMD ["/start.sh"]
