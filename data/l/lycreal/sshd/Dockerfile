FROM ubuntu:18.04

MAINTAINER Lycreal <jgsly123@gmail.com>

RUN apt-get update \
 && apt-get install -y --no-install-recommends openssh-server \
 && rm -rf /var/lib/apt/lists/*

COPY entrypoint.sh /entrypoint

RUN chmod +x /entrypoint && \
    mkdir /var/run/sshd /root/.ssh

ENTRYPOINT ["/entrypoint"]
