FROM alpine:latest
MAINTAINER MarsYang

# Create dirs and users
RUN mkdir -p /opt/atlassian/bitbucketci/agent/build
RUN adduser -s /bin/sh -u 1000 -D pipelines

RUN apk update \
    && apk add \
     wget \
     curl \
     git \
     openssh-client \
     ansible \
     # for base64
     coreutils

# Default to UTF-8 file.encoding
ENV LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    LANGUAGE=C.UTF-8

WORKDIR /opt/atlassian/bitbucketci/agent/build
ENTRYPOINT /bin/sh
