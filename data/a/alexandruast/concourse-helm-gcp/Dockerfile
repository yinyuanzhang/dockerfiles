FROM alpine:3.8 as build
LABEL maintainer="Alexandru Ast <alexandru.ast@gmail.com>"

ARG HELM_URL=https://storage.googleapis.com/kubernetes-helm/helm-v2.12.3-linux-amd64.tar.gz
ARG KUBECTL_URL=https://storage.googleapis.com/kubernetes-release/release/v1.11.6/bin/linux/amd64/kubectl
ARG GCLOUD_SDK_URL=https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-233.0.0-linux-x86_64.tar.gz

ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/google-cloud-sdk/bin

WORKDIR /
RUN apk add --update --no-cache ca-certificates git python jq bash curl tar gzip \
  && curl -sSL -o /usr/local/bin/kubectl "${KUBECTL_URL}" \
  && chmod +x /usr/local/bin/kubectl \
  && mkdir -p /opt \
  && curl -sSL "${GCLOUD_SDK_URL}" | tar zx -C /opt \
  && /opt/google-cloud-sdk/install.sh -q \
  && gcloud config set disable_usage_reporting true \
  && curl -sSL "${HELM_URL}" | tar zx -C /tmp \
  && mv /tmp/linux-amd64/helm /usr/local/bin/helm \
  && mkdir -p "$(helm home)/plugins" \
  && helm plugin install https://github.com/viglesiasce/helm-gcs.git >/dev/null 2>&1 \
  && helm plugin install https://github.com/databus23/helm-diff >/dev/null 2>&1 \
  && helm init --client-only

ADD assets /opt/resource
RUN chmod +x /opt/resource/*

ENTRYPOINT [ "/bin/bash" ]
