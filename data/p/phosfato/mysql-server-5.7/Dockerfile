FROM ubuntu

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update -yq && \
    apt-get upgrade -yq &&  \
    apt-get install -yq mysql-server-5.7 && \
    # remove files left by `apt-get update`
    rm -rf /var/lib/apt/lists/* && \
    mkdir /var/run/mysqld

COPY mysqld.cnf /etc/mysql/mysql.conf.d/mysqld.cnf

VOLUME /var/lib/mysql

STOPSIGNAL SIGTERM

EXPOSE 3306

CMD ["mysqld"]
