FROM alpine:latest
MAINTAINER "Matthew de Verteuil <matthew@kiratalent.com>"

ENV TERRAFORM_VERSION=0.11.7
ENV TERRAFORM_SHA256SUM=6b8ce67647a59b2a3f70199c304abca0ddec0e49fd060944c26f666298e23418

ENV TFLINT_VERSION=0.7.0

RUN apk add --update git curl openssh && \
    curl https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip > terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \
    echo "${TERRAFORM_SHA256SUM}  terraform_${TERRAFORM_VERSION}_linux_amd64.zip" > terraform_${TERRAFORM_VERSION}_SHA256SUMS && \
    sha256sum -cs terraform_${TERRAFORM_VERSION}_SHA256SUMS && \
    unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip -d /bin && \
    rm -f terraform_${TERRAFORM_VERSION}_linux_amd64.zip

RUN curl -Lo tflint.zip https://github.com/wata727/tflint/releases/download/v${TFLINT_VERSION}/tflint_linux_amd64.zip && \
    unzip tflint.zip -d /bin && \
    rm -f tflint.zip

