FROM circleci/python:3.6

ENV GO_VERSION=1.13.4
ENV NODE_VERSION=10.16.0
ENV BUILDIFIER_VERSION=0.26.0
ENV FLAKE8_VERSION=3.7.6
ENV ISORT_VERSION=4.3.4
ENV PEP8_VERSION=0.5.0
ENV PLEASE_VERSION=14.0.0
ENV TENSORFLOW_VERSION=1.14.0

# ENV KUBE_VERSION=1.13.7

USER root
# install go
ENV PATH="/usr/local/go/bin:${PATH}"
RUN \
  curl -o /tmp/go${GO_VERSION}.linux-amd64.tar.gz https://dl.google.com/go/go${GO_VERSION}.linux-amd64.tar.gz \
  && tar -xf /tmp/go${GO_VERSION}.linux-amd64.tar.gz -C /usr/local \
  && rm -rf /tmp/go${GO_VERSION}.linux-amd64.tar.gz

# install npm
ENV PATH="/usr/local/nodejs/bin:${PATH}"
RUN \
  curl -o /tmp/node-v${NODE_VERSION}-linux-x64.tar.xz https://nodejs.org/dist/v${NODE_VERSION}/node-v${NODE_VERSION}-linux-x64.tar.xz \
  && tar -xf /tmp/node-v${NODE_VERSION}-linux-x64.tar.xz -C /tmp \
  && mv /tmp/node-v${NODE_VERSION}-linux-x64 /usr/local/nodejs \
  && rm /tmp/node-v${NODE_VERSION}-linux-x64.tar.xz \
  # yarn
  && npm install -g yarn

# aws cli
RUN \
  pip install --no-cache-dir awscli --upgrade flake8==${FLAKE8_VERSION} isort==${ISORT_VERSION} pep8-naming==${PEP8_VERSION} tensorflow==${TENSORFLOW_VERSION}

# install linter deps
# RUN \
#   pip install flake8==${FLAKE8_VERSION} isort==${ISORT_VERSION} pep8-naming==${PEP8_VERSION}

# Install soundfile lib
RUN apt-get install -y libsndfile-dev

# install eslint and its dependencies
COPY package.json package-lock.json /usr/local/nodejs/
RUN npm ci -g
ENV PATH="/usr/local/nodejs/node_modules/eslint/bin:${PATH}"

# install buildifier
RUN \
  wget https://github.com/bazelbuild/buildtools/releases/download/${BUILDIFIER_VERSION}/buildifier \
  && chmod +x buildifier \
  && cp buildifier /usr/local/bin/

# install java
RUN \
  apt-get update \
  && apt-get install -y \
    default-jre-headless \
    postgresql-client \
  && rm -rf /var/lib/apt/lists/*

# install helm
RUN \
  wget https://get.helm.sh/helm-v2.16.1-linux-amd64.tar.gz -O helm.tar.gz \
  && tar -zxvf helm.tar.gz \
  && mv linux-amd64/helm /usr/local/bin/ \
  && helm init -c

USER circleci

COPY please.sh /tmp/please.sh
RUN /tmp/please.sh
ENV PATH="~/.please:${PATH}"

COPY test.sh /tmp/test.sh
RUN /tmp/test.sh
