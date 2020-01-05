FROM ubuntu:14.04

RUN apt-get update && \
    apt-get install -y mysql-server-5.6 mysql-client-5.6 vim-nox curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN sed -i -e"s/^bind-address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/" /etc/mysql/my.cnf
RUN rm -rf /var/lib/mysql/*

ADD ./startup.sh /opt/startup.sh
ADD ./fetchdb.sh /bin/fetch-db

EXPOSE 3306

CMD ["/bin/bash", "/opt/startup.sh"]
