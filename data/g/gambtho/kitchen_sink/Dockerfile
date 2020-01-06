FROM ubuntu:16.04
ARG tf_version="0.11.7"
ARG go_version="1.10.3"
ARG docker_version="1.21.2"

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    apt-transport-https \
    build-base \
    gcc \ 
    abuild \
    binutils \
    binutils-doc \ 
    gcc-doc \
    ca-certificates \
    curl \
    dmsetup \
    git \
    gzip \
    jq \
    make \
    python-pip \
    software-properties-common \
    unzip \
    wget \
    zip \
    xvfb \
    redis-server \
    libgtk2.0-0 \
    libnotify-dev \
    libgconf-2-4 \
    libnss3 \
    libxss1 \
    libasound2 \
    default-jdk \
    build-essential checkinstall \
    libssl-dev \
    && rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Docker
RUN ( curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - ) \
 && apt-key fingerprint 0EBFCD88 \
 && add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" \
 && apt-get update \
 && apt-get install -y docker-ce \
 && curl -L https://github.com/docker/compose/releases/download/1.18.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose \
 && chmod +x /usr/local/bin/docker-compose

# SBT
RUN ( echo "deb https://dl.bintray.com/sbt/debian /" | tee -a /etc/apt/sources.list.d/sbt.list ) \
 && apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2EE0EA64E40A89B84B2DF73499E82A75642AC823 \
 && apt-get update \
 && apt-get install -y --no-install-recommends sbt

# Node
RUN curl -sL https://deb.nodesource.com/setup_9.x | bash - \
 && apt-get install -y nodejs \
 && npm install -g yarn

# AWS CLI
RUN pip install -U setuptools wheel \
&& pip install -U awscli

RUN curl -o /usr/local/bin/ecs-cli https://s3.amazonaws.com/amazon-ecs-cli/ecs-cli-linux-amd64-latest \
&& chmod +x /usr/local/bin/ecs-cli

# Terraform 
RUN curl https://releases.hashicorp.com/terraform/${tf_version}/terraform_${tf_version}_linux_amd64.zip -o terraform_${tf_version}_linux_amd64.zip \
    && unzip terraform_${tf_version}_linux_amd64.zip -d /usr/local/bin \
    && rm terraform_${tf_version}_linux_amd64.zip 

# GoLang
RUN curl https://dl.google.com/go/go${go_version}.linux-amd64.tar.gz -o go${go_version}.linux-amd64.tar.gz \
    && tar -C /usr/local -xzf go${go_version}.linux-amd64.tar.gz \
    && rm go${go_version}.linux-amd64.tar.gz 

RUN mkdir -p ${HOME}/go \
    && echo 'export GOPATH=${HOME}/go' >> ${HOME}/.profile \
    && echo 'export GOBIN=${GOPATH}/bin' >> ${HOME}/.profile

ENV PATH=$PATH:/usr/local/go/bin

# Cleanup
RUN rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/*


