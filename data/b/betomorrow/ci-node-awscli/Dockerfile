FROM node:10-alpine

RUN apk --no-cache add \
      bash \
      curl \
      jq \
      groff \
      git \
      py-pip \
      python &&\
    pip install --upgrade \
      pip \
      awscli &&\
    mkdir ~/.aws

VOLUME ["~/.aws"]

ENTRYPOINT ["/bin/bash", "-l", "-c"]