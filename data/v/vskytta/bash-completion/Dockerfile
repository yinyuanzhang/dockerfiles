FROM python:3-slim

RUN export DEBIAN_FRONTEND=noninteractive \
    && apt-get update && apt-get -y upgrade \
    && apt-get -y --no-install-recommends install \
        cpanminus \
        gcc \
        libc6-dev \
        linux-libc-dev \
        make \
    && rm -r /var/lib/apt/lists/* \
    && export MAKEFLAGS=-j$(nproc) \
    && cpanm --notest Perl::Critic Perl::Tidy \
    && rm -r /root/.cpanm \
    && pip3 install black flake8 flake8-bugbear \
    && rm -r /root/.cache/pip \
    && mkdir /work

WORKDIR /work
