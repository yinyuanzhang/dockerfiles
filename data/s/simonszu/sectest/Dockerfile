
FROM debian:latest

RUN apt-get update \
    && apt-get install -y \
    telnet \
    nmap \
    ssh \
    netcat \
    traceroute \
    mtr \
    htop \
    dnsutils \
    iputils-ping \
    stress \
    netstress \
    curl \
    && rm -rf /var/lib/apt/lists/*
    
RUN mkdir /data

RUN useradd -ms /bin/bash executor
USER executor
WORKDIR /home/executor

ENTRYPOINT ["tail", "-f", "/dev/null"]
