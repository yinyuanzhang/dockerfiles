FROM ubuntu:18.04

RUN apt-get update && apt-get install -y --no-install-recommends \
  python3-pip curl unzip git jq \
  && rm -rf /var/lib/apt/lists/*

RUN curl https://releases.hashicorp.com/terraform/0.11.14/terraform_0.11.14_linux_amd64.zip -O \
  && unzip terraform_0.11.14_linux_amd64.zip -d /usr/bin/ \
  && chmod +x /usr/bin/terraform \
  && rm -f terraform_0.11.14_linux_amd64.zip

RUN curl https://github.com/gruntwork-io/terragrunt/releases/download/v0.18.7/terragrunt_linux_amd64 -O -L \
  && mv terragrunt_linux_amd64 /usr/bin/terragrunt \
  && chmod +x /usr/bin/terragrunt


