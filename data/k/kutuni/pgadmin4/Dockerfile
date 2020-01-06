FROM python:3-alpine3.6

ENV PGADMIN4_VERSION 2.0

# Metadata
LABEL org.label-schema.name="pgAdmin4" \
      org.label-schema.version="$PGADMIN4_VERSION" \
      org.label-schema.license="PostgreSQL" \
      org.label-schema.url="https://www.pgadmin.org" \
      org.label-schema.vcs-url="https://github.com/kutuni/pgAdmin4"

RUN set -ex \
	&& apk add --no-cache --virtual .run-deps \
		bash \
		postgresql \
		postgresql-libs \
	&& apk add --no-cache --virtual .build-deps \
		gcc \
		musl-dev \
		openssl \
		postgresql-dev \
	&& pip --no-cache-dir install \
		https://ftp.postgresql.org/pub/pgadmin/pgadmin4/v2.0/pip/pgadmin4-2.0-py2.py3-none-any.whl \
	&& apk del .build-deps

VOLUME /var/lib/pgadmin4

COPY docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]

EXPOSE 5050
CMD ["pgadmin4"]
