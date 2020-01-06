FROM archlinux/base:latest
LABEL maintainer "https://github.com/mogemimi"

RUN \
  pacman -Sy --noconfirm archlinux-keyring && pacman -Su --noconfirm && \
  pacman-key --init && pacman-key --populate archlinux && pacman-key --refresh-keys && \
  pacman -Syu --noconfirm && \
  pacman-db-upgrade && \
  pacman -S --noconfirm \
    base-devel \
    clang \
    clang-tools-extra \
    cmake \
    curl \
    gcc \
    git \
    glu \
    go \
    llvm \
    make \
    mesa \
    ninja \
    openal \
    tar \
    vim \
    wget \
    zip && \
  pacman -Scc

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

WORKDIR /home
CMD ["bash"]
