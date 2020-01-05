FROM hashicorp/terraform:0.11.13
LABEL MAINTAINER="Olivier Nsabimana <onsabimana@energylink.io>"

ENV CHAMBER_VERSION=v1.15.0
ADD https://github.com/segmentio/chamber/releases/download/$CHAMBER_VERSION/chamber-$CHAMBER_VERSION-linux-amd64 /usr/bin/chamber

ENV AIVEN_PROVIDER_VERSION=v1.0.8
ADD https://github.com/aiven/terraform-provider-aiven/releases/download/$AIVEN_PROVIDER_VERSION/terraform-provider-aiven-linux_amd64 /root/.terraform.d/plugins/terraform-provider-aiven_$AIVEN_PROVIDER_VERSION

# Add zip (for building null resources)
# Add libc6-compat (for aiven provider - See https://github.com/hashicorp/docker-hub-images/pull/63)
RUN \
   apk --no-cache add zip libc6-compat \
   && chmod +x /usr/bin/chamber \
   && chmod +x /root/.terraform.d/plugins/terraform-provider-aiven_$AIVEN_PROVIDER_VERSION

