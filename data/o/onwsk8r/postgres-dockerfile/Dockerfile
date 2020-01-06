FROM centos:7

LABEL maintainer="onwsk8r@gmail.com" \
      description="Run Postgres 10"

# PGDATA: Set to CentOS default data directory
# PGBINDIR: Set to CentOS default directory to install PG binaries
# PGCTLTIMEOUT: How long to wait for PG to shut down, adjust -t accordingly in `docker stop`
# NOBACKCOMPAT: Whether to use PG 10 only features such as SCRAM SHA256 PW encryption
ENV PGDATA=/var/lib/pgsql/10/data \
    PGBINDIR=/usr/pgsql-10/bin \
    PGCTLTIMEOUT=8 \
    NOBACKCOMPAT=0

HEALTHCHECK --interval=3s --timeout=1s CMD usr/pgsql-10/bin/pg_isready
# How to stop Postgres
# - SIGTERM (Docker default) waits for clients to disconnect and shuts down
#   cleanly. **Make sure to adjust the Docker stop timeout accordingly**
# - SIGINT terminates connections immediately and shuts down cleanly
# - SIGKILL shuts down immediately and UNCLEANLY.
# STOPSIGNAL SIGINT
EXPOSE 5432

# List of packages at
# https://download.postgresql.org/pub/repos/yum/10/redhat/rhel-7-x86_64/
RUN yum -y install https://download.postgresql.org/pub/repos/yum/10/redhat/rhel-7-x86_64/pgdg-centos10-10-2.noarch.rpm epel-release && \
    yum -y update && \
    yum -y install postgresql10-{contrib,server} pgbson10 postgis_24_10

USER postgres:postgres
COPY *.sh /usr/bin/
ENTRYPOINT "/usr/bin/entrypoint.sh"
