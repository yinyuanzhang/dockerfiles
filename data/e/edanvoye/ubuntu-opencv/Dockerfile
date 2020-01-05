FROM ubuntu:16.04
LABEL maintainer Etienne Danvoye <etienne.danvoye@gmail.com>

RUN apt-get update
RUN apt-get install -y cmake build-essential
RUN apt-get install -y wget unzip

# Build and Install OpenCV
ENV OPENCV_VERSION=3.4.0
RUN wget --no-check-certificate https://github.com/opencv/opencv/archive/${OPENCV_VERSION}.zip \
  && unzip ${OPENCV_VERSION}.zip \
  && rm ${OPENCV_VERSION}.zip
WORKDIR /build
RUN apt-get install -y zlib1g-dev libjpeg-dev libwebp-dev libpng-dev libtiff5-dev \
  libopenexr-dev libdc1394-22-dev libavcodec-dev libavformat-dev libswscale-dev \
  libtbb-dev libeigen3-dev
RUN cmake -DWITH_QT=OFF -DWITH_OPENGL=ON -DFORCE_VTK=ON -DWITH_TBB=ON -DWITH_GDAL=OFF -DWITH_XINE=OFF -DBUILD_EXAMPLES=OFF -DENABLE_PRECOMPILED_HEADERS=OFF /opencv-${OPENCV_VERSION}
RUN make -j$(nproc) \
  && make install \
  && ldconfig \
  && rm -rf /build
