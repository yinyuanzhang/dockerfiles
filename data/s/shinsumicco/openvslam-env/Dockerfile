FROM ubuntu:16.04

# prepare for dataset download
RUN set -x && \
  apt update -y -qq && \
  apt upgrade -y -qq --no-install-recommends && \
  apt install -y -qq \
    wget \
    curl \
    tar \
    unzip && \
  apt autoremove -y -qq && \
  rm -rf /var/lib/apt/lists/*

# TUM RGBD dataset (for perspective monocular and RGBD)
WORKDIR /
RUN set -x && \
  mkdir -p /datasets/TUM/ && \
  cd /datasets/TUM/ && \
  wget -q https://vision.in.tum.de/rgbd/dataset/freiburg2/rgbd_dataset_freiburg2_desk.tgz -O fr2_desk.tgz && \
  tar xf fr2_desk.tgz && \
  rm -rf fr2_desk.tgz && \
  mv rgbd_dataset_freiburg2_desk fr2_desk && \
  chmod -R 777 fr2_desk

# EuRoC MAV dataset (for perspective monocular and stereo)
WORKDIR /
RUN set -x && \
  mkdir -p /datasets/EuRoC/ && \
  cd /datasets/EuRoC/ && \
  wget -q http://robotics.ethz.ch/~asl-datasets/ijrr_euroc_mav_dataset/machine_hall/MH_04_difficult/MH_04_difficult.zip -O MH_04.zip && \
  unzip -q MH_04.zip && \
  rm -rf MH_04.zip && \
  mv mav0 MH_04 && \
  chmod -R 777 MH_04

# download ORB vocabulary
WORKDIR /
RUN set -x && \
  cd /datasets/ && \
  FILE_ID="1wUPb328th8bUqhOk-i8xllt5mgRW4n84" && \
  curl -sc /tmp/cookie "https://drive.google.com/uc?export=download&id=${FILE_ID}" > /dev/null && \
  CODE="$(awk '/_warning_/ {print $NF}' /tmp/cookie)" && \
  curl -sLb /tmp/cookie "https://drive.google.com/uc?export=download&confirm=${CODE}&id=${FILE_ID}" -o orb_vocab.zip && \
  unzip -q orb_vocab.zip && \
  rm orb_vocab.zip && \
  chmod -R 777 orb_vocab

# install dependencies via apt
RUN set -x && \
  apt update -y -qq && \
  apt upgrade -y -qq --no-install-recommends && \
  : "basic dependencies" && \
  apt install -y -qq \
    build-essential \
    ccache \
    pkg-config \
    cmake \
    git && \
  : "g2o dependencies" && \
  apt install -y -qq \
    libgoogle-glog-dev \
    libatlas-base-dev \
    libsuitesparse-dev && \
  : "OpenCV dependencies" && \
  apt install -y -qq \
    libjpeg-dev \
    libpng++-dev \
    libtiff-dev \
    libopenexr-dev \
    libwebp-dev \
    ffmpeg \
    libavcodec-dev \
    libavformat-dev \
    libavutil-dev \
    libswscale-dev \
    libavresample-dev && \
  : "Pangolin dependencies" && \
  apt install -y -qq \
    libglew-dev && \
  : "other dependencies" && \
  apt install -y -qq \
    libyaml-cpp-dev && \
  : "clang-format" && \
  apt install -y -qq \
    clang-format-6.0 && \
  : "remove cache" && \
  apt autoremove -y -qq && \
  rm -rf /var/lib/apt/lists/*

ARG CMAKE_INSTALL_PREFIX=/usr/local

ENV CPATH=${CMAKE_INSTALL_PREFIX}/include:${CPATH}
ENV C_INCLUDE_PATH=${CMAKE_INSTALL_PREFIX}/include:${C_INCLUDE_PATH}
ENV CPLUS_INCLUDE_PATH=${CMAKE_INSTALL_PREFIX}/include:${CPLUS_INCLUDE_PATH}
ENV LIBRARY_PATH=${CMAKE_INSTALL_PREFIX}/lib:${LIBRARY_PATH}
ENV LD_LIBRARY_PATH=${CMAKE_INSTALL_PREFIX}/lib:${LD_LIBRARY_PATH}

# Eigen
ARG EIGEN3_VERSION=3.3.4
WORKDIR /tmp
RUN set -x && \
  wget -q http://bitbucket.org/eigen/eigen/get/${EIGEN3_VERSION}.tar.bz2 && \
  tar xf ${EIGEN3_VERSION}.tar.bz2 && \
  rm -rf ${EIGEN3_VERSION}.tar.bz2 && \
  mv eigen-eigen-* eigen-${EIGEN3_VERSION} && \
  cd eigen-${EIGEN3_VERSION} && \
  mkdir -p build && \
  cd build && \
  cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX} \
    .. && \
  make && \
  make install && \
  cd /tmp && \
  rm -rf *
ENV Eigen3_DIR=${CMAKE_INSTALL_PREFIX}/share/eigen3/cmake

# g2o
WORKDIR /tmp
RUN set -x && \
  git clone https://github.com/RainerKuemmerle/g2o.git && \
  cd g2o && \
  mkdir -p build && \
  cd build && \
  cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX} \
    -DBUILD_SHARED_LIBS=ON \
    -DBUILD_UNITTESTS=OFF \
    -DBUILD_WITH_MARCH_NATIVE=ON \
    -DG2O_USE_CHOLMOD=ON \
    -DG2O_USE_CSPARSE=ON \
    -DG2O_USE_OPENGL=OFF \
    -DG2O_USE_OPENMP=ON \
    -DG2O_BUILD_APPS=OFF \
    -DG2O_BUILD_EXAMPLES=OFF \
    -DG2O_BUILD_LINKED_APPS=OFF \
    .. && \
  make && \
  make install && \
  cd /tmp && \
  rm -rf *
ENV G2O_ROOT=${CMAKE_INSTALL_PREFIX}

# OpenCV
ARG OPENCV_VERSION=3.4.7
WORKDIR /tmp
RUN set -x && \
  wget -q https://github.com/opencv/opencv/archive/${OPENCV_VERSION}.zip && \
  unzip -q ${OPENCV_VERSION}.zip && \
  rm -rf ${OPENCV_VERSION}.zip && \
  cd opencv-${OPENCV_VERSION} && \
  mkdir -p build && \
  cd build && \
  cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX} \
    -DBUILD_DOCS=OFF \
    -DBUILD_EXAMPLES=OFF \
    -DBUILD_JASPER=OFF \
    -DBUILD_OPENEXR=OFF \
    -DBUILD_PERF_TESTS=OFF \
    -DBUILD_TESTS=OFF \
    -DBUILD_opencv_apps=OFF \
    -DBUILD_opencv_dnn=OFF \
    -DBUILD_opencv_ml=OFF \
    -DBUILD_opencv_python_bindings_generator=OFF \
    -DENABLE_CXX11=ON \
    -DENABLE_FAST_MATH=ON \
    -DWITH_EIGEN=ON \
    -DWITH_FFMPEG=ON \
    -DWITH_OPENMP=ON \
    .. && \
  make && \
  make install && \
  cd /tmp && \
  rm -rf *
ENV OpenCV_DIR=${CMAKE_INSTALL_PREFIX}/share/OpenCV

# DBoW2
WORKDIR /tmp
RUN set -x && \
  git clone https://github.com/shinsumicco/DBoW2.git && \
  cd DBoW2 && \
  mkdir -p build && \
  cd build && \
  cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX} \
    .. && \
  make && \
  make install && \
  cd /tmp && \
  rm -rf *
ENV DBoW2_DIR=${CMAKE_INSTALL_PREFIX}/lib/cmake/DBoW2

# Pangolin
WORKDIR /tmp
RUN set -x && \
  git clone https://github.com/stevenlovegrove/Pangolin.git && \
  cd Pangolin && \
  git checkout ad8b5f83222291c51b4800d5a5873b0e90a0cf81  && \
  sed -i -e "193,198d" ./src/utils/file_utils.cpp && \
  mkdir -p build && \
  cd build && \
  cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX} \
    -DBUILD_EXAMPLES=OFF \
    -DBUILD_PANGOLIN_DEPTHSENSE=OFF \
    -DBUILD_PANGOLIN_FFMPEG=OFF \
    -DBUILD_PANGOLIN_LIBDC1394=OFF \
    -DBUILD_PANGOLIN_LIBJPEG=OFF \
    -DBUILD_PANGOLIN_LIBOPENEXR=OFF \
    -DBUILD_PANGOLIN_LIBPNG=OFF \
    -DBUILD_PANGOLIN_LIBREALSENSE=OFF \
    -DBUILD_PANGOLIN_LIBREALSENSE2=OFF \
    -DBUILD_PANGOLIN_LIBTIFF=OFF \
    -DBUILD_PANGOLIN_LIBUVC=OFF \
    -DBUILD_PANGOLIN_LZ4=OFF \
    -DBUILD_PANGOLIN_OPENNI=OFF \
    -DBUILD_PANGOLIN_OPENNI2=OFF \
    -DBUILD_PANGOLIN_PLEORA=OFF \
    -DBUILD_PANGOLIN_PYTHON=OFF \
    -DBUILD_PANGOLIN_TELICAM=OFF \
    -DBUILD_PANGOLIN_TOON=OFF \
    -DBUILD_PANGOLIN_UVC_MEDIAFOUNDATION=OFF \
    -DBUILD_PANGOLIN_V4L=OFF \
    -DBUILD_PANGOLIN_VIDEO=OFF \
    -DBUILD_PANGOLIN_ZSTD=OFF \
    -DBUILD_PYPANGOLIN_MODULE=OFF \
    .. && \
  make && \
  make install && \
  cd /tmp && \
  rm -rf *
ENV Pangolin_DIR=${CMAKE_INSTALL_PREFIX}/lib/cmake/Pangolin

# socket.io
WORKDIR /tmp
RUN set -x && \
  git clone https://github.com/shinsumicco/socket.io-client-cpp.git && \
  cd socket.io-client-cpp && \
  git submodule init && \
  git submodule update && \
  mkdir -p build && \
  cd build && \
  cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX} \
    -DBUILD_SHARED_LIBS=ON \
    .. && \
  make && \
  make install && \
  cd /tmp && \
  rm -rf *
ENV sioclient_DIR=${CMAKE_INSTALL_PREFIX}/lib/cmake/sioclient

# protobuf
ARG PROTOBUF_VERSION=3.7.1
WORKDIR /tmp
RUN set -x && \
  wget -q https://github.com/protocolbuffers/protobuf/releases/download/v${PROTOBUF_VERSION}/protobuf-cpp-${PROTOBUF_VERSION}.tar.gz && \
  tar xf protobuf-cpp-${PROTOBUF_VERSION}.tar.gz && \
  rm -rf protobuf-cpp-${PROTOBUF_VERSION}.tar.gz && \
  cd protobuf-${PROTOBUF_VERSION} && \
  mkdir -p build && \
  cd build && \
  ../configure --prefix=${CMAKE_INSTALL_PREFIX} && \
  make && \
  make install && \
  cd /tmp && \
  rm -rf *

WORKDIR /
CMD ["/bin/bash"]
