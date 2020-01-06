FROM alpine:3.8

RUN apk add --update --no-cache \
        bash \
        ca-certificates \
        curl \
        git \
        jq \
        less \
        python \
        py-pip \
        unzip \
 && pip install --upgrade pip \
 && pip install --upgrade setuptools distribute awscli s3cmd awsebcli python-magic

ENV TERRAFORM_VERSION=0.11.11
RUN cd /tmp \
 && curl -sSL -o terraform_${TERRAFORM_VERSION}_linux_amd64.zip https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip \
 && curl -sSL -o terraform_${TERRAFORM_VERSION}_SHA256SUMS https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_SHA256SUMS \
 && cat terraform_${TERRAFORM_VERSION}_SHA256SUMS | grep terraform_${TERRAFORM_VERSION}_linux_amd64.zip > terraform_SHA256SUMS \
 && sha256sum -cs terraform_SHA256SUMS \
 && unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip -d /usr/bin \
 && rm -rf terraform_${TERRAFORM_VERSION}_*

VOLUME ["/app"]
WORKDIR /app
