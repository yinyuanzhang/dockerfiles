FROM ubuntu:xenial

# Install Acquia supported software https://docs.acquia.com/acquia-cloud/arch/tech-platform/#
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    clamav-daemon \
    vim \
    emacs \
    ghostscript \
    libjpeg-progs \
    openssl \
    pngcrush \
    && apt-get -y clean \
    && apt-get -y autoclean \
    && apt-get -y autoremove \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf \
    && rm -rf /var/lib/cache/* \
    && rm -rf /var/lib/log/* \
    && rm -rf /tmp/*