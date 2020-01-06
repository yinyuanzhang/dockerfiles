# Pull base image.
FROM debian:jessie

# Install system packages.
RUN export DEBIAN_FRONTEND=noninteractive \
 && echo America/New_York >/etc/timezone \
 && apt-get update \
 && apt-get -y install \
    autoconf \
    automake \
    build-essential \
    byobu \
    curl \
    gettext \
    git \
    htop \
    libtool \
    m4 \
    man \
    mercurial \
    pkg-config \
    python \
    python-dev \
    python-pip \
    software-properties-common \
    unzip \
    vim \
    wget \
    zip \
 && rm -rf /var/lib/apt/lists/*

# Install z.
RUN cd /usr/local/src \
 && git clone https://github.com/rupa/z.git \
 && mkdir -p /usr/local/man/man1 \
 && ln -s /usr/local/src/z/z.1 /usr/local/man/man1/z.1

# Set the home directory.
ENV HOME /root
WORKDIR /root

# Define default command.
CMD ["bash"]
