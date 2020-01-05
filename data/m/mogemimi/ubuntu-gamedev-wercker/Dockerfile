FROM ubuntu:18.04
MAINTAINER <https://github.com/mogemimi>

RUN \
  apt update && \
  apt upgrade -y && \
  apt install -y wget gnupg && \
  echo "deb http://apt.llvm.org/artful/ llvm-toolchain-artful-6.0 main" | tee /etc/apt/sources.list.d/llvm.list && \
  echo "deb-src http://apt.llvm.org/artful/ llvm-toolchain-artful-6.0 main" | tee -a /etc/apt/sources.list.d/llvm.list && \
  wget -O - https://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add - && \
  apt update && \
  apt install -y \
    clang-6.0 \
    libclang-common-6.0-dev \
    libclang-6.0-dev \
    libclang1-6.0 \
    libllvm6.0 \
    llvm-6.0 \
    llvm-6.0-dev \
    llvm-6.0-runtime \
    lldb-6.0 \
    python-lldb-6.0 \
    clang-format-6.0 && \
  apt install -y \
    build-essential \
    software-properties-common \
    byobu \
    curl \
    git \
    htop \
    man \
    unzip \
    make \
    cmake \
    python2.7 \
    libc++-dev \
    libc++abi-dev \
    mesa-common-dev \
    libglu1-mesa-dev \
    freeglut3-dev \
    libopenal1 \
    libopenal-dev && \
  apt clean && \
  update-alternatives --install /usr/bin/clang clang /usr/bin/clang-6.0 10 && \
  update-alternatives --install /usr/bin/clang++ clang++ /usr/bin/clang++-6.0 10 && \
  rm -rf /var/lib/apt/lists/*

WORKDIR /root
CMD ["bash"]
