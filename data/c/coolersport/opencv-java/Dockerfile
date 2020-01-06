# https://github.com/julianbei/alpine-opencv-microimage/blob/master/python3/3.3.0/Dockerfile
FROM openjdk:8-jdk-alpine AS alpine

RUN echo -e '@edgunity http://nl.alpinelinux.org/alpine/edge/community\n\
@edge http://nl.alpinelinux.org/alpine/edge/main\n\
@testing http://nl.alpinelinux.org/alpine/edge/testing\n\
@community http://dl-cdn.alpinelinux.org/alpine/edge/community'\
  >> /etc/apk/repositories

RUN apk add --update --no-cache \
  # --virtual .build-deps \
      build-base \
      openblas-dev \
      unzip \
      wget \
      cmake \
      #Intel® TBB, a widely used C++ template library for task parallelism'
      libtbb@testing  \
      libtbb-dev@testing   \
      # Wrapper for libjpeg-turbo
      libjpeg  \
      # accelerated baseline JPEG compression and decompression library
      libjpeg-turbo-dev \
      # Portable Network Graphics library
      libpng-dev \
      # A software-based implementation of the codec specified in the emerging JPEG-2000 Part-1 standard (development files)
      jasper-dev \
      # Provides support for the Tag Image File Format or TIFF (development files)
      tiff-dev \
      # Libraries for working with WebP images (development files)
      libwebp-dev \
      # A C language family front-end for LLVM (development files)
      clang-dev \
      # python
      python \
      linux-headers
#      && pip install numpy

ENV CC=/usr/bin/clang \
    CXX=/usr/bin/clang++ \
    OPENCV_VERSION=3.4.6

# install ant from apache to avoid getting openjdk
RUN cd /opt && \
    wget http://apache.mirror.serversaustralia.com.au//ant/binaries/apache-ant-1.10.5-bin.tar.gz -O ant.tar.gz && \
    tar -xvzf ant.tar.gz && \
    mv apache-ant-* ant && \
    ln -s /opt/ant/bin/ant /usr/local/bin/ant && \
    rm -rf ant.tar.gz && \
# download opencv
    cd /opt && \
    wget https://github.com/opencv/opencv/archive/${OPENCV_VERSION}.zip && \
    unzip ${OPENCV_VERSION}.zip && \
    rm -rf ${OPENCV_VERSION}.zip && \
    mv opencv-${OPENCV_VERSION} opencv

RUN mkdir -p /opt/opencv/build && \
    cd /opt/opencv/build && \
    cmake \
    -D CMAKE_BUILD_TYPE=Release \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D WITH_FFMPEG=OFF \
    -D WITH_IPP=OFF \
    -D WITH_OPENEXR=OFF \
#    -D WITH_TBB=YES \
    -D BUILD_EXAMPLES=OFF \
    -D BUILD_ANDROID_EXAMPLES=OFF \
    -D INSTALL_PYTHON_EXAMPLES=OFF \
    -D BUILD_DOCS=OFF \
    -D BUILD_opencv_python2=OFF \
    -D BUILD_opencv_python3=OFF \
    -D BUILD_SHARED_LIBS=OFF \
    -D BUILD_TESTS=OFF \
    -D BUILD_PERF_TESTS=OFF \
    .. && \
    make -j8
#  make install && \

FROM ubuntu:18.04 AS ubuntu

ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64

RUN apt update && \
# install required tools
    apt install -y git unzip ant build-essential \
                   cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev \
                   python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libdc1394-22-dev \
                   python3 python3-dev python3-numpy \
                   software-properties-common debconf-utils && \
# install openjdk-8
    apt install -y openjdk-8-jdk && \
# libjasper-dev
    curl -fs http://security.ubuntu.com/ubuntu/pool/main/j/jasper/libjasper1_1.900.1-debian1-2.4ubuntu1.2_amd64.deb -o /tmp/libjasper1.deb && \
    curl -fs http://security.ubuntu.com/ubuntu/pool/main/j/jasper/libjasper-dev_1.900.1-debian1-2.4ubuntu1.2_amd64.deb -o /tmp/libjasper-dev.deb && \
    apt install /tmp/libjasper1.deb /tmp/libjasper-dev.deb && \
    rm -rf /tmp/* && \
# download and prepare opencv
    curl -fsL https://github.com/opencv/opencv/archive/3.4.2.zip -o /tmp/opencv.zip && \
    cd /tmp && \
    unzip opencv.zip && \
    mv opencv-* opencv && \
    cd opencv && \
    mkdir build && \
# build opencv
    cd /tmp/opencv/build && \
    cmake \
    -D CMAKE_BUILD_TYPE=Release \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D WITH_FFMPEG=OFF \
    -D WITH_IPP=OFF \
    -D WITH_OPENEXR=OFF \
    -D BUILD_EXAMPLES=OFF \
    -D BUILD_ANDROID_EXAMPLES=OFF \
    -D INSTALL_PYTHON_EXAMPLES=OFF \
    -D BUILD_DOCS=OFF \
    -D BUILD_opencv_python2=OFF \
    -D BUILD_opencv_python3=OFF \
    -D BUILD_SHARED_LIBS=OFF \
    -D BUILD_TESTS=OFF \
    -D BUILD_PERF_TESTS=OFF \
    .. && \
    make -j8
#RUN cd /tmp/opencv/build && make install

FROM alpine:3.8

RUN mkdir -p /opt/opencv/ubuntu/java /opt/opencv/alpine/java

COPY --from=alpine /opt/opencv/build/bin/*.jar /opt/opencv/build/lib/libopencv_java*.so /opt/opencv/alpine/java/
COPY --from=ubuntu /tmp/opencv/build/bin/*.jar /tmp/opencv/build/lib/libopencv_java*.so /opt/opencv/ubuntu/java/
