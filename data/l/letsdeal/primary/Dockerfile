ARG DOCKER_COMPOSE_VERSION=1.25.0-rc1

FROM alpine:latest

ARG DOCKER_VERSION=18.09.8
ARG HELM_VERSION=2.14.2
ARG KUBECTL_VERSION=1.15.1
ARG SENTRY_CLI_VERSION=1.49.0
ARG TERRAFORM_VERSION=0.12.6

RUN apk add --no-cache openssl

# https://docs.docker.com/engine/installation/linux/docker-ce/binaries/#install-static-binaries
RUN wget -q -O - https://download.docker.com/linux/static/stable/x86_64/docker-${DOCKER_VERSION}.tgz | tar -x -f - -z --strip-components=1 -v docker/docker

# https://docs.helm.sh/using_helm/#from-the-binary-releases
RUN wget -q -O - https://storage.googleapis.com/kubernetes-helm/helm-v${HELM_VERSION}-linux-amd64.tar.gz | tar -x -f - -z --strip-components=1 -v linux-amd64/helm

# https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-kubectl-on-linux
RUN wget -q -O kubectl https://storage.googleapis.com/kubernetes-release/release/v${KUBECTL_VERSION}/bin/linux/amd64/kubectl && chmod +x kubectl

# https://sentry.io/get-cli/
RUN wget -q -O sentry-cli https://downloads.sentry-cdn.com/sentry-cli/${SENTRY_CLI_VERSION}/sentry-cli-Linux-x86_64 && chmod +x sentry-cli

# https://www.terraform.io/intro/getting-started/install.html
RUN wget -q -O terraform_${TERRAFORM_VERSION}_linux_amd64.zip https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip \
 && unzip -o terraform_${TERRAFORM_VERSION}_linux_amd64.zip terraform

FROM docker/compose:${DOCKER_COMPOSE_VERSION}-alpine AS docker-compose

FROM google/cloud-sdk:255.0.0-alpine

RUN apk add --no-cache git lua5.3 lua-cjson lua-http openssl

COPY deploy-notifier.lua /usr/local/bin/deploy-notifier
COPY --from=0 docker /usr/local/bin/
COPY --from=docker-compose /usr/local/bin/docker-compose /usr/local/bin/docker-compose
COPY --from=0 helm /usr/local/bin/
COPY --from=0 kubectl /usr/local/bin/
COPY --from=0 sentry-cli /usr/local/bin/
COPY --from=0 terraform /usr/local/bin/
