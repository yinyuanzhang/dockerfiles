FROM jenkins/jnlp-slave:3.29-1

ENV KOPS_VERSION=1.9.0
ENV KUBECTL_VERSION=v1.10.2
ENV TERRAFORM_VERSION=0.12.3
ENV HELM_VERSION=v2.8.2
ENV PACKER_VERSION=1.3.4

USER root

RUN curl -LO --silent --show-error https://github.com/kubernetes/kops/releases/download/${KOPS_VERSION}/kops-linux-amd64 \
&& mv kops-linux-amd64 /usr/local/bin/kops \
&& curl -LO https://storage.googleapis.com/kubernetes-release/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl \
&& mv kubectl /usr/local/bin/kubectl \
&& curl -LO https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip \
&& unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip \
&& mv terraform /usr/local/bin/terraform \
&& curl -LO https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_linux_amd64.zip \
&& unzip packer_${PACKER_VERSION}_linux_amd64.zip \
&& mv packer /usr/local/bin/packer \
&& curl -LO https://storage.googleapis.com/kubernetes-helm/helm-${HELM_VERSION}-linux-amd64.tar.gz \
&& tar -zxvf helm-${HELM_VERSION}-linux-amd64.tar.gz \
&& mv linux-amd64/helm /usr/local/bin/helm \
&& chmod +x /usr/local/bin/kops /usr/local/bin/kubectl /usr/local/bin/terraform /usr/local/bin/helm \
&& rm -rf terraform_${TERRAFORM_VERSION}_linux_amd64.zip \
&& rm -rf helm-${HELM_VERSION}-linux-amd64.tar.gz
