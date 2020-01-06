FROM ubuntu:trusty

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
      curl \
      gcc \
      git \
      gnupg2 \
      libffi-dev \
      libssl-dev \
      libyaml-dev \
      make \
      openssl \
      python-dev \
      python-pip && \
    pip install --upgrade setuptools && \
    pip install sops && \
    cd /usr/local/bin && \
    curl -sSL https://github.com/InQuicker/ktmpl/releases/download/0.7.0/ktmpl-0.7.0-linux.tar.gz | tar zvx && \
    curl -sSO https://storage.googleapis.com/kubernetes-release/release/v1.6.2/bin/linux/amd64/kubectl && \
    chmod +x ktmpl kubectl && \
    apt-get purge -y curl && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
