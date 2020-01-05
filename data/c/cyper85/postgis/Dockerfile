FROM postgres:12

MAINTAINER Andreas Neumann <andr.neumann@googlemail.com> 

ENV POSTGIS_MAJOR 3
ENV POSTGIS_VERSION  3.0.0+dfsg-1.pgdg100+1

RUN apt-get update
RUN apt-cache showpkg postgresql-$PG_MAJOR-postgis-$POSTGIS_MAJOR
RUN apt-get install -y --no-install-recommends postgresql-$PG_MAJOR-postgis-$POSTGIS_MAJOR=$POSTGIS_VERSION 
RUN apt-get install -y --no-install-recommends postgresql-$PG_MAJOR-postgis-$POSTGIS_MAJOR-scripts=$POSTGIS_VERSION
RUN apt-get install -y --no-install-recommends postgis=$POSTGIS_VERSION
RUN rm -rf /var/lib/apt/lists/*

RUN mkdir -p /docker-entrypoint-initdb.d
COPY init-user.sh /docker-entrypoint-initdb.d/

VOLUME ["/var/lib/postgresql/data"]
