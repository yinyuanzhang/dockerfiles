FROM python:3.7-alpine

ARG CLOUD_SDK_VERSION=250.0.0
ENV CLOUD_SDK_VERSION=$CLOUD_SDK_VERSION

RUN apk --update add \
    postgresql-client \
    mysql-client \
    curl \
    python \
    py-crcmod \
    bash \
    libc6-compat \
    openssh-client \
    git \
    gnupg \
    inotify-tools \
    openssl \
    bash \
    ca-certificates \
  && rm -rf /var/cache/apk/*

RUN curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz \
  && tar xzf google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz \
  && rm google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz \
  && ln -s /lib /lib64 \
  && /google-cloud-sdk/install.sh --quiet \
  && ln -s /google-cloud-sdk/bin/gcloud /bin/ \
  && ln -s /google-cloud-sdk/bin/gsutil /bin/ \
  && gcloud config set core/disable_usage_reporting true \
  && gcloud config set component_manager/disable_update_check true \
  && gcloud config set metrics/environment github_docker_image \
  && gcloud --version
