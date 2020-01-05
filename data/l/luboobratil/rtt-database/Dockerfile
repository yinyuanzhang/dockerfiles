FROM mysql:5.7

LABEL maintainer.name="Lubo Obratil"
LABEL maintainer.email="lubomir.obratil@gmail.com"
LABEL image.source="https://github.com/LuboO/rtt-database-docker"
LABEL project="https://github.com/crocs-muni/randomness-testing-toolkit"

COPY disable_remote_root_login.sql /docker-entrypoint-initdb.d/
COPY migrate /usr/local/bin/
COPY run_sql /usr/local/bin/

RUN chmod 770 /usr/local/bin/migrate /usr/local/bin/run_sql

COPY migration_order.txt /migration_order.txt
COPY migrations /migrations/

ENV RTT_DATABASE_DB_DATA_DIR=/var/lib/mysql

