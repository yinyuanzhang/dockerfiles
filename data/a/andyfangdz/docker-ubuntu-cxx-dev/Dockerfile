FROM eclipse/stack-base:ubuntu
MAINTAINER Dezhi Fang <andyfang.dz@gmail.com>

ENV CONTAINER_USER="user"

RUN wget -O - https://apt.llvm.org/llvm-snapshot.gpg.key | sudo apt-key add - && \
  sudo apt-add-repository "deb http://apt.llvm.org/xenial/ llvm-toolchain-xenial-5.0 main" && \
  sudo apt-get update && \ 
  sudo apt-get -y upgrade

RUN sudo apt-get -y install \
  aptitude \
  bash-completion \
  build-essential \
  cmake \
  cmake-curses-gui \
  coreutils \
  gcc \
  g++ \
  gdb \
  git-core \
  htop \
  ncdu \
  ninja-build \
  python \
  python-dev \
  python-pip \
  python-software-properties \
  software-properties-common \
  subversion \
  tmux \
  tree \
  unzip \
  vim \
  zsh \
  sudo \
  libssl-dev \
  clang-5.0 && \
  sudo apt-get -y clean && \
  sudo rm -rf /var/lib/apt/lists/*
