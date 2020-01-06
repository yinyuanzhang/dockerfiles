# Build ARGS
ARG ALPINE_VERSION=3.6
ARG TERRAFORM_VERSION=0.11.13

# Set Alpine version
FROM alpine:${ALPINE_VERSION} AS alpine

# Get Terraform binary
FROM hashicorp/terraform:${TERRAFORM_VERSION} AS tf

# Get Terragrunt binary
FROM alpine AS tfg

ARG TERRAGRUNT_VERSION=v0.18.3

RUN apk --no-cache --update add \
    ca-certificates \
    wget \
    && wget --output-document=/bin/terragrunt --no-verbose "https://github.com/gruntwork-io/terragrunt/releases/download/${TERRAGRUNT_VERSION}/terragrunt_linux_amd64" \
    && chmod +x /bin/terragrunt

# Build deploy image
FROM alpine as final

RUN apk --no-cache --update add \
    make \
    git \
    openssh-client \
    && mkdir -p /usr/local/tmp \
    && echo 'terragrunt = {}' >  /usr/local/tmp/terraform.tfvars \
    && touch /usr/local/tmp/fake.tf

COPY --from=tf /bin/terraform /bin/terraform
COPY --from=tfg /bin/terragrunt /bin/terragrunt
COPY --from=tfg /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/ca-certificates.crt

WORKDIR /data

ENTRYPOINT ["/bin/terragrunt"]

CMD ["version", "--terragrunt-config", "/usr/local/tmp/terraform.tfvars", "--terragrunt-working-dir", "/usr/local/tmp"]
