FROM postgres:9.6
MAINTAINER chaya

RUN apt-get update && apt-get install -y curl git-core maven jq

COPY flyway /flyway-bin
RUN chmod -R 755 /flyway-bin

COPY shell/install.sh /docker-entrypoint-initdb.d
COPY shell/docker-entrypoint.sh /docker-entrypoint.sh

COPY shell/configure-as-master.sh /opt
COPY shell/configure-as-slave.sh /opt
COPY shell/configure-security.sh /opt
COPY shell/database-install.sh /opt
COPY shell/pruning.sh /opt

RUN chmod +x /docker-entrypoint-initdb.d/install.sh /opt/configure-as-master.sh /opt/pruning.sh /opt/configure-as-slave.sh /opt/configure-security.sh /opt/database-install.sh docker-entrypoint.sh