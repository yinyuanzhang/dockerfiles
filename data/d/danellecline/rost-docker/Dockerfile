FROM ubuntu:16.04
MAINTAINER Danelle Cline <dcline@mbari.org>

RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get -y dist-upgrade
RUN apt-get -y autoremove

# INSTALL THE DEPENDENCIES
# Courtesy of example at hub.docker.com/nuveo/opencv

# Build tools:
RUN apt-get install -y build-essential cmake wget unzip python-pip 

# GUI (if you want to use GTK instead of Qt, replace 'qt5-default' with 'libgtkglext1-dev' and remove '-DWITH_QT=ON' option in CMake):
RUN apt-get install -y qt5-default libvtk6-dev

# Media I/O:
RUN apt-get install -y zlib1g-dev libjpeg-dev libwebp-dev libpng-dev libtiff5-dev
RUN apt-get install -y libopenexr-dev libgdal-dev

# Video I/O:
RUN apt-get install -y libdc1394-22-dev libavcodec-dev libavformat-dev libswscale-dev libtheora-dev libvorbis-dev libxvidcore-dev libx264-dev yasm libopencore-amrnb-dev libopencore-amrwb-dev libv4l-dev libxine2-dev

# Parallelism and linear algebra libraries:
RUN apt-get install -y libtbb-dev libeigen3-dev

# Python:
RUN apt-get install -y python-dev python-tk python-numpy python3-dev python3-tk python3-numpy

# Java:
RUN apt-get install -y ant default-jdk

# Documentation:
RUN apt-get install -y doxygen

# ROST dependencies
RUN apt-get install -y libboost-all-dev libflann-dev libfftw3-dev libopencv-dev libsndfile1-dev

# Set /code as working directory
WORKDIR /code

# Check out and build OpenCV latest 2 release
ENV VERSION 3.0.0
RUN wget http://sourceforge.net/projects/opencvlibrary/files/opencv-unix/${VERSION}/opencv-${VERSION}.zip/download -O opencv-${VERSION}.zip
RUN unzip opencv-${VERSION}.zip
RUN mkdir /code/opencv-${VERSION}/build
WORKDIR /code/opencv-${VERSION}/build
RUN cmake -DWITH_QT=ON -DWITH_OPENGL=ON -DFORCE_VTK=ON -DWITH_TBB=ON -DWITH_GDAL=ON -DWITH_XINE=ON -DBUILD_EXAMPLES=ON -DCMAKE_INSTALL_PREFIX=$CV_ROOT ..
RUN make -j4 && make install

# Install ROST command line tools
WORKDIR /code
RUN apt-get install -y git
RUN pip install --upgrade pip 
RUN pip install pysrt
RUN git clone https://gitlab.com/warplab/rost-cli.git

WORKDIR /code/rost-cli/build
# patch errors in the CMakeLists.txt files
RUN sed -i 's/OpenCV_INCLUDE_DIR/OpenCV_INCLUDE_DIRS/g' /code/rost-cli/sunshine/CMakeLists.txt
RUN cmake ..
ADD mjpeg_client.patch .
RUN patch /code/rost-cli/utils/src/mjpg_client.cpp mjpeg_client.patch
RUN make && make install

# Setup environment
ENV ROSTPATH /code/rost-cli
ENV PATH /opt/conda/bin:/code/rost-cli/bin:$PATH
