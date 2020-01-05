FROM debian:buster

MAINTAINER GoAbout <tech@goabout.com>

RUN apt-get -qq update && \
    apt-get -qq install -y --no-install-recommends \
        curl ca-certificates git gpg gpg-agent jq openssl parallel && \
    rm -rf /var/lib/apt/lists/*

ENV KUSTOMIZE_VERSION=3.2.2 \
    SOPS_VERSION=3.4.0 \
    SOPSSECRETGENERATOR_VERSION=1.1.0 \
    SOPSSECRETGENERATOR_PATH=/root/.config/kustomize/plugin/goabout.com/v1beta1/sopssecretgenerator \
    KUBECTL_VERSION=1.16.1 \
    DO_EXCLUSIVELY_COMMIT=02d45b47f8bf8e6009aa7fca9e9a7257a77a0404

RUN curl -sLo /usr/local/bin/circle-lock \
    https://raw.githubusercontent.com/bellkev/circle-lock-test/${DO_EXCLUSIVELY_COMMIT}/do-exclusively

RUN curl -sLo /usr/local/bin/kustomize \
    https://github.com/kubernetes-sigs/kustomize/releases/download/kustomize/v${KUSTOMIZE_VERSION}/kustomize_kustomize.v${KUSTOMIZE_VERSION}_linux_amd64

RUN curl -sLo /usr/local/bin/sops \
    https://github.com/mozilla/sops/releases/download/${SOPS_VERSION}/sops-${SOPS_VERSION}.linux

RUN mkdir -p ${SOPSSECRETGENERATOR_PATH} && \
    curl -sLo ${SOPSSECRETGENERATOR_PATH}/SopsSecretGenerator \
    https://github.com/goabout/kustomize-sopssecretgenerator/releases/download/v${SOPSSECRETGENERATOR_VERSION}/SopsSecretGenerator_${SOPSSECRETGENERATOR_VERSION}_linux_amd64

RUN curl -sLo /usr/local/bin/kubectl \
    https://storage.googleapis.com/kubernetes-release/release/v${KUBECTL_VERSION}/bin/linux/amd64/kubectl

RUN chmod +x /usr/local/bin/* ${SOPSSECRETGENERATOR_PATH}/*
