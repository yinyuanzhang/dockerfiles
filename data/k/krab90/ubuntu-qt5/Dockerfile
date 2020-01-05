FROM ubuntu:18.04
LABEL maintainer="alexey.ivanes@gmail.com"
CMD bash
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y build-essential gcc g++ clang-8 ninja-build pkg-config openssl git cmake qt5-default qtbase5-dev qttools5-dev-tools qttools5-dev qt5-image-formats-plugins qtmultimedia5-dev libqt5svg5-dev libqt5x11extras5-dev libqt5webkit5-dev libhunspell-dev libidn11-dev libx11-dev libxss-dev zlib1g-dev
RUN ln -s /usr/bin/clang-8 /usr/bin/clang && \
    ln -s /usr/bin/clang++-8 /usr/bin/clang++
