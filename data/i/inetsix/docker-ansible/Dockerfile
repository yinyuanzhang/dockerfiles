FROM python:2.7.16-stretch

LABEL maintainer="Thomas Grimonet"
LABEL com.example.version="1.0"
LABEL vendor1="Inetsix"
LABEL com.example.release-date="2019-01-11"
LABEL com.example.version.is-production="True"

RUN apt-get update -qq && \
    DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -qq -y git vim sshpass openssh-client && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    pip install ansible && \
    pip install jxmlease
