FROM inbobmk/r-3.2.3:develop

## This handle reaches Thierry
MAINTAINER "Thierry Onkelinx" thierry.onkelinx@inbo.be

# Add the PostgreSQL PGP key to verify their Debian packages.
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8

# Add PostgreSQL's repository. It contains the most recent stable release
#     of PostgreSQL, ``9.3``.
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" > /etc/apt/sources.list.d/pgdg.list

## Install postgresql
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    postgresql=9.3+154ubuntu1 \
    postgresql-client-9.3=9.3.10-1.pgdg12.4+1 \
    postgresql-contrib-9.3=9.3.10-1.pgdg12.4+1 \
    odbc-postgresql=1:09.02.0100-2ubuntu1

# Run the rest of the commands as the ``postgres`` user created by the ``postgres-9.3`` package when it was ``apt-get installed``
USER postgres

# Create a PostgreSQL role named ``docker`` with ``docker`` as the password and
# then create a database `n2kresult` owned by the ``docker`` role.
RUN /etc/init.d/postgresql start \
  && psql --command "CREATE USER docker WITH SUPERUSER PASSWORD 'docker';" \
  && createdb -O docker n2kresult

# Adjust PostgreSQL configuration so that remote connections to the
# database are possible.
RUN echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/9.3/main/pg_hba.conf

# And add ``listen_addresses`` to ``/etc/postgresql/9.3/main/postgresql.conf``
RUN echo "listen_addresses='*'" >> /etc/postgresql/9.3/main/postgresql.conf

# Expose the PostgreSQL port
EXPOSE 5432

# Add VOLUMEs to allow backup of config, logs and databases
VOLUME  ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]

## Start R
CMD ["R", "--no-save", "--no-restore"]
