FROM alpine:3.8

MAINTAINER "Neel Shah <nshah@capsulecares.com>"

ENV KUBECTL_VERSION=1.12.7
ENV AWS_IAM_AUTHENTICATOR_VERSION=1.12.7/2019-03-27
ENV HELM_VERSION=2.13.1

RUN apk --update add openssl curl && \
	apk upgrade && \
	\
	echo "===> Installing Kubectl..." && \
	curl -LO https://storage.googleapis.com/kubernetes-release/release/v${KUBECTL_VERSION}/bin/linux/amd64/kubectl && \
	chmod +x ./kubectl && \
	mv ./kubectl /usr/local/bin/kubectl && \
	\
	echo "===> Installing Helm..." && \
	curl -LO https://storage.googleapis.com/kubernetes-helm/helm-v${HELM_VERSION}-linux-amd64.tar.gz && \
	tar vxf helm-* && \
	mv linux-amd64/helm /usr/local/bin/helm && \
	rm -rf linux-amd64 && \
	\
	echo "===> Installing AWS IAM Authenticator..." && \
	curl -o aws-iam-authenticator https://amazon-eks.s3-us-west-2.amazonaws.com/${AWS_IAM_AUTHENTICATOR_VERSION}/bin/linux/amd64/aws-iam-authenticator && \
	chmod +x ./aws-iam-authenticator && \
	cp ./aws-iam-authenticator /usr/local/bin/aws-iam-authenticator && \
	\
	echo "===> Installing Git..." && \
	apk --update add git && \
	\
	echo "===> Installing Bash..." && \
	apk --update add bash


ENTRYPOINT ["sh", "-c", "kubectl version --short --client"]
