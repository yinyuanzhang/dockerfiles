FROM hurrigan/debian:8.4

MAINTAINER David Calvert <dockerhub@hurrigan.com>

ENV MYSQL_ROOT_PASSWORD yourpassword

USER root

COPY files/ /

RUN apt-get update && \
    apt-get install -y ca-certificates mariadb-server percona-xtrabackup && \
    rm -rf /var/lib/apt/lists/* && \
    chmod +x /usr/local/bin/run.sh

EXPOSE 3306

VOLUME [ "/var/lib/mysql" ]

CMD [ "run.sh" ]
