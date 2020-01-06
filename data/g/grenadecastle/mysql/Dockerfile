FROM mariadb:10.4

RUN        touch /var/log/mysql/mariadb-slow.log \
        && touch /var/log/mysql/mariadb.err \
        && chown mysql:adm /var/log/mysql/mariadb.err \
        && chown mysql:adm /var/log/mysql/mariadb-slow.log \
        && chown mysql:adm /var/log/mysql \
        && chown root:root /var/log \
        && chmod 0640 /var/log/mysql/mariadb.err \
        && chmod 0640 /var/log/mysql/mariadb-slow.log \
        && chmod 0750 /var/log/mysql \
        && chmod 0775 /var/log \
        && chmod 0755 /var

RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /tmp/*