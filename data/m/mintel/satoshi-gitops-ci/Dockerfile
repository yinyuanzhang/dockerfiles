##
# Builder Golang
##

FROM golang:1.12-stretch AS go-builder

# Until terraform0.12 need tfjson2
RUN go get github.com/justinm/tfjson2
RUN go get github.com/kvz/json2hcl

# No recent release.
# https://github.com/jsonnet-bundler/jsonnet-bundler/issues/45
RUN go get github.com/jsonnet-bundler/jsonnet-bundler/cmd/jb

# No releases.
RUN go get github.com/brancz/gojsontoyaml

##
# Builder Debian
##

FROM debian:10-slim as deb-builder

WORKDIR /tmp

ENV DEBIAN_FRONTEND=noninteractive \
    LANG=C.UTF-8 \
    LANGUAGE=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    LC_TYPE=C.UTF-8 \
    GITCRYPT_VERSION=0.6.0 \
    GITCRYPT_SHA256=777c0c7aadbbc758b69aff1339ca61697011ef7b92f1d1ee9518a8ee7702bb78 \
    JSONNET_VERSION=0.12.1 \
    JSONNET_SHA256=257c6de988f746cc90486d9d0fbd49826832b7a2f0dbdb60a515cc8a2596c950

RUN apt-get -y update && \
    apt-get -y install locales && \
    localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8 && \
    apt-get -y install \
      apt-transport-https \
      curl \
      g++ \
      libssl-dev \
      make && \
      curl -L https://github.com/google/jsonnet/archive/v${JSONNET_VERSION}.tar.gz -o /tmp/jsonnet.tar.gz && \
      echo "$JSONNET_SHA256  jsonnet.tar.gz" | sha256sum -c && \
      tar zxvf /tmp/jsonnet.tar.gz  -C /tmp && \
      cd /tmp/jsonnet-$JSONNET_VERSION && make && mv jsonnet /usr/local/bin && chmod a+x /usr/local/bin/jsonnet && cd - && \
      rm -rf /tmp/jsonnet.tar.gz /tmp/jsonnet-$JSONNET_VERSION && \
      curl -L https://github.com/AGWA/git-crypt/archive/$GITCRYPT_VERSION.tar.gz -o /tmp/git-crypt.tar.gz && \
      echo "$GITCRYPT_SHA256  git-crypt.tar.gz" | sha256sum -c && \
      tar zxvf /tmp/git-crypt.tar.gz  -C /tmp && \
      cd /tmp/git-crypt-$GITCRYPT_VERSION && make && make install PREFIX=/usr/local && cd - && \
      rm -rf /tmp/git-crypt.tar.gz /tmp/git-crypt-$GITCRYPT_VERSION && \
      apt-get -y autoremove && apt-get -y clean

##
# Main Image
##

FROM debian:10-slim

LABEL vendor="Mintel"
LABEL maintainer "fciocchetti@mintel.com"

ENV DEBIAN_FRONTEND=noninteractive \
    LANG=C.UTF-8 \
    LANGUAGE=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    LC_TYPE=C.UTF-8

# Clean docs
RUN echo "path-exclude /usr/share/doc/*" > /etc/dpkg/dpkg.cfg.d/01_nodoc && \
    echo "path-include /usr/share/doc/*/copyright" >> /etc/dpkg/dpkg.cfg.d/01_nodoc && \
    echo "path-exclude /usr/share/man/*" >> /etc/dpkg/dpkg.cfg.d/01_nodoc && \
    echo "path-exclude /usr/share/groff/*" >> /etc/dpkg/dpkg.cfg.d/01_nodoc && \
    echo "path-exclude /usr/share/info/*" >> /etc/dpkg/dpkg.cfg.d/01_nodoc && \
    echo "path-exclude /usr/share/lintian/*" >> /etc/dpkg/dpkg.cfg.d/01_nodoc && \
    echo "path-exclude /usr/share/linda/*" >> /etc/dpkg/dpkg.cfg.d/01_nodoc  && \
    find /usr/share/doc -depth -type f ! -name copyright|xargs rm || true && \
    find /usr/share/doc -empty|xargs rmdir || true && \
    rm -rf /usr/share/man/* /usr/share/groff/* /usr/share/info/* && \
    rm -rf /usr/share/lintian/* /usr/share/linda/* /var/cache/man/*

WORKDIR /tmp

RUN apt-get -y update && \
    apt-get -y install locales && \
    localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8 && \
    apt-get -y install \
      apt-transport-https \
      bash \
      bash-completion \
      bsdmainutils \
      dnsutils \
      ca-certificates \
      curl \
      gawk \
      gettext-base \
      git \
      gnupg2 \
      make \
      openssl \
      openssh-client \
      pass \
      procps \
      python3-virtualenv \
      python3-pip \
      python3-pkg-resources \
      software-properties-common \
      wget \
      unzip \
      pwgen \
      ssss && \
    wget -q -O- https://download.docker.com/linux/debian/gpg | apt-key add - && \
    wget -q -O- https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && \
    echo "deb [arch=amd64] https://download.docker.com/linux/debian stretch stable" >> /etc/apt/sources.list && \
    echo "deb https://packages.cloud.google.com/apt cloud-sdk-stretch -c -s) main" >> /etc/apt/sources.list.d/google-cloud-sdk.list && \
    apt-get -y update && \
    apt-get -y install docker-ce-cli google-cloud-sdk && \
    apt-get -y purge aptitude g++ libssl-dev gcc libc-dev && \
    apt-get -y autoremove && apt-get -y clean


ENV YAML2JSON_VERSION=1.3 \
    YAML2JSON_SHA256=e792647dd757c974351ea4ad35030852af97ef9bbbfb9594f0c94317e6738e55 \
    YQ_VERSION=2.3.0 \
    YQ_SHA256=97b2c61ae843a429ce7e5a2c470cfeea1c9e9bf317793b41983ef228216fe31b \
    KUSTOMIZE_VERSION=3.2.1 \
    KUSTOMIZE_SHA256=a91b38778945e8a63fe70bc7522703a94c1d572d5dcee245e96647359e1fd04b \
    KUBECTL_VERSION=1.13.11 \
    KUBECTL_SHA256=825b7e68bb316bf6b1c776d16336a3a2049afae8c664b233de06d6505c8d1ca5 \
    VAULT_VERSION=1.1.3 \
    VAULT_SHA256=293b88f4d31f6bcdcc8b508eccb7b856a0423270adebfa0f52f04144c5a22ae0 \
    VAULT_SIDEKICK_VERSION=0.3.10 \
    VAULT_SIDEKICK_SHA256=484c6ae5f47ba01989b176f3eb7ce565c3edcce31522187c74129d58cbf829b5 \
    DUMB_INIT_VERSION=1.2.2 \
    DUMB_INIT_SHA256=37f2c1f0372a45554f1b89924fbb134fc24c3756efaedf11e07f599494e0eff9 \
    KIND_VERSION=0.5.1 \
    KIND_SHA256=9a64f1774cdf24dad5f92e1299058b371c4e3f09d2f9eb281e91ed0777bd1e13 \
    TERRAFORM_VERSION=0.12.5 \
    TERRAFORM_SHA256=babb4a30b399fb6fc87a6aa7435371721310c2e2102a95a763ef2c979ab06ce2 \
    TERRAGRUNT_VERSION=0.19.12 \
    TERRAGRUNT_SHA256=a605a8ee8133fdf952c43a3a3483a8e4a0f168c602291d6e5d63758f9dd83022 \
    TERRAFORM_CT_PROVIDER_VERSION=0.4.0 \
    TERRAFORM_CT_PROVIDER_SHA256=b9ddb666fd566f865ff93368f46101ab64f0f2a1c7f44e1a924153277ef3a005 \
    KUBECFG_VERSION=0.13.0 \
    KUBECFG_SHA256=1edb1068ad95b9c22c222d7fb5a033cded22dcfe2530964d5197ab8a6376a6e7 \
    JQ_VERSION=1.5 \
    JQ_SHA256=c6b3a7d7d3e7b70c6f51b706a3b90bd01833846c54d32ca32f0027f00226ff6d \
    BASH_UNIT_VERSION=1.6.1 \
    BASH_UNIT_SHA256=596c2bcbcebcc5611e3f2e1458b0f4be1adad8f91498b20e97c9f7634416950f \
    TEST_SSL_VERSION=3.0rc5 \
    TEST_SSL_SHA256=6118f08b88c0075f39820296f0d76889165dd67e64dbfdfd1104d6d122a938c9 \
    KUBESEAL_VERSION=0.5.1 \
    KUBESEAL_SHA256=c8a9dd32197c6ce3420a0d2c78dd7b3963bae03f53c9c1d032d0279fabfe2cb9 \
    CONFTEST_VERSION=0.11.0 \
    CONFTEST_SHA256=935ce17d12041af23d0fa98135ddc56c32108ef7e522bb608c62bddbf8611881


#yaml2json
RUN set -e \
    && wget -q -O /usr/local/bin/yaml2json https://github.com/bronze1man/yaml2json/releases/download/v${YAML2JSON_VERSION}/yaml2json_linux_amd64 \
    && chmod +x /usr/local/bin/yaml2json \
    && cd /usr/local/bin \
    && echo "$YAML2JSON_SHA256  yaml2json" | sha256sum -c \
#yq
    && wget -q -O /usr/local/bin/yq https://github.com/mikefarah/yq/releases/download/${YQ_VERSION}/yq_linux_amd64 \
    && chmod +x /usr/local/bin/yq \
    && cd /usr/local/bin \
    && echo "$YQ_SHA256  yq" | sha256sum -c \
# kustomize
    && wget -q -O /usr/local/bin/kustomize https://github.com/kubernetes-sigs/kustomize/releases/download/kustomize%2Fv${KUSTOMIZE_VERSION}/kustomize_kustomize.v${KUSTOMIZE_VERSION}_linux_amd64 \
    && chmod +x /usr/local/bin/kustomize \
    && cd /usr/local/bin \
    && echo "$KUSTOMIZE_SHA256  kustomize" | sha256sum -c \
# kubectl
    && wget -q -O /usr/local/bin/kubectl https://storage.googleapis.com/kubernetes-release/release/v${KUBECTL_VERSION}/bin/linux/amd64/kubectl \
    && chmod +x /usr/local/bin/kubectl \
    && cd /usr/local/bin \
    && echo "$KUBECTL_SHA256  kubectl" | sha256sum -c \
    && cd /tmp \
# vault
    && wget -q -O /tmp/vault.zip https://releases.hashicorp.com/vault/${VAULT_VERSION}/vault_${VAULT_VERSION}_linux_amd64.zip \
    && echo "$VAULT_SHA256  vault.zip" | sha256sum -c \
    && unzip vault.zip -d /usr/local/bin \
    && chmod +x /usr/local/bin/vault \
    && rm -f vault.zip \
# vault-sidekick
    && wget -q -O /usr/local/bin/vault-sidekick https://github.com/UKHomeOffice/vault-sidekick/releases/download/v${VAULT_SIDEKICK_VERSION}/vault-sidekick_linux_amd64 \
    && chmod +x /usr/local/bin/vault-sidekick \
    && cd /usr/local/bin \
    && echo "$VAULT_SIDEKICK_SHA256  vault-sidekick" | sha256sum -c \
# dumb-init
    && wget -q -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v${DUMB_INIT_VERSION}/dumb-init_${DUMB_INIT_VERSION}_amd64 \
    && chmod +x /usr/local/bin/dumb-init \
    && cd /usr/local/bin \
    && echo "$DUMB_INIT_SHA256  dumb-init" | sha256sum -c \
# terraform
    && cd /tmp \
    && wget -q https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip -O /tmp/terraform.zip \
    && echo "$TERRAFORM_SHA256  terraform.zip" | sha256sum -c \
    && unzip terraform.zip -d /usr/local/bin \
    && chmod +x /usr/local/bin/terraform \
    && rm -f terraform.zip \
# terragrunt
    && wget -q https://github.com/gruntwork-io/terragrunt/releases/download/v${TERRAGRUNT_VERSION}/terragrunt_linux_amd64 -O /tmp/terragrunt \
    && echo "$TERRAGRUNT_SHA256  terragrunt" | sha256sum -c \
    && mv /tmp/terragrunt /usr/local/bin \
    && chmod +x /usr/local/bin/terragrunt \
# terraform-ct-provider
    && wget -q  https://github.com/coreos/terraform-provider-ct/releases/download/v${TERRAFORM_CT_PROVIDER_VERSION}/terraform-provider-ct-v${TERRAFORM_CT_PROVIDER_VERSION}-linux-amd64.tar.gz -O /tmp/terraform-ct-provider.tar.gz \
    && echo "$TERRAFORM_CT_PROVIDER_SHA256  terraform-ct-provider.tar.gz" | sha256sum -c \
    && tar zxvf /tmp/terraform-ct-provider.tar.gz  -C /tmp \
    && mv /tmp/terraform-provider-ct-v${TERRAFORM_CT_PROVIDER_VERSION}-linux-amd64/terraform-provider-ct /usr/local/bin \
    && rm -f /tmp/terraform-ct-provider.tar.gz \
# bash_unit
    && wget -q https://github.com/pgrange/bash_unit/archive/v${BASH_UNIT_VERSION}.tar.gz -O /tmp/bash_unit.tar.gz \
    && echo "$BASH_UNIT_SHA256  bash_unit.tar.gz" | sha256sum -c \
    && tar zxvf /tmp/bash_unit.tar.gz  -C /tmp \
    && mv /tmp/bash_unit-${BASH_UNIT_VERSION}/bash_unit /usr/local/bin \
    && chmod a+x /usr/local/bin \
    && rm -f /tmp/bash_unit.tar.gz \
# kubecfg
    && wget -q https://github.com/ksonnet/kubecfg/releases/download/v${KUBECFG_VERSION}/kubecfg-linux-amd64 -O /tmp/kubecfg \
    && chmod +x /tmp/kubecfg \
    && echo "$KUBECFG_SHA256  kubecfg" | sha256sum -c \
    && mv /tmp/kubecfg /usr/local/bin \
# kubeseal
    && wget -q https://github.com/bitnami-labs/sealed-secrets/releases/download/v${KUBESEAL_VERSION}/kubeseal-linux-amd64 -O /tmp/kubeseal \
    && chmod +x /tmp/kubeseal \
    && echo "$KUBESEAL_SHA256  kubeseal" | sha256sum -c \
    && mv /tmp/kubeseal /usr/local/bin \
# JQ
    && wget -q https://github.com/stedolan/jq/releases/download/jq-${JQ_VERSION}/jq-linux64 -O /tmp/jq \
    && chmod +x /tmp/jq \
    && echo "$JQ_SHA256  jq" | sha256sum -c \
    && mv /tmp/jq /usr/local/bin \
# testssl.sh
    && wget -q https://github.com/drwetter/testssl.sh/archive/${TEST_SSL_VERSION}.tar.gz -O /tmp/testssl.tar.gz \
    && echo "$TEST_SSL_SHA256  testssl.tar.gz" | sha256sum -c \
    && tar zxvf /tmp/testssl.tar.gz  -C /tmp \
    && mv /tmp/testssl.sh-${TEST_SSL_VERSION} /tmp/testssl.sh \
    && rm -f /tmp/testssl.tar.gz \
# Kind
    && wget -q -O /usr/local/bin/kind https://github.com/kubernetes-sigs/kind/releases/download/v${KIND_VERSION}/kind-linux-amd64 \
    && cd /usr/local/bin \
    && chmod +x /usr/local/bin/kind \
    && echo "$KIND_SHA256  kind" | sha256sum -c \
# conftest
    && wget -q https://github.com/instrumenta/conftest/releases/download/v${CONFTEST_VERSION}/conftest_${CONFTEST_VERSION}_Linux_x86_64.tar.gz -O /tmp/conftest.tar.gz \
    && cd /tmp \
    && echo "$CONFTEST_SHA256  conftest.tar.gz" | sha256sum -c \
    && tar zxvf /tmp/conftest.tar.gz  -C /tmp \
    && mv /tmp/conftest /usr/local/bin/conftest \
    && chmod a+x /usr/local/bin/conftest \
    && cd - \
    && rm -f /tmp/conftest*

# Install LETSENCRYPT staging fake root ca
RUN set -e \
    && curl -o /usr/local/share/ca-certificates/fakelerootx1.crt https://letsencrypt.org/certs/fakelerootx1.pem \
    && curl -o /usr/local/share/ca-certificates/fakeleintermediatex1.crt https://letsencrypt.org/certs/fakeleintermediatex1.pem \
    && update-ca-certificates

COPY --from=mintel/k8s-yaml-splitter:0.1.0 /k8s-yaml-splitter /usr/local/bin/k8s-yaml-splitter
COPY --from=gcr.io/google_containers/pause-amd64:3.1 /pause /
COPY --from=openpolicyagent/opa:0.12.1 /opa /usr/local/bin/opa
COPY --from=prom/prometheus:v2.13.0 /bin/promtool /usr/local/bin/promtool

COPY --from=go-builder /go/bin/tfjson2 /usr/local/bin/tfjson2
COPY --from=go-builder /go/bin/gojsontoyaml /usr/local/bin/gojsontoyaml
COPY --from=go-builder /go/bin/json2hcl /usr/local/bin/json2hcl
COPY --from=go-builder /go/bin/jb /usr/local/bin/jb

COPY --from=deb-builder /usr/local/bin/jsonnet /usr/local/bin/jsonnet
COPY --from=deb-builder /usr/local/bin/git-crypt /usr/local/bin/git-crypt
#
#
USER 0

RUN useradd -ms /bin/bash mintel
USER mintel

RUN set -e \
    && pip3 install yamllint docker-compose

# Configure support for terraform-ct-provider
RUN echo 'providers {\n \
ct = "/usr/local/bin/terraform-provider-ct"\n \
}\n' >> /home/mintel/.terraformrc

# Extend PATH for mintel user
RUN echo 'PATH=$HOME/.local/bin:$PATH' >> /home/mintel/.bashrc

USER 0
COPY resources/ /
USER mintel

ENV PATH=/home/mintel/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin \
    DOCKER_HOST_ALIAS=docker \
    KIND_NODES=1 \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8 \
    LC_ALL=en_US.UTF-8 \
    LC_TYPE=en_US.UTF-8

# Don't use a real entrypoint 
ENTRYPOINT ["/usr/bin/env"]
