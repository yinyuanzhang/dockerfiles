FROM docker:18.03.0-ce-git
MAINTAINER Kosuke Arisawa <arisawa@gmail.com>

RUN apk add --no-cache \
      py-pip \
      jq \
      ruby=2.4.5-r0 \
      ruby-bundler

RUN pip install --upgrade pip
RUN pip install awscli
