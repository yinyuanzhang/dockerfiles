FROM docker:18.09

ARG CLOUD_SDK_VERSION=228.0.0
ARG HELM_VERSION=v2.12.1
ARG HELMFILE_VERSION=v0.41.0

RUN apk add --no-cache bash gawk sed grep bc coreutils
RUN apk add --update -t deps curl tar gzip

RUN curl -L https://storage.googleapis.com/kubernetes-helm/helm-${HELM_VERSION}-linux-amd64.tar.gz > helm.tar.gz  && \
    tar -zxvf helm.tar.gz  && \
    mv linux-amd64/helm /usr/local/bin/helm  && \
    rm -rf helm.tar.gz  && \
    helm init --client-only

RUN apk add --no-cache python && \
    python -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip install --upgrade pip setuptools && \
    rm -r /root/.cache

RUN curl -L https://github.com/roboll/helmfile/releases/download/${HELMFILE_VERSION}/helmfile_linux_amd64 > /usr/bin/helmfile && \
    chmod +x /usr/bin/helmfile && \
    helmfile --version

RUN apk add --update -t deps git
RUN curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \
    tar -zxvf google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \ 
    rm -rf google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz
ENV PATH /google-cloud-sdk/bin:$PATH
RUN gcloud config set core/disable_usage_reporting true && \
    gcloud config set component_manager/disable_update_check true && \
    gcloud components install kubectl