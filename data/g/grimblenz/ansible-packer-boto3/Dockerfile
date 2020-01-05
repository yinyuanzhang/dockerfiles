FROM ubuntu:18.04
MAINTAINER "Andrew Stockman <andrew.stockman@ihsmarkit.com>"

ENV PACKER_VERSION=1.4.0
ENV PACKER_SHA256SUM=7505e11ce05103f6c170c6d491efe3faea1fb49544db0278377160ffb72721e4
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update \
 && apt install -y openssl ssh unzip python-pip python-boto3 \
 && rm -rf /var/lib/apt/lists/* \
 && pip install ansible==2.7.15

ADD https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_linux_amd64.zip ./
ADD https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_SHA256SUMS ./

RUN sed -i '/.*linux_amd64.zip/!d' packer_${PACKER_VERSION}_SHA256SUMS
RUN sha256sum -c packer_${PACKER_VERSION}_SHA256SUMS
RUN unzip packer_${PACKER_VERSION}_linux_amd64.zip -d /bin
RUN rm -f packer_${PACKER_VERSION}_linux_amd64.zip
