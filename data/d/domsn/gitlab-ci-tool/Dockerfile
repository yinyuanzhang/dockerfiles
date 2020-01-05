FROM docker:stable-git

MAINTAINER Domsn Lee <domsn.lee@gmail.com>

ENV KUBE_LATEST_VERSION="v1.12.6"

RUN apk update \
 && apk add ca-certificates curl gettext vim openssh-client git bind-tools net-tools bash \
 && curl -L https://storage.googleapis.com/kubernetes-release/release/${KUBE_LATEST_VERSION}/bin/linux/amd64/kubectl -o /usr/local/bin/kubectl \
 && chmod +x /usr/local/bin/kubectl \
 && rm /var/cache/apk/*
