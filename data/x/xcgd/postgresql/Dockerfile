FROM xcgd/ubuntu4base:xenial
MAINTAINER florent.aide@xcg-consulting.fr 

ADD files /

# Add the PostgreSQL PGP key to verify their Debian packages.
RUN apt-key add /var/tmp/ACCC4CF8.asc && rm /var/tmp/ACCC4CF8.asc

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -yq install locales

ENV LANG en_US.UTF-8

RUN DEBIAN_FRONTEND=noninteractive apt-get -yq install postgresql-9.6 postgresql-contrib-9.6 --no-install-recommends

# stop and clear the database as it is init or mounted on container runtime
RUN pg_dropcluster --stop 9.6 main

ADD --chown=postgres:postgres files-postgres/etc/postgresql /etc/postgresql

# Execution environment

VOLUME ["/var/log/postgresql", "/var/lib/postgresql", "/etc/postgresql"]
# Set the default entrypoint to run when starting the container
ENTRYPOINT ["/usr/local/bin/boot"]
# Expose the PostgreSQL port (not to be exposed to the outside world)
EXPOSE 5432
