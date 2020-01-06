from centos:centos6

MAINTAINER Anoop A K <anoop@codecg.com>

# Set Locale and Data directory
ENV PGDATA /var/lib/pgsql/data
ENV LANG en_US.utf8

# Add postgres user
RUN groupadd -r postgres && useradd -r -g postgres postgres 

# install PostgreSQL server
RUN yum install postgresql-server -y

# Switch user to postgres for database configuration
USER postgres

# Create data directory and set permissions
RUN mkdir -p /var/lib/pgsql/data && chown -R postgres /var/lib/pgsql/data 

# Initialize and setup user account
RUN initdb &&\
    pg_ctl start &&\
    sleep 1 &&\
    createdb afanasy &&\
    psql --command "CREATE USER afadmin PASSWORD 'AfPassword';" &&\
    pg_ctl stop &&\
    sleep 1
    
# Configure PostgreSQL for afanasy server access
RUN echo "host    afanasy    afadmin    192.168.0.0/16    password" >> /var/lib/pgsql/data/pg_hba.conf
RUN echo "host    afanasy    afadmin    172.17.0.0/16    password" >> /var/lib/pgsql/data/pg_hba.conf
RUN echo "listen_addresses='*'" >> /var/lib/pgsql/data/postgresql.conf 

# Fix for error "Could not create shared memory segment" while launching the container in centos6
RUN sed -i "s/shared_buffers = 32MB/shared_buffers = 3500/" /var/lib/pgsql/data/postgresql.conf

VOLUME ["/var/log/pgsql", "/var/lib/pgsql/data"]
EXPOSE 5432

CMD ["postgres"]
