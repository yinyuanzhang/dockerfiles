FROM alpine:3.8

ARG HELM_VERSION=v2.11.0
ARG KUBE_VERSION="v1.14.8"

RUN apk --no-cache update \
  && rm -rf /var/cache/apk/* \
  && apk add --update -t deps curl tar gzip make bash python which nodejs-current yarn npm ca-certificates git openssh \
  && apk add mongodb-tools --update-cache --repository http://dl-3.alpinelinux.org/alpine/v3.9/community/ --repository http://dl-3.alpinelinux.org/alpine/v3.9/main/ \
  && curl -L https://storage.googleapis.com/kubernetes-release/release/${KUBE_VERSION}/bin/linux/amd64/kubectl -o /usr/local/bin/kubectl \
  && chmod +x /usr/local/bin/kubectl \
  && curl -L http://storage.googleapis.com/kubernetes-helm/helm-${HELM_VERSION}-linux-amd64.tar.gz | tar zxv -C /tmp \
  && mv /tmp/linux-amd64/helm /usr/local/bin/helm \
  && chmod +x /usr/local/bin/helm \
  && helm init --client-only \
  && curl -sSL https://sdk.cloud.google.com > /tmp/gcl && bash /tmp/gcl --install-dir=~/gcloud --disable-prompts \
  && rm -rf /tmp/linux-amd64

RUN mkdir -p ~/.helm/plugins \
  && helm plugin install https://github.com/hypnoglow/helm-s3.git \
  && helm plugin install https://github.com/nouney/helm-gcs \
  && helm plugin install https://github.com/databus23/helm-diff \
  && helm plugin install https://github.com/futuresimple/helm-secrets \
  && rm -r /tmp/helm-diff /tmp/helm-diff.tgz

WORKDIR /tmp
