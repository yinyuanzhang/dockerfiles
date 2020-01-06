FROM alpine:3.4

MAINTAINER Sergii Nuzhdin <ipaq.lw@gmail.com>

ENV KUBE_LATEST_VERSION=v1.11.2
ENV HELM_VERSION=v2.11.0
ENV HELM_FILENAME=helm-${HELM_VERSION}-linux-amd64.tar.gz


RUN apk add --update ca-certificates \
 && apk add --update gettext tar gzip \
 && apk add --update curl  \
 && curl -L https://storage.googleapis.com/kubernetes-release/release/${KUBE_LATEST_VERSION}/bin/linux/amd64/kubectl -o /usr/local/bin/kubectl \
 && curl -L https://storage.googleapis.com/kubernetes-helm/${HELM_FILENAME} | tar xz && mv linux-amd64/helm /bin/helm && rm -rf linux-amd64 \
 && chmod +x /usr/local/bin/kubectl \
 && rm /var/cache/apk/*

CMD ["helm"]
