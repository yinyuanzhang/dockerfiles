FROM postgres:10.4
MAINTAINER Brian Holman <bholman@dezota.com>

ENV POSTGRES_PASSWORD="Chang3M3R1ghtN0w"

RUN apt-get update && \
    apt-get -y install gzip wget python && \
    mkdir /awdata && \
    chown postgres:postgres /awdata

COPY pginit-aw.sh /docker-entrypoint-initdb.d/pginit-aw.sh
