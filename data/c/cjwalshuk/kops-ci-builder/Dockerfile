#Losely based on devopsil/kops-docker
FROM alpine:3.6

ENV KUBECTL_VERSION 1.15.5
ENV KOPS_VERSION 1.14.0

ENV HELM_VERSION=3.0.1
ENV RELEASE_ROOT="https://get.helm.sh"
ENV RELEASE_FILE="helm-v${HELM_VERSION}-linux-amd64.tar.gz"

#https://get.helm.sh/helm-v3.0.1-linux-arm64.tar.gz

#install kubectl
RUN apk add --update \
    curl \
    jq \
    vim \
    tar \
    sed \
    git \
    bash \
    wget \
    util-linux pciutils usbutils coreutils binutils findutils grep \
    ca-certificates \
    openssh-client \
    && curl -s -L https://storage.googleapis.com/kubernetes-release/release/v${KUBECTL_VERSION}/bin/linux/amd64/kubectl -o /usr/bin/kubectl \
    && chmod +x /usr/bin/kubectl

#install kops
RUN  curl -s -L https://github.com/kubernetes/kops/releases/download/${KOPS_VERSION}/kops-linux-amd64 -o /usr/bin/kops \
     && chmod +x /usr/bin/kops

RUN curl -s -L -o /usr/bin/aws-iam-authenticator https://amazon-eks.s3-us-west-2.amazonaws.com/1.10.3/2018-07-26/bin/linux/amd64/aws-iam-authenticator \
    && chmod +x /usr/bin/aws-iam-authenticator

RUN curl -L ${RELEASE_ROOT}/${RELEASE_FILE} |tar xvz && \
    mv linux-amd64/helm /usr/bin/helm && \
    chmod +x /usr/bin/helm

CMD ["/bin/bash"]
