FROM ubuntu:18.04

ARG CLOUD_SDK_VERSION=228.0.0
ENV CLOUD_SDK_VERSION=$CLOUD_SDK_VERSION

ARG HELM_VERSION=2.11.0
ENV HELM_VERSION=$HELM_VERSION

ENV PATH=/google-cloud-sdk/bin:$PATH DEBIAN_FRONTEND=noninteractive

RUN sed -i '/^deb-src /s/^/#/' /etc/apt/sources.list && \
    apt-get update && apt-get -yq upgrade && \
    apt-get install --no-install-recommends -yq zip unzip openssh-client wget curl python docker.io ca-certificates git && \
    curl -L https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz | tar -xvz -C / && \
      gcloud config set core/disable_usage_reporting true && \
      gcloud config set component_manager/disable_update_check true && \
      gcloud config set metrics/environment github_docker_image && \
      gcloud components install beta --quiet && \
      gcloud components install kubectl --quiet && \
      gcloud --version && \
    curl -L https://storage.googleapis.com/kubernetes-helm/helm-v$HELM_VERSION-linux-amd64.tar.gz | tar -xvz --strip=1 -C /usr/bin && \
    apt-get autoremove -yq && apt-get clean -yq && rm -rf /var/lib/apt/lists/*
