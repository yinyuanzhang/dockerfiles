FROM ubuntu:16.04

ENV TERRAFORM_VERSION=0.11.0 \
    CLOUD_SDK_VERSION=179.0.0 \
    TERRAFORM_INIT_PLUGINS_DIR="" \
    GOOGLE_CREDENTIALS_FILE="" \
    PATH="/google-cloud-sdk/bin:$PATH"

RUN apt-get update && apt-get dist-upgrade -y
RUN apt-get install -y curl python-dev unzip
RUN curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \
    tar xzf google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \
    rm google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz
RUN gcloud config set core/disable_usage_reporting true && \
    gcloud config set component_manager/disable_update_check true

RUN gcloud components install beta --quiet
RUN gcloud components install kubectl
RUN curl -O https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \
  unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \
  mv terraform /usr/local/bin/
RUN mkdir /terraform

WORKDIR /terraform

COPY ["docker-entrypoint.sh", "/usr/local/bin/"]

ENTRYPOINT  ["/usr/local/bin/docker-entrypoint.sh"]

CMD ["/bin/bash"]
