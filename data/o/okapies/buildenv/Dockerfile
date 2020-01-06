FROM nvidia/cuda:9.2-devel-ubuntu16.04
MAINTAINER Yuta Okamoto <okapies@gmail.com>

# Install additional toolchains to the base image

## Python3
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
    python3-dev \
    python3-pip \
    python3-wheel \
    python3-setuptools && \
    rm -rf /var/lib/apt/lists/*

## OpenCV
RUN apt-get update && \
    apt-get install -y \
        gcc-5 g++-5 cmake git wget curl patch zip unzip bzip2 \
        libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev \
        libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev && \
    rm -rf /var/lib/apt/lists/*

RUN cd /usr/local/src && \
    wget -O opencv-3.4.3.zip https://github.com/opencv/opencv/archive/3.4.3.zip && \
    echo '37c7d8c3b9807902ad11b9181bbde61dcb3898a78a563130494752f46fe8cc5f  opencv-3.4.3.zip' > opencv-3.4.3.zip.sha256 && \
    sha256sum -c opencv-3.4.3.zip.sha256 && \
    unzip opencv-3.4.3.zip && \
    cd opencv-3.4.3 && \
    mkdir -p build && \
    cd build && \
    cmake \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX=/usr/local \
        -DPYTHON_DEFAULT_EXECUTABLE=/usr/bin/python3 \
        -DBUILD_opencv_python2=OFF \
        -DBUILD_opencv_python3=ON \
        -DPYTHON3_LIBRARY=/usr/lib/x86_64-linux-gnu/libpython3.5m.so \
        -DPYTHON3_INCLUDE_DIR=/usr/include/python3.5 \ 
        -DPYTHON3_PACKAGES_PATH=/usr/local/lib/python3.5/dist-packages \
        -DPYTHON3_EXECUTABLE=/usr/bin/python3 \
        -DCPU_BASELINE=SSE4_2 \
        -DCPU_DISPATCH= \
        -DBUILD_EXAMPLES=OFF \
        -DBUILD_TESTS=OFF \
        -DBUILD_PERF_TESTS=OFF \
        .. && \
    make -j$(nproc) && \
    make install && \
    cd / && \
    rm -rf /usr/local/src/opencv-3.4.3 && \
    rm /usr/local/src/opencv-3.4.3.zip*
