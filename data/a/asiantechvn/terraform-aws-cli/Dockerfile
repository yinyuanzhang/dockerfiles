FROM alpine:latest

LABEL maintainer asiantechvn

ENV TERRAFORM_VERSION=0.12.18
ENV AWS_CLI_VERSION=1.16.309
#RUN echo "http://dl-cdn.alpinelinux.org/alpine/latest-stable/community" >> /etc/apk/repositories
RUN apk -U add \
    docker \
    docker-compose \
    ca-certificates \
    make \
    git \
    openssh \
    bash \
    dash \
    python3 \
    curl \
    groff \
    wget && \
    curl -o /usr/bin/jq -L https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64 && chmod +x /usr/bin/jq && \
    pip3 install awscli==${AWS_CLI_VERSION} && \
    rm -rf /var/cache/apk/*

RUN wget -q https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip -O terraform.zip && \
    unzip terraform.zip -d /bin && \
    rm -f terraform.zip