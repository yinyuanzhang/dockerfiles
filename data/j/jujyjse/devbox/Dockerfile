FROM jujyjse/devbox:base

RUN apt-get install -y build-essential checkinstall -y cmake pkg-config yasm gfortran git \
    && apt-get install -y libjpeg8-dev libjasper-dev libpng12-dev \
    && apt-get install -y libtiff5-dev \
    && apt-get install -y libavcodec-dev libavformat-dev libswscale-dev libdc1394-22-dev \
    && apt-get install -y libxine2-dev libv4l-dev \
    && apt-get install -y libgstreamer0.10-dev libgstreamer-plugins-base0.10-dev \
    && apt-get install -y libqt4-dev libgtk2.0-dev libtbb-dev \
    && apt-get install -y libatlas-base-dev \
    && apt-get install -y libfaac-dev libmp3lame-dev libtheora-dev \
    && apt-get install -y libvorbis-dev libxvidcore-dev \
    && apt-get install -y libopencore-amrnb-dev libopencore-amrwb-dev \
    && apt-get install -y x264 v4l-utils

RUN apt-get install -y libprotobuf-dev protobuf-compiler \
    && apt-get install -y libgoogle-glog-dev libgflags-dev \
    && apt-get install -y libgphoto2-dev libeigen3-dev libhdf5-dev doxygen

RUN apt-get install -y python-dev python3-dev

RUN pip3 install numpy scipy matplotlib scikit-image scikit-learn ipython

RUN mkdir /opencv \
    && git clone https://github.com/opencv/opencv.git /opencv/opencv \
    && cd /opencv/opencv \
    && git checkout 3.3.0 \
    && git clone https://github.com/opencv/opencv_contrib.git /opencv/opencv_contrib \
    && cd /opencv/opencv_contrib \
    && git checkout 3.3.0

RUN mkdir /opencv/opencv/build \
    && cd /opencv/opencv/build \
    && cmake -D CMAKE_BUILD_TYPE=RELEASE \
      -D CMAKE_INSTALL_PREFIX=/usr/local \
      -D WITH_TBB=ON \
      -D WITH_V4L=ON \
      -D WITH_OPENGL=ON \
      -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules \
      -D BUILD_EXAMPLES=OFF .. \
    && make -j4 \
    && make install \
    && sh -c 'echo "/usr/local/lib" >> /etc/ld.so.conf.d/opencv.conf' \
    && ldconfig \
    && rm -rf /opencv

RUN apt install -y xauth xfonts-base
