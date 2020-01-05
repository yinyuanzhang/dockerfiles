ARG DOCKER_VERSION=19.03.4
FROM docker:${DOCKER_VERSION} as dockerbase

FROM google/cloud-sdk:alpine

ARG KUBEVAL_VERSION=0.14.0
ARG HELM_VERSION=v3.0.0

ENV KUBEVAL_VERSION=$KUBEVAL_VERSION
ENV HELM_VERSION=$HELM_VERSION
ENV DOCKER_CLI_EXPERIMENTAL=enabled

COPY --from=mikayel/cloudflare-lite-api /usr/local/bin/cflite /usr/local/bin/cflite

COPY ./functions/. /usr/local/bin/

RUN apk --update add --no-cache jq gettext ca-certificates findutils tar gzip

RUN curl -L https://github.com/instrumenta/kubeval/releases/download/${KUBEVAL_VERSION}/kubeval-linux-amd64.tar.gz | tar xz -C /tmp && mv /tmp/kubeval /usr/local/bin/kubeval && rm -rf /tmp/*

RUN curl -L https://get.helm.sh/helm-${HELM_VERSION}-linux-amd64.tar.gz | tar xvz && mv linux-amd64/helm /usr/local/bin/helm && \
    rm -rf linux-amd64 && rm -rf /tmp/*

COPY --from=dockerbase /usr/local/bin/docker /usr/local/bin/docker

COPY --from=google/cloud-sdk /usr/bin/kubectl /usr/bin/kubectl
