FROM alpine:edge

LABEL de.kdac.postgis.maintainer = "Claus Böhmer" \
      de.kdac.postgis.authors = "eso@bistum-eichstaett.de" \
      de.kdac.postgis.url = "https://hub.docker.com/r/kidac/postgresql" \
      de.kdac.postgis.documentation = "https://hub.docker.com/r/kidac/postgresql" \
      de.kdac.postgis.source = "https://github.com/kidac/postgresql" \
      de.kdac.postgis.version = "11.5" \
      de.kdac.postgis.vendor = "KDAC - https://ews.kdac.de" \
      de.kdac.postgis.licenses = "https://www.postgresql.org/about/licence/" \
      de.kdac.postgis.title = "Postgresql (KDAC Version)" \
      de.kdac.postgis.description = "Adapted Postgresql/PostGIS Dockerfile used by https://ews.kdac.de"

ENV PGDATA_DIR=/var/lib/postgresql \
    PGDATA=/var/lib/postgresql/data

VOLUME ["${PGDATA_DIR}"]

RUN apk --no-cache upgrade \
 && apk add --no-cache postgresql-contrib postgresql bash tini \
 && apk add --no-cache -X http://dl-cdn.alpinelinux.org/alpine/edge/testing postgis \
 && mkdir -p /run/postgresql \
 && chown -R postgres:postgres /run/postgresql

EXPOSE 5432

COPY entrypoint.sh /
COPY postgresql.conf /
COPY pg_hba.conf /

CMD ["/entrypoint.sh"]
ENTRYPOINT ["/sbin/tini", "--"]
