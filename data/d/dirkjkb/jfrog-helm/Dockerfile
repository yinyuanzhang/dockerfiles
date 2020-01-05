FROM docker.bintray.io/jfrog/jfrog-cli-go:latest

RUN apk add --update -t deps curl tar gzip
RUN curl -L https://storage.googleapis.com/kubernetes-helm/helm-v2.11.0-linux-amd64.tar.gz > helm.tar.gz && \
    tar -zxvf helm.tar.gz && \
    mv linux-amd64/helm /usr/local/bin/helm && \
    rm -rf helm.tar.gz && \
    helm init --client-only
