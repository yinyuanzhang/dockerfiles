FROM ubuntu:latest

LABEL maintainer="anuppuranik @t g m a i l c o m"

# Upgrade the base distro
RUN apt-get update && apt-get upgrade -y

# Install some common tools and packages
RUN apt-get install -y software-properties-common \
        zip \
        unzip \
        git \
        ssh \
        curl \
        apt-transport-https \
        ca-certificates

# Docker
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - && \
    add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" && \
    apt-get update && \
    apt-get install -y docker-ce

# Oracle JDK
RUN add-apt-repository ppa:linuxuprising/java -y && \
    apt-get update && \
    echo oracle-java13-installer shared/accepted-oracle-license-v1-2 select true | /usr/bin/debconf-set-selections && \
    apt-get install -y oracle-java13-installer && \
    apt-get install -y oracle-java13-set-default && \
    apt-get clean

# gcloud sdk
RUN . /etc/os-release && \
    export CLOUD_SDK_REPO="cloud-sdk-${UBUNTU_CODENAME}" && \
    echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \
    wget https://packages.cloud.google.com/apt/doc/apt-key.gpg && apt-key add apt-key.gpg && rm apt-key.gpg && \
    apt-get update && \
    apt-get install -y \
        google-cloud-sdk \
        google-cloud-sdk-app-engine-go \
        google-cloud-sdk-app-engine-java \
        google-cloud-sdk-app-engine-python \
        google-cloud-sdk-bigtable-emulator \
        google-cloud-sdk-cbt \
        google-cloud-sdk-datalab \
        google-cloud-sdk-datastore-emulator \
        google-cloud-sdk-pubsub-emulator \
        kubectl && \
    apt-get clean

# make suitable for circle ci
RUN adduser circleci --home /home/circleci --gecos "" --disabled-password

USER circleci
