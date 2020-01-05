# We cannot use alpine images because Python packages need to be compiled
# and it would requires too much configuration
FROM python:3-slim

ARG OSCLI_HOME=/oscli
ENV PATH=$PATH:${OSCLI_HOME}/bin \
    CLOUDSDK_CONFIG=${OSCLI_HOME}/gcloud/.config \
    CLOUDSDK_CORE_PROJECT=opensense-1 \
    GCLOUD_CLUSTER=cluster-1 \
    GCLOUD_REGION=europe-west1 \
    GCLOUD_ZONE=europe-west1-d \
    GCLOUD_REGISTRY=eu.gcr.io \
    GCLOUD_API_KEYFILE= \
    KUSTOMIZE_VERSION=3.1.0

WORKDIR ${OSCLI_HOME}

    # Create a bin directory for any custom installation 
RUN mkdir ./bin && \
    # Setup Debian main repository
    echo 'deb http://deb.debian.org/debian stretch main' >> /etc/apt/sources.list && apt-get update && \
    apt-get update && \
    # Install build dependencies -- to be cleaned at the end of the Dockerfile
    apt-get install -y --no-install-recommends lsb-release curl gnupg apt-transport-https jq && \
    ### Install oscli dependencies
    # Install git cli
    apt-get install -y --no-install-recommends git && \
    # Install docker
    export DOCKER_REPO="$(lsb_release -c -s)" && \
    echo "deb [arch=amd64] https://download.docker.com/linux/debian $DOCKER_REPO stable" | tee -a /etc/apt/sources.list.d/docker.list && \
    curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - && apt-get update -y && \
    apt-get install -y --no-install-recommends docker-ce && \
    # Install Google Cloud SDK and kubectl
    export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)" && \
    echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && apt-get update -y && \
    apt-get install -y --no-install-recommends google-cloud-sdk kubectl && \
    # Install kustomize
    curl -O -L https://github.com/kubernetes-sigs/kustomize/releases/download/v${KUSTOMIZE_VERSION}/kustomize_${KUSTOMIZE_VERSION}_linux_amd64 && \
    mv kustomize_*_linux_amd64 ./bin/kustomize && chmod 755 ./bin/kustomize

# Install oscli
COPY oscli/ ${OSCLI_HOME}/oscli
COPY requirements.txt setup.* ${OSCLI_HOME}/

RUN pip3 install --no-cache-dir -r requirements.txt && \
    pip3 install --upgrade --no-cache-dir . && \
    rm -rf ./oscli && \
    # Cleaning
    apt-get remove -y --purge lsb-release gnupg apt-transport-https && \
    rm -rf /var/lib/apt/lists/*
