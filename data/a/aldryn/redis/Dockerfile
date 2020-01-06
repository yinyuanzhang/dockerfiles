FROM redis:3.0-alpine

RUN apk add --no-cache gettext

COPY docker-entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

ENV DATADIR=/data DATABASES=16 APPENDONLY=no
COPY redis.conf /etc/redis.conf

STOPSIGNAL SIGINT

CMD ["redis-server", "-"]
