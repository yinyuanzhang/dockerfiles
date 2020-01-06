FROM ubuntu:16.04

LABEL maintainer Lee

RUN apt-get update || true && \
    apt-get install -y \
    curl wget \
    pkg-config && \
    rm -rf /var/lib/dpkg/info/* /var/lib/apt/lists/*

RUN wget -c https://dl.k8s.io/v1.14.0/kubernetes.tar.gz

RUN wget -c https://dl.k8s.io/v1.14.0/kubernetes-client-linux-amd64.tar.gz

RUN wget -c https://dl.k8s.io/v1.14.0/kubernetes-server-linux-amd64.tar.gz

RUN wget -c https://dl.k8s.io/v1.14.0/kubernetes-node-linux-arm64.tar.gz


CMD ["/bin/bash"]
