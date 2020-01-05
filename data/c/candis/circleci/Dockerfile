FROM debian as extractor
# Instead of installing the full docker-ce distribution, which also pulls in
# the DKMS module and other stuff for running the server.
# Only install the docker client binary.
ENV DOCKER_VERSION=18.09.6
RUN apt update && apt install -y curl \
    && curl https://download.docker.com/linux/static/stable/x86_64/docker-${DOCKER_VERSION}.tgz | \
    tar xzvf - -C /

FROM debian
COPY --from=extractor /docker/docker /usr/bin/docker
# Install additional programming languages and tools
RUN apt update \
    && apt install -y \
    bash \
    coreutils \
    curl \
    git \
    jq \
    openssh-client \
    python \
    python-pip \
    sudo \
    zip \
    && python2 -m pip install --upgrade pip
ENV AWSCLI_VERSION=1.16.215
RUN pip install awscli==${AWSCLI_VERSION}
WORKDIR /circleci
# Install Go
# From: https://github.com/docker-library/golang/blob/2f6469ffe955721dd25e4cbb3013506659998aad/1.12/stretch/Dockerfile
RUN apt-get update && apt-get install -y --no-install-recommends \
    g++ \
    gcc \
    libc6-dev \
    make \
    wget \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*
ENV GOLANG_VERSION 1.12.9
RUN set -eux; \
    \
    # this "case" statement is generated via "update.sh"
    dpkgArch="$(dpkg --print-architecture)"; \
    case "${dpkgArch##*-}" in \
    amd64) goRelArch='linux-amd64'; goRelSha256='ac2a6efcc1f5ec8bdc0db0a988bb1d301d64b6d61b7e8d9e42f662fbb75a2b9b' ;; \
    armhf) goRelArch='linux-armv6l'; goRelSha256='0d9be0efa9cd296d6f8ab47de45356ba45cb82102bc5df2614f7af52e3fb5842' ;; \
    arm64) goRelArch='linux-arm64'; goRelSha256='3606dc6ce8b4a5faad81d7365714a86b3162df041a32f44568418c9efbd7f646' ;; \
    i386) goRelArch='linux-386'; goRelSha256='c40824a3e6c948b8ecad8fe9095b620c488b3d8d6694bdd48084a4798db4799a' ;; \
    ppc64el) goRelArch='linux-ppc64le'; goRelSha256='2e74c071c6a68446c9b00c1717ceeb59a826025b9202b3b0efed4f128e868b30' ;; \
    s390x) goRelArch='linux-s390x'; goRelSha256='2aac6de8e83b253b8413781a2f9a0733384d859cff1b89a2ad0d13814541c336' ;; \
    *) goRelArch='src'; goRelSha256='ab0e56ed9c4732a653ed22e232652709afbf573e710f56a07f7fdeca578d62fc'; \
    echo >&2; echo >&2 "warning: current architecture ($dpkgArch) does not have a corresponding Go binary release; will be building from source"; echo >&2 ;; \
    esac; \
    \
    url="https://golang.org/dl/go${GOLANG_VERSION}.${goRelArch}.tar.gz"; \
    wget -O go.tgz "$url"; \
    echo "${goRelSha256} *go.tgz" | sha256sum -c -; \
    tar -C /usr/local -xzf go.tgz; \
    rm go.tgz; \
    \
    if [ "$goRelArch" = 'src' ]; then \
    echo >&2; \
    echo >&2 'error: UNIMPLEMENTED'; \
    echo >&2 'TODO install golang-any from jessie-backports for GOROOT_BOOTSTRAP (and uninstall after build)'; \
    echo >&2; \
    exit 1; \
    fi; \
    \
    export PATH="/usr/local/go/bin:$PATH"; \
    go version
ENV GOPATH /go
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH
RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"
# Install Terraform
ENV TERRAFORM_VERSION=0.11.14
RUN wget "https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip" && \
    ls && \
    unzip ./terraform_0.11.14_linux_amd64.zip && \
    ls && \
    mv ./terraform /usr/bin/ && \
    terraform version
# Install aws-iam-authenticator - A tool to authenticate to Kubernetes using AWS IAM credentials
RUN curl -o aws-iam-authenticator https://amazon-eks.s3-us-west-2.amazonaws.com/1.14.6/2019-08-22/bin/linux/amd64/aws-iam-authenticator && \
    curl -o aws-iam-authenticator.sha256 https://amazon-eks.s3-us-west-2.amazonaws.com/1.14.6/2019-08-22/bin/linux/amd64/aws-iam-authenticator.sha256 &&\
    openssl sha1 -sha256 aws-iam-authenticator && \
    chmod +x ./aws-iam-authenticator && \
    mv ./aws-iam-authenticator /usr/bin/ && \
    aws-iam-authenticator help
# Install yq for editing YAML files
RUN GO111MODULE=on go get -u github.com/mikefarah/yq@d05391e
# Install security checking tool
RUN go get github.com/securego/gosec/cmd/gosec
# Install Minio CLI tool
RUN wget https://dl.min.io/client/mc/release/linux-amd64/mc && \
    chmod +x mc && \
    mv ./mc /usr/bin/
# Install Node.js
RUN curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
RUN sudo apt update && sudo apt install nodejs -y
RUN node --version
# Install security scanner for JS/Node.js
RUN npm install -g retire
# Add additional CLI tools (kubectl, helm and istioctl)
COPY ./scripts/install_kubectl.sh ./scripts/install_kubectl.sh
RUN ./scripts/install_kubectl.sh
COPY ./scripts/install_helm_client.sh ./scripts/install_helm_client.sh
RUN ./scripts/install_helm_client.sh
COPY ./scripts/install_istio.sh ./scripts/install_istio.sh
RUN ./scripts/install_istio.sh
# Install Spinnaker CLI tools
RUN curl -LO https://storage.googleapis.com/spinnaker-artifacts/spin/1.12.0/linux/amd64/spin \
    && chmod +x spin \
    && sudo mv spin /usr/bin/spin
# Add custom CircleCI helper scripts
ADD scripts/commands/build_helm_package.sh /usr/bin/build_helm_package
ADD scripts/commands/build_push_image.sh /usr/bin/build_push_image
ADD scripts/commands/jira_notify.sh /usr/bin/jira_notify
ADD scripts/commands/security_check.sh /usr/bin/security_check
ADD scripts/commands/start_deployment_pipeline.sh /usr/bin/start_deployment_pipeline
ADD scripts/commands/sync_spinnaker_config.sh /usr/bin/sync_spinnaker_config
ADD scripts/commands/tag_prod_release.sh /usr/bin/tag_prod_release
ADD scripts/commands/sync_infra_configs /usr/bin/node_sync_infra_configs
RUN cd /usr/bin/node_sync_infra_configs && npm install && npm -g install
