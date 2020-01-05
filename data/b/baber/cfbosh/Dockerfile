# Dockerfile for BOSH/CF operations
FROM ubuntu:16.04
MAINTAINER Alexey Zakharov <baber@mosga.net>
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y build-essential zlibc zlib1g-dev ruby ruby-dev openssl libxslt-dev libxml2-dev libssl-dev libreadline6 libreadline6-dev libyaml-dev libsqlite3-dev sqlite3 wget curl vim jq python3-yaml netcat dnsutils git
RUN wget https://s3.amazonaws.com/bosh-cli-artifacts/bosh-cli-2.0.28-linux-amd64 && chmod +x bosh-cli* && mv bosh-cli* /usr/local/bin/bosh
RUN curl -sL "https://cli.run.pivotal.io/stable?release=linux64-binary&source=github" | tar -zx && mv cf /usr/local/bin/
RUN wget https://releases.hashicorp.com/vault/0.7.3/vault_0.7.3_linux_amd64.zip && unzip vault*zip && mv vault /usr/local/bin && rm vault*zip
