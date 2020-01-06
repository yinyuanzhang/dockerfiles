FROM redis:3.2.9-alpine

LABEL maintainer "itiQiti SAS <opensource@itiqiti.com>"
LABEL creator "Mikael Robert <mikaelrob@gmail.com>"

ENV MODE=default \
    REDIS_SENTINEL=redis-sentinel \
    REDIS_SENTINEL_PORT=26379 \
    REDIS_REPLICA_PORT=26379 \
    REDIS_PORT=6379

RUN apk add --update --no-cache --virtual .build-deps curl && \
    curl -s -f -L https://github.com/itiqiti/dkconf/releases/download/0.2/dkconf-linux -o /usr/local/bin/dkconf && \
    chmod +x /usr/local/bin/dkconf && \
    apk del .build-deps

COPY ["templates", "/usr/local/etc/redis/templates"]
COPY ["docker-entrypoint.sh", "/usr/local/bin/"]

CMD  ["/usr/local/bin/docker-entrypoint.sh"]
