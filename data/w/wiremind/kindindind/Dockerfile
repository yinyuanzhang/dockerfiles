FROM docker:dind

ENV HELM_VERSION v2.14.0
ENV KIND_VERSION 0.2.1
ENV KUBECTL_VERSION v1.12.0


RUN apk add --no-cache --update curl git build-base python3-dev libffi-dev libressl-dev musl-dev \
    && curl -Lo kubectl https://storage.googleapis.com/kubernetes-release/release/$KUBECTL_VERSION/bin/linux/amd64/kubectl && chmod +x kubectl && mv kubectl /usr/local/bin/ \
    && curl -Lo kind https://github.com/kubernetes-sigs/kind/releases/download/$KIND_VERSION/kind-linux-amd64 && chmod +x kind && mv kind /usr/local/bin/ \
    && curl -o /tmp/helm-$HELM_VERSION-linux-amd64.tar.gz https://storage.googleapis.com/kubernetes-helm/helm-$HELM_VERSION-linux-amd64.tar.gz && tar -zxvf /tmp/helm-$HELM_VERSION-linux-amd64.tar.gz -C /tmp && mv /tmp/linux-amd64/helm /bin/helm && rm -rf /tmp
