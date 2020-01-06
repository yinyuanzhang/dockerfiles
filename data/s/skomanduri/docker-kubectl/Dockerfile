FROM alpine:3.6

# Install kubectl
# Note: Latest version may be found on:
# https://aur.archlinux.org/packages/kubectl-bin/
ADD https://storage.googleapis.com/kubernetes-release/release/v1.8.1/bin/linux/amd64/kubectl /usr/local/bin/kubectl

ENV HOME=/config

RUN set -x && \
    apk add --no-cache curl ca-certificates python3-dev build-base gcc yaml-dev openssl util-linux && \
    chmod +x /usr/local/bin/kubectl && \
    \
    # Create non-root user (with a randomly chosen UID/GUI) and home directory /config
    adduser kubectl -Du 2342 -h /config && \
    \
    # Basic check it works.
    kubectl version --client && \
    \
    # Install civis client
    pip3 install civis

USER kubectl
WORKDIR /config
