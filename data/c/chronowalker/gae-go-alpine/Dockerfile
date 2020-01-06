FROM golang:1.8-alpine3.6
MAINTAINER Koji <stylethewalker@gmail.com>

ENV CLOUD_SDK_VERSION=178.0.0 \
    CLOUD_SDK=/google-cloud-sdk \
    PATH=/google-cloud-sdk/bin:${PATH} \
    PATH=/google-cloud-sdk/platform/google_appengine:${PATH} \
    GOROOT=/google-cloud-sdk/platform/google_appengine/goroot-1.8 \
    GOPATH=/go

RUN cd / && apk add --update --no-cache curl tar gcc musl-dev git python && \
    curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \
    tar xzf google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \
    rm google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \
    ${CLOUD_SDK}/install.sh --usage-reporting=true --path-update=true --disable-installation-options --bash-completion=false && \
    Y | /google-cloud-sdk/bin/gcloud components install app-engine-go && \
    chmod 755 ${CLOUD_SDK}/platform/google_appengine/goapp && \
    chmod 755 ${CLOUD_SDK}/platform/google_appengine/appcfg.py && \
    apk del ${PACKAGES} --no-cache && rm -rf /tmp/* /var/cache/apk/*
