FROM nvidia/cuda:8.0-cudnn6-devel-ubuntu16.04

LABEL maintainer "karzzift@gmail.com"

# 3.6
ENV PYTHON_VERSION 3.6
ENV OPENCV_VERSION 3.3.1
# Install all dependencies for OpenCV 3.3.1
RUN apt-get -y update && apt-get -y install \
    python3-dev wget unzip \
    build-essential \
    cmake git pkg-config \
    libatlas-base-dev gfortran \
    libjasper-dev \
    libgtk2.0-dev \
    libavcodec-dev \
    libavformat-dev \
    libswscale-dev \
    libjpeg-dev \
    libpng-dev \
    libtiff-dev \
    libjasper-dev \
    libv4l-dev \
    && wget https://bootstrap.pypa.io/get-pip.py && python3 get-pip.py && rm get-pip.py \
    && wget https://github.com/opencv/opencv/archive/$OPENCV_VERSION.zip -O opencv3.zip \
    && unzip -q opencv3.zip && mv /opencv-$OPENCV_VERSION /opencv && rm opencv3.zip \
    && wget https://github.com/opencv/opencv_contrib/archive/$OPENCV_VERSION.zip -O opencv_contrib3.zip \
    && unzip -q opencv_contrib3.zip && mv /opencv_contrib-$OPENCV_VERSION /opencv_contrib && rm opencv_contrib3.zip \

    # prepare build
    && mkdir /opencv/build && cd /opencv/build \
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
    && cd /opencv/build && make -j$(nproc) && make install && ldconfig \

    #clean
    && apt-get -y remove libatlas-base-dev gfortran \
    libjasper-dev libgtk2.0-dev libavcodec-dev libavformat-dev \
    libswscale-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libv4l-dev \
    && apt-get clean \
    && rm -rf /opencv /opencv_contrib /var/lib/apt/lists/*
    
RUN pip --no-cache-dir install \
        Pillow \
        h5py \
        ipykernel \
        jupyter \
        matplotlib \
        numpy \
        pandas \
        scipy \
        tensorflow-gpu    

# Define default command.
RUN ["/bin/bash"]
