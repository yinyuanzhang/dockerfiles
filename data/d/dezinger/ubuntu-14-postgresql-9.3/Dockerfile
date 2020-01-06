FROM dezinger/ubuntu-14:latest

MAINTAINER dezinger@gmail.com

ENV DEBIAN_FRONTEND noninteractive
ARG PG_MAJOR=9.3
ARG PG_BIN=/usr/lib/postgresql/$PG_MAJOR/bin
ARG PG_DBDIR=/var/lib/postgresql/$PG_MAJOR/main
ARG LOG_DIR=/var/log/postgresql

COPY files/ /

RUN \
# Add the PostgreSQL PGP key to verify their packages.
# It should be the same key as https://www.postgresql.org/media/keys/ACCC4CF8.asc
    apt-get install -y gnupg && \
    curl -s https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - && \
# Update
    apt-get -y update && apt-get install --no-install-recommends -y \ 
# Install PostgreSQL
    postgresql-$PG_MAJOR \ 
    postgresql-client-$PG_MAJOR \ 
    postgresql-contrib-$PG_MAJOR && \
# Post installation configuration
    mkdir -p /var/run/postgresql/$PG_MAJOR-main.pg_stat_tmp && \ 
    chown -R postgres:postgres /var/run/postgresql/$PG_MAJOR-main.pg_stat_tmp && \ 
    chmod +x /usr/local/bin/run_postgres && \
    chmod -R 755 /init /hooks && \ 
    mkdir -p $PG_DBDIR && chown -R postgres:postgres $PG_DBDIR && \ 
    mkdir -p ${LOG_DIR} && \
    chmod -R 777 ${LOG_DIR} ${PG_BIN} /var/lib/postgresql /var/run/postgresql  && \
# clean
    apt-get -y autoremove && apt-get -y clean && apt-get autoclean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*   
    

ENV PATH=$PATH:/usr/lib/postgresql/${PG_MAJOR}/bin \
	PG_MAJOR=${PG_MAJOR} \
	PG_BIN=${PG_BIN} \
	PG_DBDIR=${PG_DBDIR} \
        LOG_DIR=${LOG_DIR}
    
VOLUME ["/var/lib/postgresql"]

# Expose the PostgreSQL port
EXPOSE 5432