FROM node:12-alpine

ENV GOOGLE_CLOUD_SDK_VERSION 272.0.0

ARG GHR_VERSION=v0.12.1

# Packages for Signal Noise workflows
RUN apk add --no-cache vim tar gzip jq curl

# Packages for CircleCi compatibility
RUN apk add --no-cache bash git openssh ca-certificates

# Packages as install helpers for the SDKs
RUN apk add --no-cache python py-crcmod py-pip libc6-compat openssh-client

# Add GCloud SDK
ENV PATH /google-cloud-sdk/bin:$PATH
RUN curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-${GOOGLE_CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \
  tar xzf google-cloud-sdk-${GOOGLE_CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \
  rm google-cloud-sdk-${GOOGLE_CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \
  ln -s /lib /lib64 && \
  gcloud config set core/disable_usage_reporting true && \
  gcloud config set component_manager/disable_update_check true && \
  gcloud config set metrics/environment github_docker_image

# Add AWS CLI
RUN pip --no-cache-dir install awscli && \
  rm -rf /var/cache/apk/*

# Adds GitHub Release functionality
# Reference: https://github.com/gavinkflam/ghr-alpine/blob/master/Dockerfile
RUN \
  # Prepare for download context directory
  mkdir /tmp/ghr_download && \
  cd /tmp/ghr_download && \
  # Download the tarball from Github
  wget https://github.com/tcnksm/ghr/releases/download/${GHR_VERSION}/ghr_${GHR_VERSION}_linux_amd64.tar.gz -O - | tar xz && \
  # Copy the binary and change owner
  cp ghr_${GHR_VERSION}_linux_amd64/ghr /usr/local/bin/ghr && \
  chown root:root /usr/local/bin/ghr && \
  # Remove the download context directory
  rm -rf /tmp/ghr_download

VOLUME ["/root/.config"]
