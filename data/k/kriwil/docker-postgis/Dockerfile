FROM postgres:9.4

RUN apt-get update && apt-get install -y postgresql-9.4-postgis-2.1 postgis \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*
COPY postgis.sql docker-entrypoint-initdb.d/
