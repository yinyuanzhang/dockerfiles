FROM golang:1.12.4
LABEL authors="Mat Baker <mbaker@energylink.io, Olivier Nsabimana <onsabimana@energylink.io>"

ENV TERRAFORM_VERSION=0.11.7

RUN \
     apt-get update -y \
  && apt-get install -y zip \
  && curl https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip > terraform_${TERRAFORM_VERSION}_linux_amd64.zip \
  && unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip -d /bin \
  && rm -f terraform_${TERRAFORM_VERSION}_linux_amd64.zip

RUN \
  go get github.com/segmentio/terraform-docs \
  && cp /go/bin/terraform-docs /bin \
  && chmod +x /bin/terraform-docs

ENTRYPOINT [ "sh" ]
