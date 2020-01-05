FROM ubuntu:18.04
MAINTAINER Hermann Krumrey <hermann@krumreyh.com>

ADD VERSION .
RUN apt update && \
    apt install -y \
    python3 python3-pip python3-venv \
    texlive \
    ssh rsync \
    gitstats \
    build-essential patch ruby-dev zlib1g-dev liblzma-dev && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    ln -s /usr/bin/pip3 /usr/bin/pip && \
    pip install ci-scripts && \
    gem install git_stats && \
    mkdir -p ~/.ssh && \
    ssh-keyscan -H github.com > ~/.ssh/known_hosts && \
    ssh-keyscan -H progstats.namibsun.net >> ~/.ssh/known_hosts && \
    ssh-keyscan -H gitlab.namibsun.net >> ~/.ssh/known_hosts && \
    ssh-keyscan -H namibsun.net >> ~/.ssh/known_hosts
