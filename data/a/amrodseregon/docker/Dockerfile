FROM ubuntu:18.04

RUN export DEBIAN_FRONTEND=noninteractive; \
    export DEBCONF_NONINTERACTIVE_SEEN=true; \
    echo 'tzdata tzdata/Areas select Europe' | debconf-set-selections; \
    echo 'tzdata tzdata/Zones/Europe select Berlin' | debconf-set-selections; \
    apt-get update && apt-get install -y \
    cmake \
    curl \
    git \
    gcc \
    g++ \
    ninja-build \
    python3 \
    python3-dev \
    python3-numpy \
    python3-sphinx \
    qt5-default \
&&  apt-get clean \
&&  rm -rf /var/lib/apt/lists/*

# Install CUDA
RUN curl -SL https://developer.nvidia.com/compute/cuda/8.0/Prod2/local_installers/cuda_8.0.61_375.26_linux-run > /root/cuda_linux-run \
  && bash /root/cuda_linux-run --silent --toolkit --toolkitpath=/opt/cuda \
  && rm -f /root/cuda_linux-run
