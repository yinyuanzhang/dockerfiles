FROM liksi/ansible:2.8.5-ubuntu18.04

MAINTAINER Liksi <info@liksi.fr>

ARG TERRAFORM_INVENTORY_VERSION=0.9
ARG TERRAFORM_VERSION=0.12.9

RUN apt-get update \
    && apt-get install -y curl unzip \
    && rm -rf /var/lib/apt/lists/*

RUN curl -LO https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip \
    && unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip \
    && chmod +x ./terraform \
    && mv ./terraform /usr/local/bin/terraform \
    && rm terraform_${TERRAFORM_VERSION}_linux_amd64.zip

RUN curl -LO https://github.com/adammck/terraform-inventory/releases/download/v${TERRAFORM_INVENTORY_VERSION}/terraform-inventory_${TERRAFORM_INVENTORY_VERSION}_linux_amd64.zip \
    && unzip terraform-inventory_${TERRAFORM_INVENTORY_VERSION}_linux_amd64.zip \
    && chmod +x ./terraform-inventory \
    && mv ./terraform-inventory /usr/local/bin/terraform-inventory \
    && rm terraform-inventory_${TERRAFORM_INVENTORY_VERSION}_linux_amd64.zip
