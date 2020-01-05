FROM ubuntu:16.04

MAINTAINER "Thierry Onkelinx" thierry.onkelinx@inbo.be

## Install wget
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    wget \
  && apt-get clean

# Add the PostgreSQL PGP key to verify their Debian packages.
# It should be the same key as https://www.postgresql.org/media/keys/ACCC4CF8.asc
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8

# Add PostgreSQL's repository. It contains the most recent stable release
#     of PostgreSQL, ``9.3``.
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ xenial-pgdg main" > /etc/apt/sources.list.d/pgdg.list

# Install ``python-software-properties``, ``software-properties-common`` and PostgreSQL 9.3
#  There are some warnings (in red) that show up during the build. You can hide
#  them by prefixing each apt-get statement with DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
  && apt-get install -y  --no-install-recommends\
    postgresql-9.5 \
    postgresql-client-9.5 \
    postgresql-contrib-9.5

# Add locale
RUN locale-gen nl_BE.UTF-8 \
  && update-locale

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    git

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    default-jre

## get code to setup the database
COPY unittest /unittest
COPY generic /generic

RUN git -c http.sslVerify=false clone https://github.com/inbo/n2kresult.git \
  && cd n2kresult \
  && git checkout datasource \
  && chmod +x ut_update.sh \
  && cd /

# Run the rest of the commands as the ``postgres`` user created by the ``postgres-9.3`` package when it was ``apt-get installed``
USER postgres

## Install liquibase
RUN mkdir ~/liquibase \
  && cd ~/liquibase \
  && wget --no-check-certificate https://github.com/liquibase/liquibase/releases/download/liquibase-parent-3.5.3/liquibase-3.5.3-bin.tar.gz\
  && tar -xzf liquibase-3.5.3-bin.tar.gz \
  && rm liquibase-3.5.3-bin.tar.gz \
  && cd lib \
  && wget https://jdbc.postgresql.org/download/postgresql-9.4.1211.jar \
  && cd ~

# Create a PostgreSQL role named ``docker`` with ``docker`` as the password and
# then create a database `docker` owned by the ``docker`` role.
# Note: here we use ``&&\`` to run commands one after the other - the ``\``
#       allows the RUN command to span multiple lines.
RUN    /etc/init.d/postgresql start \
  && psql --file /unittest/unittest.sql \
  && psql --file /generic/create_schema.sql \
  && cd /n2kresult \
  && ./ut_update.sh \
  && psql --dbname=n2kunittest --command="GRANT TRUNCATE ON ALL TABLES IN SCHEMA public to unittest_analysis;" \
  && cd ~


# Adjust PostgreSQL configuration so that remote connections to the
# database are possible.
RUN echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/9.5/main/pg_hba.conf

# And add ``listen_addresses`` to ``/etc/postgresql/9.3/main/postgresql.conf``
RUN echo "listen_addresses='*'" >> /etc/postgresql/9.5/main/postgresql.conf

# Expose the PostgreSQL port
EXPOSE 5432

# Set the default command to run when starting the container
CMD ["/usr/lib/postgresql/9.5/bin/postgres", "-D", "/var/lib/postgresql/9.5/main", "-c", "config_file=/etc/postgresql/9.5/main/postgresql.conf"]
