FROM ubuntu:latest

ENV TERRAFORM_VERSION=0.12.6
RUN apt-get update && \
    apt-get install -y curl ca-certificates unzip git jq --no-install-recommends && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN mkdir $HOME/.kube && \
    mkdir $HOME/.helm && \
    mkdir $HOME/.helm/plugins && \
    mkdir -p ~/.terraform.d/plugins/linux_amd64/

# Kubectl
RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl && \
    chmod +x ./kubectl && \
    mv ./kubectl /usr/local/bin/kubectl

# Terraform
ADD https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip ./
RUN unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip -d /usr/local/bin/ && \
    rm -f terraform_${TERRAFORM_VERSION}_linux_amd64.zip

# Terraform Provider Aiven
RUN AIVEN_VERSION=$(curl --silent "https://api.github.com/repos/aiven/terraform-provider-aiven/releases/latest" | \
    grep '"tag_name":' | \
    sed -E 's/.*"([^"]+)".*/\1/') && \
    curl -sOL "https://github.com/aiven/terraform-provider-aiven/releases/download/"$AIVEN_VERSION'/terraform-provider-aiven-linux_amd64' && \
    chmod +x ./terraform-provider-aiven-linux_amd64 && \
    mv terraform-provider-aiven-linux_amd64 ~/.terraform.d/plugins/linux_amd64/terraform-provider-aiven_$AIVEN_VERSION

# Helm
RUN curl -LO https://get.helm.sh/helm-v3.0.1-linux-amd64.tar.gz && \
    tar -zxvf helm-v3.0.1-linux-amd64.tar.gz && \
    mv linux-amd64/helm /usr/local/bin/ && \
    rm -rf linux-amd64 helm-v3.0.1-linux-amd64.tar.gz && \
    helm plugin install https://github.com/databus23/helm-diff --version v3.0.0-rc.7
# helmfile
RUN HELMFILE_VERSION=$(curl --silent "https://api.github.com/repos/roboll/helmfile/releases/latest" | \
    grep '"tag_name":' | \
    sed -E 's/.*"([^"]+)".*/\1/') && \
    curl -sOL "https://github.com/roboll/helmfile/releases/download/"$HELMFILE_VERSION'/helmfile_linux_amd64' && \
    chmod +x ./helmfile_linux_amd64 && \
    mv helmfile_linux_amd64 /usr/local/bin/helmfile
RUN curl -sL https://aka.ms/InstallAzureCLIDeb | bash
