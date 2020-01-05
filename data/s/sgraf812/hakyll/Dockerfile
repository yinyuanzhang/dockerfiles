FROM ubuntu:18.04
MAINTAINER Sebastian Graf <sgraf1337@gmail.com>

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    netbase \
    ca-certificates \
    curl \
    xz-utils \
    libz-dev \
    libgmp3-dev \
    libghc-bzlib-dev \
    git \
    ssh \
    unzip

RUN rm -rf /var/lib/apt/lists
RUN curl -L https://github.com/commercialhaskell/stack/releases/download/v1.9.3/stack-1.9.3-linux-x86_64.tar.gz | tar zx -C /tmp
RUN mv /tmp/stack-1.9.3-linux-x86_64/stack /usr/local/bin
RUN stack setup

ENTRYPOINT /bin/bash