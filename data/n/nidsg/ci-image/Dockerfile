FROM docker:stable-git

ENV TERRAFORM_VERSION="0.11.10" \
    GCREDSTASH_VERSION="0.3.5" \
    GCREDSTASH_SHA256="462c78808c2dd2a87db61ee87228fbf53f9b638c14b1dc96fa10947ad444f579"

RUN apk --no-cache add --update \
        bash \
        ca-certificates \
        curl \
        jq \
        make \
        perl \
        py-pip \
        tar \
        unzip && \
    rm -rf /var/cache/apk/*

RUN pip --no-cache-dir install \
        awscli \
        boto3 \
        docker-compose \
        ecs-deploy

RUN cd /tmp && \
    curl -o terraform.zip https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \
    unzip terraform.zip -d /usr/bin && \
    cd /tmp && \
    curl -sLo gcredstash.gz https://github.com/winebarrel/gcredstash/releases/download/v${GCREDSTASH_VERSION}/gcredstash-v${GCREDSTASH_VERSION}-linux-amd64.gz && \
    echo "${GCREDSTASH_SHA256}  gcredstash.gz" | sha256sum -c - && gunzip gcredstash.gz && \
    mv gcredstash /usr/local/bin/gcredstash && chmod +x /usr/local/bin/gcredstash && \
    rm -rf /tmp/*
