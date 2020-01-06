FROM ubuntu:14.04.2
MAINTAINER Nhan Tran <tranphanquocnhan@gmail.com>

RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get install -y wget
RUN apt-get install -y unzip
RUN apt-get install -y curl
RUN apt-get install -y vim
RUN update-alternatives --set editor /usr/bin/vim.basic

# Install the database packages
RUN apt-get install -y postgresql-9.3
RUN apt-get install -y postgresql-client
RUN apt-get install -y libpq-dev

RUN sed -i -e "s/#listen_addresses = 'localhost'/listen_addresses = '*'/g" /etc/postgresql/9.3/main/postgresql.conf
RUN sed -i -e "s/local   all             all                                     peer/local   all             all                                     md5/g" /etc/postgresql/9.3/main/pg_hba.conf
RUN echo "host    all             all             0.0.0.0/0            md5" >> /etc/postgresql/9.3/main/pg_hba.conf
RUN cat /etc/postgresql/9.3/main/pg_hba.conf

EXPOSE 5432

ONBUILD ADD create_database.sql /home/postgres/create_database.sql
ONBUILD RUN chown postgres:postgres /home/postgres/create_database.sql
ONBUILD USER postgres
# Login to PostgreSQL
ONBUILD RUN /etc/init.d/postgresql start && psql -f /home/postgres/create_database.sql
ONBUILD CMD ["/usr/lib/postgresql/9.3/bin/postgres", "-D", "/var/lib/postgresql/9.3/main", "-c", "config_file=/etc/postgresql/9.3/main/postgresql.conf"]
