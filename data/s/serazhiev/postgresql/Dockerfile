FROM postgres:11.3

ARG USE_POSTGIS=true
ENV PLUGIN_VERSION=v0.9.5.Final

ENV WAL2JSON_COMMIT_ID=926e11f00ce279c34d913c49e78f7becc56fbfd0

# Install the packages which will be required to get everything to compile
RUN apt-get update \
    && apt-get install -f -y --no-install-recommends \
        software-properties-common \
        build-essential \
        pkg-config \
        git \
        postgresql-server-dev-11 \
        libproj-dev \
    && if [ "$USE_POSTGIS" != "false" ]; then apt-get install -f -y --no-install-recommends \
        postgresql-11-postgis-2.5 \
        postgresql-11-postgis-2.5-scripts \
        postgis; \
       fi \
    && apt-get clean && apt-get update && apt-get install -f -y --no-install-recommends \
        liblwgeom-dev \
    && add-apt-repository "deb http://ftp.debian.org/debian testing main contrib" \
    && apt-get update && apt-get install -f -y --no-install-recommends \
        libprotobuf-c-dev=1.2.* \
    && rm -rf /var/lib/apt/lists/*

# Compile the plugin from sources and install it
RUN git clone https://github.com/debezium/postgres-decoderbufs -b $PLUGIN_VERSION --single-branch \
    && cd /postgres-decoderbufs \
    && make && make install \
    && cd / \
    && rm -rf postgres-decoderbufs

RUN git clone https://github.com/eulerto/wal2json -b master --single-branch \
    && cd /wal2json \
    && git checkout $WAL2JSON_COMMIT_ID \
    && make && make install \
    && cd / \
    && rm -rf wal2json
# Copy the custom configuration which will be passed down to the server (using a .sample file is the preferred way of doing it by
# the base Docker image)
COPY postgresql.conf.sample /usr/share/postgresql/postgresql.conf.sample

# Copy the script which will initialize the replication permissions
COPY init-permissions.sh /docker-entrypoint-initdb.d
RUN apt-get update -y \
&& apt-get install -y python3-pip python3.6 libffi-dev libssl-dev libxml2-dev libxslt1-dev  zlib1g-dev libjpeg62-turbo-dev libkrb5-dev \
&& git clone https://github.com/pgaudit/pgaudit.git \
&& cd pgaudit \
&& git checkout REL_11_STABLE \
&& make check USE_PGXS=1 \
&& make install USE_PGXS=1


