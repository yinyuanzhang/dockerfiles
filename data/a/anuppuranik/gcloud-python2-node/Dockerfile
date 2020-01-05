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


# Python 2.7
RUN apt-get install -y \
    python2.7

# Docker
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - && \
    add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" && \
    apt-get update && \
    apt-get install -y docker-ce

# gcloud sdk
RUN . /etc/os-release && \
    export CLOUD_SDK_REPO="cloud-sdk-${UBUNTU_CODENAME}" && \
    echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \
    curl -fsSL https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && \
    apt-get update && \
    apt-get install -y \
        google-cloud-sdk \
        google-cloud-sdk-app-engine-python \
        kubectl && \
    apt-get clean

# Install yarn and node js
RUN echo "Installing Yarn and Node" && \
    wget https://deb.nodesource.com/setup_10.x && bash setup_10.x && \
    apt-get install -y nodejs && \
    echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee -a /etc/apt/sources.list.d/yarn.list && \
    wget https://dl.yarnpkg.com/debian/pubkey.gpg && apt-key add pubkey.gpg && rm pubkey.gpg && \
    apt-get update && \
    apt-get install -y yarn

# make suitable for circle ci
RUN adduser circleci --home /home/circleci --gecos "" --disabled-password

USER circleci
