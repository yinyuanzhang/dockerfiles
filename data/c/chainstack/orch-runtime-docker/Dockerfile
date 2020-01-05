FROM hyperledger/fabric-tools:1.4.4

# Dec 11, 2019 marker

LABEL vendor="Chainstack"

ENV LANG=en_US.UTF-8
ENV LC_ALL=C.UTF-8

# System deps
RUN apt-get update && apt-get install -qqy software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get autoremove -y python3.5  && \
    apt-get upgrade -qqy && \
    apt-get install -qqy \
      build-essential \
      python3.7 \
      python3.7-dev \
      python3-distutils \
      gettext \
      git \
      curl \
      wget \
      vim \
      libssl-dev \
      libmysqlclient-dev \
      libleveldb-dev \
      libdb-dev \
      libsodium-dev \
      libtinfo-dev \
      zlib1g-dev && \
    update-ca-certificates && \
    apt-get clean && \
    curl https://bootstrap.pypa.io/get-pip.py | python3.7

RUN rm -f /usr/bin/python && ln -s /usr/bin/python3.7 /usr/bin/python

# Add Tini
ENV TINI_VERSION=v0.18.0

ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /bin/tini
RUN chmod +x /bin/tini

ENV CLOUD_SDK=273.0.0-0
ENV KUBECTL=1.14.9-00

RUN echo "deb http://packages.cloud.google.com/apt cloud-sdk-bionic main" > /etc/apt/sources.list.d/google-cloud-sdk.list \
    && echo "deb http://apt.kubernetes.io/ kubernetes-xenial main" > /etc/apt/sources.list.d/kubernetes.list \
    && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && \
    apt-get update \
    && apt-get install -y google-cloud-sdk=${CLOUD_SDK} kubectl=${KUBECTL} \
    && gcloud config set core/disable_usage_reporting true \
    && gcloud config set component_manager/disable_update_check true \
    && apt-get clean

# Add helm
ENV HELM_VERSION=v2.16.1

RUN wget -q http://storage.googleapis.com/kubernetes-helm/helm-${HELM_VERSION}-linux-amd64.tar.gz -O - | tar -xzO linux-amd64/helm > /usr/local/bin/helm && \
    chmod +x /usr/local/bin/helm && helm init --service-account ci-helm --client-only && \
    helm plugin install https://github.com/nouney/helm-gcs

RUN pip install pip pipenv dump-env poetry

# Add latest stable quorum tools
ENV QUORUM_VERSION=2.4.0
ENV ISTANBUL_VERSION=1.0.1
ENV QUORUM_TOOLBOX_VERSION=3.2.0

# All dependencies are for constellation
RUN apt-get update -qq \
    && apt-get install -qqy \
        wget \
        libleveldb-dev \
        libdb-dev \
        libtinfo-dev \
        zlib1g-dev \
        libsodium-dev \
        libgmp-dev \
        netbase \
    && apt-get clean

# Install geth
RUN wget -q https://dl.bintray.com/quorumengineering/quorum/v${QUORUM_VERSION}/geth_v${QUORUM_VERSION}_linux_amd64.tar.gz -O - \
    | tar xzO geth > /usr/local/bin/geth \
    && chmod +x /usr/local/bin/geth

# Install istanbul
RUN wget -q https://dl.bintray.com/quorumengineering/istanbul-tools/istanbul-tools_v${ISTANBUL_VERSION}_linux_amd64.tar.gz -O - \
    | tar xzO istanbul> /usr/local/bin/istanbul \
	&& chmod +x /usr/local/bin/istanbul

# Install bootnode
RUN wget -q https://github.com/chainstack/quorum-toolbox/releases/download/v${QUORUM_TOOLBOX_VERSION}/bootnode_v${QUORUM_VERSION}_linux_amd64.tar.gz -O - \
    | tar xzO bootnode > /usr/local/bin/bootnode \
    && chmod +x /usr/local/bin/bootnode

# Install constellation
RUN wget -q https://github.com/chainstack/quorum-toolbox/releases/download/v${QUORUM_TOOLBOX_VERSION}/constellation-latest-ubuntu1804.tar.gz -O - \
    | tar xzO constellation-node > /usr/local/bin/constellation-node \
    && chmod +x /usr/local/bin/constellation-node

RUN rm -f /usr/bin/python && ln -s /usr/bin/python3.7 /usr/bin/python
