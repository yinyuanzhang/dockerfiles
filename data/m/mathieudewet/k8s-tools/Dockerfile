FROM google/cloud-sdk:220.0.0-alpine

ENV HELM_VERSION="v2.9.1"

RUN mkdir /root/project
WORKDIR /root/project

RUN apk add openssl docker && \
    curl https://raw.githubusercontent.com/kubernetes/helm/master/scripts/get | bash -s -- --version ${HELM_VERSION} && \
    curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl && \
    chmod +x ./kubectl && \
    mv ./kubectl /usr/local/bin/kubectl

