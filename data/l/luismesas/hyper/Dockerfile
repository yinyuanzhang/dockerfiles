FROM ubuntu:xenial
MAINTAINER Luis Mesas <luis.mesas@intelygenz.com>
WORKDIR /root

# Update CA Certificates
RUN apt-get update && \
    apt-get install -y --reinstall \
        ca-certificates && \
    apt-get clean && \
    apt-get autoremove && \
    rm -rf /var/lib/{apt,dpkg,cache,log}/ /tmp/* /var/tmp/*

# Installs wget
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        wget && \
	apt-get clean && \
	apt-get autoremove && \
	rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Installs hyper
RUN wget https://hyper-install.s3.amazonaws.com/hyper-linux-x86_64.tar.gz && \
    tar xzf hyper-linux-x86_64.tar.gz && \
    rm hyper-linux-x86_64.tar.gz && \
    ln -s /root/hyper /usr/bin/hyper

WORKDIR /app
