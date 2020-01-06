# Build Image
FROM debian:stable-slim as builder

# Install build dependencies
RUN DEBIAN_FRONTEND=noninteractive apt-get update -qq \
	&& DEBIAN_FRONTEND=noninteractive apt-get install -qq -y --no-install-recommends --no-install-suggests \
		ca-certificates \
		curl \
		git \
		unzip

ARG TF_VERSION=0.12.10
ARG TG_VERSION=v0.20.4

# Get Terraform
RUN curl -S -L -O \
		  https://releases.hashicorp.com/terraform/${TF_VERSION}/terraform_${TF_VERSION}_linux_amd64.zip \
  && ls -la \
	&& unzip terraform_${TF_VERSION}_linux_amd64.zip \
	&& mv terraform /usr/bin/terraform \
	&& chmod +x /usr/bin/terraform

# Get Terragrunt
RUN curl -sS -L \
      https://github.com/gruntwork-io/terragrunt/releases/download/${TG_VERSION}/terragrunt_linux_amd64 \
      -o /usr/bin/terragrunt \
	&& chmod +x /usr/bin/terragrunt

# Target Image
FROM alpine:3.9

LABEL \
	maintainer="Fabio todaro <ft@ovalmoney.com>" \
	repo="https://github.com/OvalMoney/docker-terragrunt"

RUN set -eux \
	&& apk add --no-cache git

COPY --from=builder /usr/bin/terraform /usr/bin/terraform
COPY --from=builder /usr/bin/terragrunt /usr/bin/terragrunt

CMD ["terragrunt", "--version"]
