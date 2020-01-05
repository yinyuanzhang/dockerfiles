ARG PYTHON_VERSION=3.7

FROM python:${PYTHON_VERSION}-alpine
LABEL Author="叶泽宇/Zéyǔ Yè <shuliyey@gmail.com>" Description="deloitte-technical-zeyu base build image" Vendor="叶泽宇" Version="1.0.0"

ARG KUBECTL_VERSION=1.14.2
ARG HELM_VERSION=2.11.0
ARG GIT_CRYPT_VERSION=0.6.0
ARG YQ_VERSION=latest
ARG TERRAFORM_VERSION=0.11.13
ARG AWS_IAM_AUTHENTICATOR_VERSION=0.4.0

ADD entrypoint.sh /
ADD install.sh /tmp/
ADD requirements.txt /tmp/

RUN apk add --update curl ca-certificates bash ncurses git g++ make openssh openssl openssl-dev expect coreutils grep gawk gnupg util-linux sed jq libxml2-dev libxslt-dev build-base screen \
  && cd /tmp \
  && pip install -r /tmp/requirements.txt \
  && /tmp/install.sh --infos="kubectl:${KUBECTL_VERSION} helm:${HELM_VERSION} git-crypt:${GIT_CRYPT_VERSION} yq:${YQ_VERSION} terraform:${TERRAFORM_VERSION} aws-iam-authenticator:${AWS_IAM_AUTHENTICATOR_VERSION}" \
  && rm -rf /tmp/* \
  && rm -rf /var/cache/apk/*

WORKDIR /root

ENTRYPOINT ["/entrypoint.sh"]
