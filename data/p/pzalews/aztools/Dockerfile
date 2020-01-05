FROM mcr.microsoft.com/azure-cli:2.0.76

ENV YQ_BIN_VERSION 2.2.0
ENV TERRAFORM_VERSION 0.12.13
ENV KUBECTL_VERSION 1.13.10

ENTRYPOINT ["/entrypoint.sh"]
COPY entrypoint.sh entrypoint.sh
COPY commands.sh /commands.sh

VOLUME /work
WORKDIR /work
ENV HOME /work

RUN curl --silent --location --output /usr/local/bin/yq https://github.com/mikefarah/yq/releases/download/${YQ_BIN_VERSION}/yq_linux_amd64 && \
    chmod 755 /usr/local/bin/yq && \
    chmod +x /entrypoint.sh && \
    chmod +x /commands.sh

RUN curl --silent -o terraform.zip https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip &&\ 
    unzip terraform.zip &&\
    chmod +x terraform &&\
    mv terraform /usr/bin &&\
    rm terraform.zip

RUN curl --silent -LO https://storage.googleapis.com/kubernetes-release/release/v${KUBECTL_VERSION}/bin/linux/amd64/kubectl && \
    mv kubectl /usr/bin/kubectl && \
    chmod +x /usr/bin/kubectl


