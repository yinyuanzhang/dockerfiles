FROM alpine:3.8

ARG KUBE_LATEST_VERSION="v1.10.0"

ADD https://storage.googleapis.com/kubernetes-release/release/${KUBE_LATEST_VERSION}/bin/linux/amd64/kubectl /usr/local/bin/
RUN chmod +x /usr/local/bin/kubectl
