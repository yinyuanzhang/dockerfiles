FROM jenkins/jnlp-slave:3.35-4-alpine

ARG DOCKER_COMPOSE_VERSION=1.22.0
ARG HELM_VERSION=v2.14.3

USER root

RUN apk --update upgrade && \
    apk add --no-cache py-pip git openssh curl python3-dev && \
    apk add gcc musl-dev linux-headers rsync grep make docker jq && \
    rm -rf /var/cache/apk/*

RUN wget https://storage.googleapis.com/kubernetes-helm/helm-${HELM_VERSION}-linux-amd64.tar.gz && \
    tar -xvf helm-${HELM_VERSION}-linux-amd64.tar.gz && \
    mv linux-amd64/helm /usr/local/bin && \
    rm -f helm-${HELM_VERSION}-linux-amd64.tar.gz && \
    rm -rf linux-amd64
RUN helm init --client-only

RUN pip install --upgrade pip setuptools && \
    pip install -U wheel twine awscli crudini docker-compose==${DOCKER_COMPOSE_VERSION} && \
    python3 -m pip install --no-cache-dir twine wheel && \
    rm -rf `find / -regex '.*\.py[co]'`

COPY pypirc /root/.pypirc
