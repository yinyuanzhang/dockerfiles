FROM alpine:3.5

LABEL de.kdac.postgresql.maintainer = "Claus Böhmer" \
      de.kdac.postgresql.authors = "eso@bistum-eichstaett.de" \
      de.kdac.postgresql.url = "https://hub.docker.com/r/kidac/postgresql" \
      de.kdac.postgresql.documentation = "https://hub.docker.com/r/kidac/postgresql" \
      de.kdac.postgresql.source = "https://github.com/kidac/postgresql" \
      de.kdac.postgresql.version = "9.6" \
      de.kdac.postgresql.vendor = "KDAC - https://ews.kdac.de" \
      de.kdac.postgresql.licenses = "https://www.postgresql.org/about/licence/" \
      de.kdac.postgresql.title = "Postgresql (KDAC Version)" \
      de.kdac.postgresql.description = "Adapted Postgresql Dockerfile used by https://ews.kdac.de"

ENV PGDATA_DIR=/var/lib/postgresql \
    PGDATA=/var/lib/postgresql/data

VOLUME ["${PGDATA_DIR}"]

RUN apk --no-cache upgrade \
 && apk add --no-cache postgresql-contrib postgresql bash tini \
 && mkdir -p /run/postgresql \
 && chown -R postgres:postgres /run/postgresql

EXPOSE 5432

COPY entrypoint.sh /
COPY postgresql.conf /
COPY pg_hba.conf /

CMD ["/entrypoint.sh"]
ENTRYPOINT ["/sbin/tini", "--"]
