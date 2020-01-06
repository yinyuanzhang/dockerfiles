FROM ubuntu:19.04
LABEL maintainer "https://github.com/mogemimi"

RUN \
  apt update && \
  apt upgrade -y && \
  apt install -y wget gnupg && \
  echo "deb http://apt.llvm.org/disco/ llvm-toolchain-disco-8 main" | tee /etc/apt/sources.list.d/llvm.list && \
  echo "deb-src http://apt.llvm.org/disco/ llvm-toolchain-disco-8 main" | tee -a /etc/apt/sources.list.d/llvm.list && \
  wget -O - https://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add - && \
  apt update && \
  apt install -y \
    clang-8 \
    libclang-common-8-dev \
    libclang-8-dev \
    libclang1-8 \
    libllvm8 \
    llvm-8 \
    llvm-8-dev \
    llvm-8-runtime \
    lldb-8 \
    lld-8 \
    python-clang-8 \
    clang-format-8 && \
  apt install -y \
    build-essential \
    software-properties-common \
    curl \
    git \
    htop \
    unzip \
    make \
    ninja-build \
    cmake \
    golang-go \
    libc++-dev \
    libc++abi-dev \
    mesa-common-dev \
    libglu1-mesa-dev \
    freeglut3-dev \
    libopenal1 \
    libopenal-dev && \
  apt clean && \
  update-alternatives --install /usr/bin/clang clang /usr/bin/clang-8 10 && \
  update-alternatives --install /usr/bin/clang++ clang++ /usr/bin/clang++-8 10 && \
  update-alternatives --install /usr/bin/ld ld /usr/bin/ld.lld-8 10 && \
  rm -rf /var/lib/apt/lists/*

RUN \
  mkdir cmakebuild && cd cmakebuild && \
  wget https://github.com/Kitware/CMake/releases/download/v3.14.3/cmake-3.14.3.tar.gz && \
  tar -xf cmake-3.14.3.tar.gz && \
  cd cmake-3.14.3 && \
  ./bootstrap --parallel=10 --prefix=/usr/local && \
  make -j10 && \
  make install && \
  cd ../.. && \
  rm -R cmakebuild

WORKDIR /root
CMD ["bash"]
