FROM python:2.7.12-alpine

ENV ARCH amd64

ENV DUMB_INIT_VERSION 1.1.3

ENV GOSU_VERSION 1.9
ENV GOSU_SIGNING_KEY B42F6819007F00F88E364FD4036A9C25BF357DD4

RUN set -ex -o pipefail; \
    apk add --no-cache --virtual .build-deps curl \
    && cd $(mktemp -d) \
    && curl -fsSL -O "https://github.com/Yelp/dumb-init/releases/download/v${DUMB_INIT_VERSION}/dumb-init_${DUMB_INIT_VERSION}_${ARCH}" \
    && curl -fsSL -O "https://github.com/Yelp/dumb-init/releases/download/v${DUMB_INIT_VERSION}/sha256sums" \
    && cat sha256sums | tail -n 1 | sha256sum -c \
    && mv -v dumb-init_${DUMB_INIT_VERSION}_${ARCH} /usr/local/bin/dumb-init \
    && curl -fsSL -o /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/${GOSU_VERSION}/gosu-${ARCH}" \
    && curl -fsSL -o gosu.asc "https://github.com/tianon/gosu/releases/download/${GOSU_VERSION}/gosu-${ARCH}.asc" \
    && chmod +x /usr/local/bin/dumb-init /usr/local/bin/gosu \
    && gosu nobody true \
    && apk del .build-deps \
    && rm -rf /var/cache/apk/* \
    && pip install --upgrade pip \
    && pip install eve eve-swagger redis

WORKDIR /src

VOLUME /src

EXPOSE 80

ENTRYPOINT ["/usr/local/bin/dumb-init", "--"]

CMD ["python", "main.py"]
