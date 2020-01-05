#
# Nuclos DB based on Postgres 11.2 Dockerfile
#
# https://bitbucket.org/nuccess/docker-nuclos-db

# Pull base image.
FROM library/postgres:11.5

# Optimize DB for Nuclos
ADD postgresql.conf /etc/postgres/postgresql.conf-template

ENV POSTGRES_DB=nuclosdb \
  POSTGRES_USER=nuclos \
  DB_PASSWORD=password \
  LOCALE=de_DE.UTF-8 \
  TZ=Europe/Berlin \
  TOTAL_RAM_GB=1 \
  MAX_CONNECTIONS=50

ADD nuclos-db-run.sh /usr/local/bin
ADD execute-db-cmds.sh /usr/local/bin

ENV EXECUTE_CMD_DIR=/var/nuclos-db
ENV EXECUTE_CMD_BACKUPS_DIR=$EXECUTE_CMD_DIR/backups
ENV EXECUTE_CMD_LOGS_DIR=$EXECUTE_CMD_DIR/logs

# Add VOLUME to allow DDL, backups or restore
VOLUME ["/var/nuclos-db/", "/var/lib/postgresql/data/"]

CMD ["nuclos-db-run.sh"]