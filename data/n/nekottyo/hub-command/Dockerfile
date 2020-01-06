FROM debian:stretch-slim

ENV HUB_VERSION 2.12.8

WORKDIR /app
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        git \
        wget \
        ca-certificates \
    && wget -q https://github.com/github/hub/releases/download/v${HUB_VERSION}/hub-linux-amd64-${HUB_VERSION}.tgz \
    && tar zxf hub-linux-amd64-${HUB_VERSION}.tgz \
    && mv hub-linux-amd64-${HUB_VERSION}/bin/hub /usr/local/bin/ \
    && rm -rf ./* \
    && chmod +x /usr/local/bin/hub \
    && apt-get purge -y \
        wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

CMD ["hub"]
