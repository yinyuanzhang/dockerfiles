FROM docker:stable-git
ENV HELM_VERSION=2.12.2 \
    KUBERNETES_VERSION=1.10.1
RUN apk add --update --no-cache \
  openssl \
  curl \
  tar \
  gzip \
  bash \
  ca-certificates \
  git; \
  \
# Install Helm and Kubectl
  \
  curl -L -o /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub; \
  curl -L -O https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.28-r0/glibc-2.28-r0.apk; \
  apk add glibc-2.28-r0.apk; \
  rm glibc-2.28-r0.apk; \
  curl "https://kubernetes-helm.storage.googleapis.com/helm-v${HELM_VERSION}-linux-amd64.tar.gz" | tar zx; \
  mv linux-amd64/helm /usr/bin/; \
  mv linux-amd64/tiller /usr/bin/; \
  curl -L -o /usr/bin/kubectl "https://storage.googleapis.com/kubernetes-release/release/v${KUBERNETES_VERSION}/bin/linux/amd64/kubectl"; \
  chmod +x /usr/bin/kubectl;