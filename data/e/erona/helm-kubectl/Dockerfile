FROM alpine:3.9

ENV KUBE_VERSION="v1.13.4"
ENV HELM_VERSION="v2.13.1"

RUN apk add --no-cache ca-certificates \
    && wget -q https://storage.googleapis.com/kubernetes-release/release/${KUBE_VERSION}/bin/linux/amd64/kubectl -O /usr/local/bin/kubectl \
    && chmod +x /usr/local/bin/kubectl \
    && wget -q https://storage.googleapis.com/kubernetes-helm/helm-${HELM_VERSION}-linux-amd64.tar.gz -O - | tar -xzp && mv linux-amd64/helm linux-amd64/tiller /usr/local/bin/ \
    && rm -rf linux-amd64
