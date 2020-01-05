FROM ubuntu:14.04
MAINTAINER Shisei Hanai<ruimo.uno@gmail.com>

RUN apt-get update
RUN apt-get -y install build-essential wget monit
RUN sudo apt-get install -y libreadline-dev build-essential zlib1g-dev

RUN cd /tmp && wget http://ftp.postgresql.org/pub/source/v9.3.4/postgresql-9.3.4.tar.bz2
RUN cd /tmp && tar xf postgresql-9.3.4.tar.bz2
RUN cd /tmp/postgresql-9.3.4 && \
  ./configure && \
  make && \
  make install
RUN cd /tmp/postgresql-9.3.4/contrib/pg_trgm && \
  sed -i 's;^\(\s*#define\s*KEEPONLYALNUM.*\)$;/* \1 */;' trgm.h && \
  make && \
  make install
RUN rm -r /tmp/postgresql-9.3.4
RUN useradd --shell /bin/false -d /var/home postgres
RUN mkdir /var/lib/pgdata && chown -R postgres:postgres /var/lib/pgdata
RUN su - postgres -s /bin/bash -c "/usr/local/pgsql/bin/initdb -D /var/lib/pgdata"
RUN sed -i -e "s;^#log_destination\s*=\s*.*$;log_destination = 'syslog';" \
           -e "s;^#port\s=.*;port = 5432;" \
           -e "s;^#listen_address.*;listen_addresses = '0.0.0.0';" \
  /var/lib/pgdata/postgresql.conf
RUN echo "host     all             all             172.16.0.0/12           trust" >> /var/lib/pgdata/pg_hba.conf
RUN echo "host     all             all             192.168.0.0/16          trust" >> /var/lib/pgdata/pg_hba.conf
ADD monit   /etc/monit/conf.d/

# Add Japan locale
RUN locale-gen ja_JP.UTF-8
RUN sudo /usr/sbin/update-locale LANG=ja_JP.UTF-8

# Define mountable directories.
VOLUME ["/var/lib/pgdata"]

EXPOSE 5432

ADD profile /profile

CMD ["/usr/bin/monit", "-I", "-c", "/etc/monit/monitrc"]
