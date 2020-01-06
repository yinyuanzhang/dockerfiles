FROM alpine:3.5

LABEL maintainer "itiQiti SAS <opensource@itiqiti.com>"

ENV MODE=default \
    VARNISH_PACKAGE_VERSION="4.1.3-r0" \
    VARNISH_OPTIONS= \
    VARNISH_PORT=80 \
    VARNISH_LOG=false \
    VARNISH_MEMORY=100M \
    VARNISH_CFG=

RUN apk add --update --no-cache --virtual .build-deps curl && \
    curl -s -f -L https://github.com/itiqiti/dkconf/releases/download/0.2/dkconf-linux -o /usr/local/bin/dkconf && \
    chmod +x /usr/local/bin/dkconf && \
    apk del .build-deps && \
    apk add --no-cache "varnish=${VARNISH_PACKAGE_VERSION}"

COPY ["templates", "/etc/varnish/templates"]
COPY ["docker-entrypoint.sh", "/usr/local/bin/"]

EXPOSE ${VARNISH_PORT}

WORKDIR /etc/varnish

CMD  ["/usr/local/bin/docker-entrypoint.sh"]
