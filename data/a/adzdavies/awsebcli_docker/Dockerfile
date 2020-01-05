FROM alpine:latest

RUN \
  apk --no-cache --upgrade add \ 
    bash \
    curl \
    less \
    groff \
    jq \
    git \
    zip \
    python \
    py-pip \
    openssh-client

RUN \
  pip install --upgrade \
    pip \
    "awsebcli==3.15.1" && \
  mkdir /root/.aws
