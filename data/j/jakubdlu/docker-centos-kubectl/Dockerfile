FROM centos:7
MAINTAINER jakub.dlugolecki@gmail.com

ENV KUBECTL_URL="https://storage.googleapis.com/kubernetes-release/release/v1.12.1/bin/linux/amd64/kubectl"
ENV HELM_URL="https://storage.googleapis.com/kubernetes-helm/helm-v2.9.1-linux-amd64.tar.gz"

RUN yum -y install git gettext && \
    curl -L "${KUBECTL_URL}" -o /usr/local/bin/kubectl && \
    chmod 755 /usr/local/bin/kubectl && \
    curl -Lsf "${HELM_URL}" | tar -xvz --strip-components=1 -C /usr/local/bin linux-amd64/helm
