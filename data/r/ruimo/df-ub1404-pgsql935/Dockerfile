FROM ubuntu:14.04
MAINTAINER Shisei Hanai<ruimo.uno@gmail.com>

RUN apt-get update
RUN apt-get -y install build-essential wget
RUN sudo apt-get install -y libreadline-dev build-essential zlib1g-dev

RUN cd /tmp && wget http://ftp.postgresql.org/pub/source/v9.3.5/postgresql-9.3.5.tar.bz2
RUN cd /tmp && tar xf postgresql-9.3.5.tar.bz2
RUN cd /tmp/postgresql-9.3.5 && \
  ./configure && \
  make && \
  make install
RUN cd /tmp/postgresql-9.3.5/contrib/pg_trgm && \
  sed -i 's;^\(\s*#define\s*KEEPONLYALNUM.*\)$;/* \1 */;' trgm.h && \
  make && \
  make install
RUN rm -r /tmp/postgresql-9.3.5
RUN useradd --shell /bin/false -d /var/home postgres
# Define mountable directories.
RUN mkdir -p /var/pgsql/data
RUN chown -R postgres:postgres /var/pgsql

VOLUME ["/var/pgsql"]
EXPOSE 5432

ADD profile /profile
ADD initdb.sh /initdb.sh

RUN chmod +x /initdb.sh

USER postgres

CMD ["/usr/local/pgsql/bin/postgres", "-D", "/var/pgsql/data"]
