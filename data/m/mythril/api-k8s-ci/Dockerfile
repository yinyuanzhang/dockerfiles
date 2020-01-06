FROM golang:1.11-alpine3.8 as getter

RUN apk add git && go get -u sigs.k8s.io/kind


FROM azuresdk/azure-cli-python

ENV KUBECTL_VERSION=v1.12.0
ENV HELM_VERSION=v2.11.0
ENV DOCKER_VERSION=18.06.1

RUN wget https://storage.googleapis.com/kubernetes-release/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl && \
  chmod a+x ./kubectl && \
  mv ./kubectl /usr/local/bin

RUN wget https://storage.googleapis.com/kubernetes-helm/helm-${HELM_VERSION}-linux-amd64.tar.gz && \
  tar zxfv helm-${HELM_VERSION}-linux-amd64.tar.gz && \
  chmod a+x ./linux-amd64/helm && \
  mv ./linux-amd64/helm /usr/local/bin && \
  rm -rf ./linux-amd64 helm-${HELM_VERSION}-linux-amd64.tar.gz

RUN wget https://amazon-eks.s3-us-west-2.amazonaws.com/1.10.3/2018-07-26/bin/linux/amd64/aws-iam-authenticator && \
  chmod a+x ./aws-iam-authenticator && \
  mv ./aws-iam-authenticator /usr/local/bin

RUN wget https://github.com/roboll/helmfile/releases/download/v0.40.1/helmfile_linux_amd64 && \
  chmod a+x ./helmfile_linux_amd64 && \
  mv ./helmfile_linux_amd64 /usr/local/bin/helmfile

RUN wget https://github.com/mozilla/sops/releases/download/3.1.1/sops-3.1.1.linux && \
  chmod a+x ./ && \
  mv ./sops-3.1.1.linux /usr/local/bin/sops

RUN wget https://download.docker.com/linux/static/stable/x86_64/docker-${DOCKER_VERSION}-ce.tgz && \
  tar zxfv docker-${DOCKER_VERSION}-ce.tgz && \
  chmod a+x ./docker/docker && \
  mv ./docker/docker /usr/local/bin && \
  rm -rf ./docker docker-${DOCKER_VERSION}-ce.tgz

RUN apk -Uuv add --update --no-cache \
  bash\
  curl \
  git \
  gnupg \
  openssl \
  socat

ENV HELM_HOME=/root/.helm

RUN mkdir -p $HELM_HOME/plugins

RUN helm plugin install https://github.com/databus23/helm-diff

RUN helm plugin install https://github.com/futuresimple/helm-secrets

COPY ./mythrilKey-cipher.asc /root
COPY ./mythrilSecretKey-cipher.asc /root

COPY --from=getter /go/bin/kind /usr/local/bin/kind
