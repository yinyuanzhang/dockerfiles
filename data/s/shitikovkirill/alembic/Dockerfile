FROM python:3.7

ARG INSTALLED_LIB="alembic sqlalchemy psycopg2"

WORKDIR /alembic

RUN set -ex \
    && pip install ${INSTALLED_LIB} --no-cache-dir


COPY ./docker-entrypoint.sh /usr/local/bin/
RUN set -ex \
    && chmod +x /usr/local/bin/docker-entrypoint.sh

ENTRYPOINT ["docker-entrypoint.sh"]
