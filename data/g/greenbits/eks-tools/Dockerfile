FROM alpine AS base

ARG KUBECTL_VERSION=v1.13.0
ARG HELM_VERSION=2.12.1
ARG AWS_IAM_AUTHENTICATOR_VERSION=1.10.3/2018-07-26

RUN apk add --update --no-cache curl ca-certificates openssl

WORKDIR /work
RUN curl -LO https://storage.googleapis.com/kubernetes-helm/helm-v${HELM_VERSION}-linux-amd64.tar.gz
RUN echo "$(curl -Ls https://storage.googleapis.com/kubernetes-helm/helm-v${HELM_VERSION}-linux-amd64.tar.gz.sha256)  helm-v${HELM_VERSION}-linux-amd64.tar.gz" | tee helm-v${HELM_VERSION}-linux-amd64.tar.gz.sha256
RUN sha256sum -cw helm-v${HELM_VERSION}-linux-amd64.tar.gz.sha256
RUN tar xvf helm-v${HELM_VERSION}-linux-amd64.tar.gz

RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl
RUN echo "$(curl -Ls https://storage.googleapis.com/kubernetes-release/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl.sha512)  kubectl" | tee kubectl.sha512
RUN sha512sum -cw kubectl.sha512

# sha256sum does not like AWS's stored sha256 file.  We need to rebuild it
RUN curl -LO https://amazon-eks.s3-us-west-2.amazonaws.com/${AWS_IAM_AUTHENTICATOR_VERSION}/bin/linux/amd64/aws-iam-authenticator
RUN curl -Ls https://amazon-eks.s3-us-west-2.amazonaws.com/${AWS_IAM_AUTHENTICATOR_VERSION}/bin/linux/amd64/aws-iam-authenticator.sha256 | awk '{ print $1, "", $2 }' | tee aws-iam-authenticator.sha256
RUN sha256sum -cw aws-iam-authenticator.sha256

WORKDIR /prepared
RUN cp /work/linux-amd64/tiller .
RUN cp /work/linux-amd64/helm .
RUN cp /work/kubectl .
RUN cp /work/aws-iam-authenticator .
RUN chmod +x *

FROM alpine
RUN apk add --update --no-cache ca-certificates openssl git openssh
COPY --from=base /prepared /usr/bin
