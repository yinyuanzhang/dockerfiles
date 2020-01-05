FROM ruby:2.5.1-alpine
MAINTAINER "Steve Burns <steve@tacoshell.sh>"

ENV PACKER_VERSION=1.2.3
ENV ENV PACKER_SHA256SUM=822fe76c2dfe699f187ef8c44537d10453a1545db620e40b345cf6991a690f7d

RUN apk add --update git bash wget openssl

ADD https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_linux_amd64.zip ./
ADD https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_SHA256SUMS ./

RUN sed -i '/.*linux_amd64.zip/!d' packer_${PACKER_VERSION}_SHA256SUMS
RUN sha256sum -cs packer_${PACKER_VERSION}_SHA256SUMS
RUN unzip packer_${PACKER_VERSION}_linux_amd64.zip -d /bin
RUN rm -f packer_${PACKER_VERSION}_linux_amd64.zip

ENTRYPOINT ["/bin/bash"]