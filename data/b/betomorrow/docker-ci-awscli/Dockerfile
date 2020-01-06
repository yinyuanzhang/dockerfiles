FROM alpine:3.6

RUN apk --no-cache add \
      bash \
      curl \
      jq \
      groff \
      py-pip \
      python &&\
    pip install --upgrade \
      pip \
      awscli &&\
    mkdir ~/.aws

VOLUME ["~/.aws"]

ENTRYPOINT ["/bin/bash", "-l", "-c"] 
