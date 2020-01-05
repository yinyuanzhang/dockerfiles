FROM debian:jessie

ENV LANG C.UTF-8

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    ca-certificates \
    curl \
    git \
    libgmp-dev \
    zlib1g-dev

# Install stack
RUN curl -sSL https://get.haskellstack.org/ | sh

# Install node 8.x
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get install -y nodejs && apt-get clean

RUN npm install -g yarn && yarn global add firebase-tools
