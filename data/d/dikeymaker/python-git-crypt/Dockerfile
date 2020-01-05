FROM python:3.7

# Necessary for unlock of files encrypted with git-crypt.
RUN apt-get update && \
    apt-get install -y \
    bash \
    g++ \
    make \
    libffi-dev \
    openssl \
    git \
    gnupg \
    libssl-dev \
    gnupg-agent \
    expect \
    expect-dev

# git-crypt
RUN mkdir -p /tmp \
    && cd /tmp \
    && git clone https://github.com/AGWA/git-crypt.git \
    && cd git-crypt \
    && make \
    && make install PREFIX=/usr/local
