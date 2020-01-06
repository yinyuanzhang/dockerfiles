FROM mysql/mysql-server:8.0

COPY my.cnf /etc/my.cnf

RUN mkdir -p /etc/mysql/conf.d/ && \
    chmod 0444 /etc/my.cnf
