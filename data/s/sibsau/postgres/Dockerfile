from postgres:alpine
MAINTAINER Anton Goroshkin <neobht@sibsau.ru>

ENV LANG ru_RU.utf8
RUN set -ex \
    \
    && apk add --no-cache --virtual .fetch-deps \
        py-pip \
        py-psycopg2 \
        py-psutil \
    && pip install pg_activity


