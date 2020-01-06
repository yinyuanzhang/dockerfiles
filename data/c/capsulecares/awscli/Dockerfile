FROM python:3.7-alpine3.8

MAINTAINER "Neel Shah <nshah@capsulecares.com>"

ARG AWS_CLI_VERSION=1.16.260
ENV AWS_CLI_VERSION=${AWS_CLI_VERSION}

RUN apk add curl

RUN echo "===> Upgading package manager..." && \
	pip install --upgrade pip && \
	\
	echo "===> Installing AWS CLI..." && \
	pip install awscli==${AWS_CLI_VERSION}

RUN curl -o /usr/local/bin/aws-iam-authenticator https://amazon-eks.s3-us-west-2.amazonaws.com/1.12.7/2019-03-27/bin/linux/amd64/aws-iam-authenticator \
	&& chmod 755 /usr/local/bin/aws-iam-authenticator \
	&& curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl \
	&& chmod +x kubectl \
	&& mv kubectl /usr/local/bin

ENTRYPOINT ["sh", "-c", "aws --version"]
