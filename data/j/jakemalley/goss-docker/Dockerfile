FROM docker:latest
ARG GOSS_VERSION=v0.3.7
RUN apk update && apk upgrade && apk add bash curl && mkdir /test && \
    curl -s -Lo /usr/local/bin/goss https://github.com/aelsabbahy/goss/releases/download/${GOSS_VERSION}/goss-linux-amd64 && \
    chmod +rx /usr/local/bin/goss && \
    curl -s -Lo /usr/local/bin/dgoss https://raw.githubusercontent.com/aelsabbahy/goss/${GOSS_VERSION}/extras/dgoss/dgoss && \
    chmod +rx /usr/local/bin/dgoss
WORKDIR /test