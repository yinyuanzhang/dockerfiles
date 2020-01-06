FROM docker:18.09

ENV K8S_VERSION v1.13.0
ENV AWS_CLI_VERSION 1.16.72

RUN apk add --no-cache wget python py-pip \
  && pip install awscli==${AWS_CLI_VERSION} \
  && wget --no-verbose -O /usr/local/bin/kubectl https://storage.googleapis.com/kubernetes-release/release/${K8S_VERSION}/bin/linux/amd64/kubectl \
  && chmod +x /usr/local/bin/kubectl \
  && apk del wget py-pip
