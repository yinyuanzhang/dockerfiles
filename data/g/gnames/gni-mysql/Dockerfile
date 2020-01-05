FROM debian:squeeze
MAINTAINER Dmitry Mozzherin
ENV LAST_FULL_REBUILD 2015-11-30

RUN groupadd -f -g 301 -r mysql && \
    useradd -u 301 -g 301 -r -d "/nonexistent" -M -s "/bin/false" mysql && \
    apt-get update && \
    apt-get -yq install mysql-server-5.1 pwgen vim-nox procps && \
    mkdir -p /opt/gni/backup && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /var/lib/mysql/*

# Exposed ENV
ENV MYSQL_USER admin
ENV MYSQL_PASS **Random**

VOLUME /var/log
VOLUME /var/lib/mysql
VOLUME /etc/mysql
EXPOSE 3306

COPY files/start.sh /start.sh
COPY files/stop.sh /stop.sh
COPY files/create-gni-db.sh /create-gni-db.sh
COPY files/my.cnf /etc/mysql/my.cnf
CMD ["/start.sh"]
