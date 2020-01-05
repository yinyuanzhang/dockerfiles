FROM debian:stretch-slim

ENV DEBIAN_FRONTEND noninteractive

RUN apt update && \
    apt dist-upgrade -y && \
    apt install -y apt-transport-https lsb-release ca-certificates wget gpg && \
    apt clean && rm -r /var/lib/apt/lists/*

