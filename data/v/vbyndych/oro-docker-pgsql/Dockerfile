FROM postgres:9.6

RUN apt-get update \
      && apt-get install -y --no-install-recommends \
           postgresql-9.6-postgis-2.4 \
           postgresql-9.6-postgis-2.4-scripts \
           postgis \
      && rm -rf /var/lib/apt/lists/*

COPY extensions.sql /docker-entrypoint-initdb.d/10_extensions.sql