FROM runatlantis/atlantis:latest

LABEL authors="Julian Einhaus"

ENV TERRAGRUNT_VERSION=v0.21.6

RUN curl -s -Lo terragrunt https://github.com/gruntwork-io/terragrunt/releases/download/${TERRAGRUNT_VERSION}/terragrunt_linux_amd64 && \
    chmod +x terragrunt && \
    mv terragrunt /usr/local/bin && \
    chown atlantis:atlantis /usr/local/bin/terragrunt
