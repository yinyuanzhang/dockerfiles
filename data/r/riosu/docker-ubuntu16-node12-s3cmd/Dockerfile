FROM amd64/ubuntu:16.04

ENV DEBIAN_FRONTEND noninteractive

# Install nodejs and python
RUN set -ex \
    ; apt-get update \
    ; apt install -y curl python-dev python-pip wget \
    ; curl -o nodejs.deb https://deb.nodesource.com/node_12.x/pool/main/n/nodejs/nodejs_12.10.0-1nodesource1_amd64.deb \
    ; apt-get install -y ./nodejs.deb \
    ; apt-get -y autoremove \
    ; apt-get clean \
    ; apt-get autoclean \
    ; rm nodejs.deb \
    ; rm -rf /var/lib/apt/lists/*

# Install s3cmd
RUN pip install s3cmd 

