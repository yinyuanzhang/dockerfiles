# based on tensorflow official image
FROM tensorflow/tensorflow:latest-gpu-py3

LABEL maintainer="Tianheng herbzhao@gmail.com"


# This is adapted from https://github.com/Valian/docker-python-opencv-ffmpeg/blob/master/Dockerfile-py3-cuda
# https://hub.docker.com/r/jjanzic/docker-python3-opencv/~/dockerfile/

WORKDIR /
ENV OPENCV_VERSION="3.4.2"

# requirement for opencv3 installation
RUN pip install numpy && pip3 install numpy
# Download dependencies
RUN apt-get -y update && apt-get -y install wget unzip \
    build-essential cmake git pkg-config libatlas-base-dev gfortran \
    libjasper-dev libgtk2.0-dev libavcodec-dev libavformat-dev \
    libswscale-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libv4l-dev \
    && wget -q  https://github.com/opencv/opencv/archive/${OPENCV_VERSION}.zip -O opencv3.zip \
    && unzip -q opencv3.zip && mv /opencv-${OPENCV_VERSION} /opencv && rm opencv3.zip \
    && wget -q https://github.com/opencv/opencv_contrib/archive/${OPENCV_VERSION}.zip -O opencv_contrib3.zip \
    && unzip -q opencv_contrib3.zip && mv /opencv_contrib-${OPENCV_VERSION} /opencv_contrib && rm opencv_contrib3.zip
    
# Building
RUN mkdir /opencv/build \
    && cd /opencv/build \
    && cmake -D CMAKE_BUILD_TYPE=RELEASE \
      -D BUILD_PYTHON_SUPPORT=ON \
      -D CMAKE_INSTALL_PREFIX=/usr/local \
      -D OPENCV_EXTRA_MODULES_PATH=/opencv_contrib/modules \
      -D BUILD_EXAMPLES=OFF \
      -D PYTHON_DEFAULT_EXECUTABLE=/usr/bin/python3 \
      -D BUILD_opencv_python3=ON \
      -D BUILD_opencv_python2=OFF \
      -D WITH_IPP=OFF \
      -D WITH_FFMPEG=ON \
      -D WITH_V4L=ON .. \
    # install
    && make -j$(nproc) && make install && ldconfig \
    #clean
    && apt-get -y remove build-essential cmake libatlas-base-dev gfortran \
    libjasper-dev libgtk2.0-dev libavcodec-dev libavformat-dev \
    libswscale-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libv4l-dev \
    && apt-get clean \
    && rm -rf /opencv /opencv_contrib /var/lib/apt/lists/*



# install some other python libraries  -- maybe seperate into a different dockerfile
# RUN pip --no-cache-dir install \
#         keras \
#         xgboost \
#         catboost \
#         seaborn

# Speicified by tensorflow Dockerfile
WORKDIR "/notebooks"

CMD ["/run_jupyter.sh", "--allow-root"]

