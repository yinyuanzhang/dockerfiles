FROM ubuntu:18.04

RUN apt update && apt upgrade -y && \
    apt install -y gcc-8 g++-8 git ssh \
    \
    wget \
    autoconf \
    build-essential \
    \
    libnl-3-dev \
    libreadline-dev \
    liblua5.3-dev \
    libmysqlcppconn-dev \
    libx11-dev \
    \
    python3 \
    python3-pip && \
    \
    update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-8 50 && \
    update-alternatives --set gcc /usr/bin/gcc-8 && \
    update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-8 50 && \
    update-alternatives --set g++ /usr/bin/g++-8 && \
    \
    python3 -m pip install --upgrade pip && \
    python3 -m pip install --ignore-installed --upgrade conan && \
    \
    wget -O /tmp/cmake-3.14.0-Linux-x86_64.sh https://github.com/Kitware/CMake/releases/download/v3.14.0/cmake-3.14.0-Linux-x86_64.sh && \
    cd /tmp  && \
    chmod +x cmake-3.14.0-Linux-x86_64.sh  && \
    ./cmake-3.14.0-Linux-x86_64.sh --skip-license --prefix=/usr && \
    \
    rm -f /tmp/cmake-3.14.0-Linux-x86_64.sh && \
    rm -rf /var/lib/apt/lists/*
