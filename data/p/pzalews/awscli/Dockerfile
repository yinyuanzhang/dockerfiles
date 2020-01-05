FROM alpine:3.10

ENV YQ_BIN_VERSION 2.2.0
ENV TERRAFORM_VERSION 0.12.13
ENV AWSCLI_VERSION 1.16.280
ENV KUBECTL_VERSION 1.16.2
ENV AWS_IAM_AUTH_VERSION 0.4.0

COPY entrypoint.sh entrypoint.sh
COPY commands.sh /commands.sh
ENTRYPOINT ["/entrypoint.sh"]

RUN mkdir /aws
VOLUME /aws
WORKDIR /aws
ENV HOME /aws

RUN apk update && apk add --update --no-cache ca-certificates gnupg openssl curl bash && \
    apk --update --no-cache add python3  && \
    pip3 install awscli==${AWSCLI_VERSION} && \
    rm -rf /var/cache/apk/* && \
    curl --silent --location --output /usr/local/bin/yq https://github.com/mikefarah/yq/releases/download/${YQ_BIN_VERSION}/yq_linux_amd64 && \
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

RUN curl --silent -LO https://github.com/kubernetes-sigs/aws-iam-authenticator/releases/download/v${AWS_IAM_AUTH_VERSION}/aws-iam-authenticator_0.4.0_linux_amd64 && \
    mv aws-iam-authenticator_0.4.0_linux_amd64 /usr/bin/aws-iam-authenticator && \
    chmod +x /usr/bin/aws-iam-authenticator

RUN curl --silent --location "https://github.com/weaveworks/eksctl/releases/download/latest_release/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp && \
    mv /tmp/eksctl /usr/bin && \
    chmod +x /usr/bin/eksctl
 

