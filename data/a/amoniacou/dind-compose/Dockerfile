FROM docker:dind

MAINTAINER Pierre Pottié <pierre.pottie@businessdecision.com>

RUN apk add --no-cache python py-pip openssh-client git curl \
    && cd /tmp && curl -sLO https://github.com/git-lfs/git-lfs/releases/download/v2.5.1/git-lfs-linux-amd64-v2.5.1.tar.gz \
    && tar zxvf git-lfs-linux-amd64-v2.5.1.tar.gz && mv git-lfs /usr/bin/ \
    && pip install --no-cache-dir docker-compose && rm -rf /tmp/*
