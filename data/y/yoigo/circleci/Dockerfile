FROM docker:18-git


RUN apk update && apk add --no-cache \
    make \
    py-pip \
    bash \
    gettext \
    curl \
    openssl \
    wget \
    jq \
    py-crcmod \
    libc6-compat \
    openssh-client \
    git \
    gnupg \
    perl

RUN pip install \
    docker-compose \
    awscli

# Install Kubectl
RUN wget -q https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl \
    -O /usr/local/bin/kubectl && \
    chmod +x /usr/local/bin/kubectl 

# Install Helm
ENV HELM_VERSION="v2.10.0"
RUN wget -q http://storage.googleapis.com/kubernetes-helm/helm-${HELM_VERSION}-linux-amd64.tar.gz -O - | tar -xzO linux-amd64/helm > /usr/local/bin/helm \
    && chmod +x /usr/local/bin/helm

# Add gcs and s3 plugins to helm
RUN helm init --client-only && helm plugin install https://github.com/hypnoglow/helm-s3.git && helm plugin install https://github.com/nouney/helm-gcs

# Install yq CLI tool
RUN wget -O /bin/yq https://github.com/mikefarah/yq/releases/download/1.14.0/yq_linux_amd64 && \
    chmod +x /bin/yq && \
    ln -s /bin/yq /bin/yaml

# Install Gcloud SDK
ENV CLOUD_SDK_VERSION 215.0.0
ENV PATH /google-cloud-sdk/bin:$PATH
RUN curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \
    tar xzf google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \
    rm google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \
    ln -s /lib /lib64 && \
    gcloud config set core/disable_usage_reporting true && \
    gcloud config set component_manager/disable_update_check true && \
    gcloud config set metrics/environment github_docker_image && \
    gcloud --version

# Install Sentry CLI
RUN curl -sL https://github.com/DarthHater/docker-phantomjs2/releases/download/2.1.1/dockerized-phantomjs.tar.gz | tar xz -C / && \
    curl -sL https://sentry.io/get-cli/ | bash
