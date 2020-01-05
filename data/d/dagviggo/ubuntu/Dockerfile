FROM ubuntu:latest


RUN apt-get update

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \
    curl \
    net-tools \
    docker \
    build-essential \
    apt-utils \
    vim \
    mtr \
    traceroute \
    iputils-ping \
    groff \
    apache2-utils \
    netcat \
    wget \
    socat \
    dnsutils \
    htop \
    iptables \
    python3-pip

RUN cd /usr/bin && \
    curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl && \
    chmod a+x ./kubectl

RUN pip3 install awscli

