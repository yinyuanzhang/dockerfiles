FROM alpine:3.5
MAINTAINER Andreas Berg <andreas@andreas-berg.se>

# Install packages needed to build
RUN apk add --update --no-cache \
  bash \
  ca-certificates \
  curl \
  python \
  py-pip \
  wget \
  && pip install -U awscli

# Install hugo.
ARG HUGO_VERSION=0.20.5
ARG HUGO_SHA256=c34a6b52137761ce931eb2acbb99eaa18d30ded471ae72a656d59207276e643c

# Rember sha256sum (and md5sum) expect 2 spaces in front of the filename on alpine...
RUN curl -Ls https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_Linux-64bit.tar.gz \
       -o /tmp/hugo.tar.gz \
  && echo "${HUGO_SHA256}  /tmp/hugo.tar.gz" | sha256sum -c - \
  && tar xf /tmp/hugo.tar.gz -C /tmp \
  && mv /tmp/hugo /usr/bin/hugo \
  && rm -rf /tmp/hugo* \
