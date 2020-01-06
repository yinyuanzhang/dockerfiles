FROM maven:3.5-jdk-8-slim

RUN apt-get update && \
    apt-get -y install python curl unzip git jq dnsutils&& \
    cd /tmp && \
    curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-bundle.zip" && \
    unzip awscli-bundle.zip && \
    ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws && \
    rm awscli-bundle.zip && rm -rf awscli-bundle && \
    apt-get -y purge curl unzip && \
    apt -y autoremove && \
    rm -vrf /var/lib/apt/lists/* /tmp/* 
