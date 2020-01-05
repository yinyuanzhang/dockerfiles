FROM ubuntu:latest

COPY mkspiffs /opt/mkspiffs
COPY ca-cert/ca.der /workspace/certs/ca.der

RUN apt-get update -qq && apt-get install -qq -y --no-install-recommends \
    awscli openssl

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /workspace
