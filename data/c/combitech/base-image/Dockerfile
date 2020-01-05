FROM ubuntu:18.04

RUN apt-get update && apt-get install -y \
    bash \
    bc \
    binutils \
    build-essential \
    bzip2 \
    cpio \
    file \
    g++ \
    gcc \
    git \
    gosu \
    gzip \
    make \
    patch \
    perl \
    python \
    rsync \
    sed \
    tar \
    unzip \
    wget

ENV SSH_AUTH_SOCK=/tmp/ssh-agent

COPY entrypoint.sh /usr/local/bin/entrypoint.sh

RUN chmod 755 /usr/local/bin/entrypoint.sh

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

RUN mkdir -p /workspace
WORKDIR /workspace

CMD ["/bin/bash"]