#--------- Generic stuff all our Dockerfiles should start with so we get caching ------------
FROM postgres
MAINTAINER Pascal Obstétar<pascal.obstetar@gmail.com>

ENV POSTGIS_MAJOR 2.4

# Installe l'extension postgis
RUN apt-get update \
      && apt-get install -y --no-install-recommends \
           postgresql-$PG_MAJOR-postgis-$POSTGIS_MAJOR \
           postgresql-$PG_MAJOR-postgis-$POSTGIS_MAJOR-scripts \
           postgis \
      && rm -rf /var/lib/apt/lists/*
      
# Met la locale en fr
RUN localedef -i fr_FR -c -f UTF-8 -A /usr/share/locale/locale.alias fr_FR.UTF-8
ENV LANG fr_FR.utf8      

# Ajoute les bash suivants
RUN mkdir -p /docker-entrypoint-initdb.d
COPY ./initdb-postgis.sh /docker-entrypoint-initdb.d/postgis.sh
COPY ./update-postgis.sh /usr/local/bin
