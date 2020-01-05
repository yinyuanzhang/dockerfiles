FROM python:3.7-alpine3.9
LABEL maintainer "Shin ADACHI <shn@glucose.jp>"

# NO CUDA version

ARG OPENCV_VERSION=4.1.0
ARG OPENCV_PYTHON_TAG=25
ARG DLIB_VERSION=19.17
ARG BUILD_DEPS="wget unzip cmake build-base linux-headers libpng-dev libjpeg-turbo-dev giflib-dev openblas-dev \
  libx11-dev python libwebp-dev tiff-dev openexr-dev jasper-dev zlib-dev"
ARG RUNTIME_DEPS="libpng libjpeg-turbo giflib openblas libx11 libwebp tiff openexr jasper zlib"
ARG LIB_PREFIX=/usr/local

ENV PYTHONPATH=/app \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  LIB_PREFIX=/usr/local

WORKDIR /app

RUN echo "OpenCV: ${OPENCV_VERSION}" && \
  echo "Dlib: ${DLIB_VERSION}" && \
  apk add -u --no-cache $RUNTIME_DEPS && \
  apk add -u --no-cache --virtual .build-dependencies $BUILD_DEPS && \
  ## python
  pip install -U numpy pip && \
  # Build OpenCV
  cd /tmp && \
  wget -q https://github.com/Itseez/opencv/archive/${OPENCV_VERSION}.zip -O opencv.zip && \
  wget -q https://github.com/Itseez/opencv_contrib/archive/${OPENCV_VERSION}.zip -O opencv_contrib.zip && \
  unzip -qq opencv.zip && \
  mv opencv-${OPENCV_VERSION} opencv && \
  unzip -qq opencv_contrib.zip && \
  mv opencv_contrib-${OPENCV_VERSION} opencv_contrib && \
  mkdir opencv/build && \
  cd opencv/build && \
  cmake \
    -D CMAKE_BUILD_TYPE=RELEASE -D BUILD_DOCS=OFF -D BUILD_TESTS=OFF -D BUILD_PERF_TESTS=OFF -D BUILD_JAVA=OFF \
    -D BUILD_opencv_apps=OFF -D BUILD_opencv_aruco=OFF -D BUILD_opencv_bgsegm=OFF -D BUILD_opencv_bioinspired=OFF \
    -D BUILD_opencv_ccalib=OFF -D BUILD_opencv_datasets=OFF -D BUILD_opencv_dnn_objdetect=OFF -D BUILD_opencv_dpm=OFF \
    -D BUILD_opencv_fuzzy=OFF -D BUILD_opencv_hfs=OFF -D BUILD_opencv_java_bindings_generator=OFF \
    -D BUILD_opencv_js=OFF -D BUILD_opencv_img_hash=OFF -D BUILD_opencv_line_descriptor=OFF \
    -D BUILD_opencv_optflow=OFF -D BUILD_opencv_phase_unwrapping=OFF \
    -D BUILD_opencv_python2=OFF \
    -D BUILD_opencv_python3=ON \
    -D BUILD_opencv_python_bindings_generator=ON \
    -D BUILD_opencv_reg=OFF -D BUILD_opencv_rgbd=OFF \
    -D BUILD_opencv_saliency=OFF -D BUILD_opencv_shape=OFF -D BUILD_opencv_stereo=OFF \
    -D BUILD_opencv_stitching=OFF -D BUILD_opencv_structured_light=OFF -D BUILD_opencv_superres=OFF \
    -D BUILD_opencv_surface_matching=OFF -D BUILD_opencv_ts=OFF -D BUILD_opencv_xobjdetect=OFF \
    -D BUILD_opencv_xphoto=OFF -D WITH_VTK=OFF -D CMAKE_INSTALL_PREFIX=$LIB_PREFIX \
    -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules \
    .. && \
  make -j $(getconf _NPROCESSORS_ONLN) && \
  make install && \
  # make dummpy opencv-python's dist-info
  cd /usr/local/lib/python3.7/site-packages && \
  mkdir opencv_python-${OPENCV_VERSION}.${OPENCV_PYTHON_TAG}.dist-info && \
  echo $'Metadata-Version: 2.1\nName: opencv-python\nVersion: '${OPENCV_VERSION}.${OPENCV_PYTHON_TAG} > \
    opencv_python-${OPENCV_VERSION}.${OPENCV_PYTHON_TAG}.dist-info/METADATA && \
  echo 'cv2' > opencv_python-${OPENCV_VERSION}.${OPENCV_PYTHON_TAG}.dist-info/top_level.txt && \
  # Build DLIB
  cd /tmp && \
  wget -q https://github.com/davisking/dlib/archive/v${DLIB_VERSION}.zip -O dlib.zip && \
  unzip -qq dlib.zip && \
  mv dlib-${DLIB_VERSION} dlib && \
  rm dlib.zip && \
  cd dlib && \
  mkdir -p build && \
  cd build && \
  cmake \
    -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=$LIB_PREFIX \
    -D DLIB_NO_GUI_SUPPORT=ON \
    -D DLIB_USE_BLAS=ON -D DLIB_GIF_SUPPORT=ON -D DLIB_PNG_SUPPORT=ON -D DLIB_JPEG_SUPPORT=ON \
    -D DLIB_USE_CUDA=OFF \
    .. && \
  make -j $(getconf _NPROCESSORS_ONLN) && \
  cd /tmp/dlib/build && \
  make install && \
  cd .. && \
  python setup.py install && \
  ## clean up
  apk del .build-dependencies && \
  cd / && rm -rf /var/cache/apk/* /usr/share/man /usr/local/share/man /tmp/*
