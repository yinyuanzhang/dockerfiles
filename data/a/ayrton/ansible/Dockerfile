FROM ubuntu:bionic

LABEL maintainer="Ayrton <root@ayr-ton.net>"

RUN apt-get update \
    && apt-get install -y python3 python3-pip openssh-client \
    && pip3 install ansible jinja2 pyaml \
    && mkdir ~/.ssh && echo "UserKnownHostsFile=/dev/null" > ~/.ssh/config \
    && echo "StrictHostKeyChecking no" > ~/.ssh/config \
    && ansible --version
