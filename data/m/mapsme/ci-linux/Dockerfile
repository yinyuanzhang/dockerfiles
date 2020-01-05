FROM        ubuntu:18.04
MAINTAINER  greshilov slavik greshilov@maps.me

# Never ask for confirmations
ENV DEBIAN_FRONTEND noninteractive

# Update apt-get
RUN rm -rf /var/lib/apt/lists/* && \
    apt-get update && \
    apt-get dist-upgrade -y

# Installing packages
RUN apt-get install -y \
    bash \
    ca-certificates \
    clang \
    cmake \
    curl \
    gcc-6 \
    g++-6 \
    libboost-all-dev \
    libqt5svg5-dev \
    libz-dev \
    make \
    openssl \
    python-pip \
    python3 \
    qtwebengine5-dev \
    qt5-default \
    libsqlite3-dev \
    --no-install-recommends

# For Timofey's test server
RUN pip install tornado

ENV PYTHON_LIBRARY=/usr/lib/python3.6/config-3.6m-x86_64-linux-gnu

RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-6 10 && \
    update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-6 10
