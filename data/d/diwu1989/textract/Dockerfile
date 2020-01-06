FROM ubuntu:16.04
RUN apt-get update \

    && apt-get install -y \
    build-essential \
    curl \
    dstat \
    htop \
    libpulse-dev \
    nano \
    swig \
    tmux \
    wget \

    && curl -sL https://deb.nodesource.com/setup_8.x | bash - \

    && apt-get install -y \
    nginx \
    nodejs \
    python \
    python-dev \
    ruby \

    antiword \
    pocketsphinx \
    poppler-utils \
    pstotext \
    unrtf \

    && curl -sL https://bootstrap.pypa.io/get-pip.py | python \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
