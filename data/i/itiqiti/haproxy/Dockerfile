FROM haproxy:1.7.5-alpine

LABEL maintainer "itiQiti SAS <opensource@itiqiti.com>"

ENV MODE=default \
    HAP_CONFIG_FILES= \
    HAP_OPTIONS= \
    HAP_CFG_FRONT= \
    HAP_CFG_BACK=

RUN apk add --update --no-cache --virtual .build-deps curl && \
    curl -s -f -L https://github.com/itiqiti/dkconf/releases/download/0.2/dkconf-linux -o /usr/local/bin/dkconf && \
    chmod +x /usr/local/bin/dkconf && \
    apk del .build-deps

COPY ["templates", "/usr/local/etc/haproxy/templates"]
COPY ["docker-entrypoint.sh", "/usr/local/bin/"]

CMD  ["/usr/local/bin/docker-entrypoint.sh"]
