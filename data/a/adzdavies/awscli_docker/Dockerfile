FROM alpine:latest

RUN \
  apk --no-cache --update add \
    bash \
    curl \
    less \
    groff \
    jq \
    git \
    zip \
    python \
    py-pip && \
  pip install --upgrade \
    pip \
    awscli \
    awslogs && \
  mkdir /root/.aws
