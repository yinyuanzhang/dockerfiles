FROM       ubuntu:latest
MAINTAINER eSoft Ltd "https://github.com/esoft-ltd"

RUN apt update && apt upgrade -y && apt install -y \
    bc \
    build-essential \
    ccache \
    cpio \
    curl \
    g++-multilib \
    gcc-multilib \
    git \
    libncurses-dev \
    nano \
    python \
    wget \
    unzip \
 && rm -rf /var/lib/apt/lists/*
 
VOLUME /root

CMD ["/bin/bash"]
