# -*- Dockerfile -*-
FROM ubuntu:18.04
MAINTAINER Christian Hopps <chopps@labn.net>

ENV LANG=en_US.UTF-8 \
    LC_ALL="en_US.UTF-8" \
    LC_CTYPE="en_US.UTF-8"

RUN apt-get update -qy && apt-get dist-upgrade -y && \
    # Add docker.
    apt-get install -y apt-transport-https dirmngr software-properties-common curl && \
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - && \
    add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable" && \
    apt-get update -qy && apt-get dist-upgrade -y && \
    # Add useful stuff for building/CI-testing
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    bash bash-completion bsdtar cpio curl docker-ce git iputils-ping gettext jq \
    locales locales-all make netcat-openbsd python python-dev python-pip \
    python3 python3-dev python3-pip python3-venv \
    rsync sudo snmp ssh tidy vim xsltproc \
    autoconf build-essential libev-dev libxslt-dev \
    libffi-dev libssl-dev zlib1g-dev \
    libgmp-dev zlib1g-dev libedit-dev && \
    echo en_US.UTF-8 UTF-8 >> /etc/locale.gen && \
    locale-gen && \
    pip install -U \
        coverage cryptography docker docker-compose lxml nose pyang pylint pysnmp \
        pytest pyyaml remarshal tox twine wheel && \
    pip3 install -U \
        coverage cryptography docker                lxml nose       pylint pysnmp \
        pytest pyyaml remarshal tox twine wheel && \
    # Install MIBs
    apt-get install -y snmp-mibs-downloader && download-mibs
