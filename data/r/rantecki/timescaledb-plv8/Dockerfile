FROM ionx/postgres-plv8:10.6
RUN apt-get update && apt-get install -y wget apt-transport-https
RUN sh -c "echo 'deb https://packagecloud.io/timescale/timescaledb/debian/ `lsb_release -c -s` main' > /etc/apt/sources.list.d/timescaledb.list"
RUN wget --quiet -O - https://packagecloud.io/timescale/timescaledb/gpgkey | apt-key add -
RUN apt-get update && apt-get install -y timescaledb-postgresql-10
RUN echo "echo \"shared_preload_libraries = 'timescaledb,plv8'\" >> /var/lib/postgresql/data/postgresql.conf" >> /docker-entrypoint-initdb.d/init-extensions.sh
