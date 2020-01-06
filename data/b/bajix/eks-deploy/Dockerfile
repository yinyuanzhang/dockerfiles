FROM alpine:3.10

RUN set -x && apk add --no-cache curl python3 bash && \
    pip3 install awscli && \
    curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.13.4/bin/linux/amd64/kubectl && \
    chmod +x ./kubectl && \
    mv ./kubectl /usr/local/bin/kubectl && \
    curl -LO https://get.helm.sh/helm-v3.0.2-linux-amd64.tar.gz && \
    tar -zxvf helm-v3.0.2-linux-amd64.tar.gz && \
    mv linux-amd64/helm /usr/local/bin/helm && \
    curl -LO https://amazon-eks.s3-us-west-2.amazonaws.com/1.14.6/2019-08-22/bin/linux/amd64/aws-iam-authenticator && \
    chmod +x ./aws-iam-authenticator && \
    mv aws-iam-authenticator /usr/local/bin/aws-iam-authenticator && \
    aws --version && \
    kubectl version --client && \
    helm version --client && \
    aws-iam-authenticator version

CMD ["/bin/bash"]
