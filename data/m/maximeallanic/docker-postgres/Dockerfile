FROM postgres:9.6

RUN apt-get update -q && apt-get install -yqq --no-install-recommends \
 postgis \
 postgresql-9.6-postgis-2.3-scripts \
 postgresql-9.6-postgis-2.3 \
 && rm -rf /var/lib/apt/lists/*