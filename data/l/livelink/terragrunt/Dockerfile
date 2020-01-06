FROM hashicorp/terraform:0.12.13
MAINTAINER LiveLink Systems Engineering <syseng@livelinktechnology.net>
# Based on https://github.com/bootswithdefer/terragrunt

ENV TERRAGRUNT_VERSION=0.21.4
ENV TERRAGRUNT_TFPATH=/bin/terraform
RUN apk add curl

RUN curl -sL https://github.com/gruntwork-io/terragrunt/releases/download/v$TERRAGRUNT_VERSION/terragrunt_linux_amd64 -o /bin/terragrunt && chmod +x /bin/terragrunt

COPY docker-entrypoint.sh /

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["terragrunt"]
