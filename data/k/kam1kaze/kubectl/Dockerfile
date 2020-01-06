FROM alpine:3.9

# curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt
ENV KUBECTL_VERSION 1.14.2

# Install kubectl
RUN set -x && \
    wget https://storage.googleapis.com/kubernetes-release/release/v${KUBECTL_VERSION}/bin/linux/amd64/kubectl -O /usr/local/bin/kubectl && \
    apk add --update --no-cache ca-certificates jq bash && \
    chmod +x /usr/local/bin/kubectl

ENTRYPOINT /usr/local/bin/kubectl
