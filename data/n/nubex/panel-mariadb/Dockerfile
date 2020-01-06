FROM mariadb:10.0

RUN apt-get update \
    && apt-get install -y  vim

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY nubex.cnf /etc/mysql/conf.d

EXPOSE 3306

CMD ["mysqld"]
