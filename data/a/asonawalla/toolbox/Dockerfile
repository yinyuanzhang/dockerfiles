FROM ubuntu:latest

RUN apt-get update \
    && apt-get install --yes \
     openssh-server \
     sudo \
    && rm -r /var/lib/apt/lists/*

RUN mkdir -p /run/sshd

ENTRYPOINT ["/usr/sbin/sshd", "-D", "-e"]