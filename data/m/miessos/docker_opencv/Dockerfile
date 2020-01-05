FROM debian:jessie

MAINTAINER miessos, https://github.com/miessos

# Keep Debian up to date
RUN apt-get -y update && apt-get -y upgrade && apt-get -y dist-upgrade && apt-get -y autoremove

# Install dependencies
RUN apt-get install -y build-essential \
    cmake \
    qt5-default \
    libvtk6-dev \
    zlib1g-dev \
    libjpeg-dev \
    libwebp-dev \
    libpng-dev \
    libtiff5-dev \
    libjasper-dev \
    libopenexr-dev \
    libgdal-dev \
    libdc1394-22-dev \
    libavcodec-dev \
    libavformat-dev \
    libswscale-dev \
    libtheora-dev \
    libvorbis-dev \
    libxvidcore-dev \
    libx264-dev yasm \
    libopencore-amrnb-dev \
    libopencore-amrwb-dev \
    libv4l-dev \
    libxine2-dev \
    libtbb-dev \
    libeigen3-dev \
    python-dev \
    python-tk \
    python-numpy \
    python3-dev \
    python3-tk \
    python3-numpy \
    ant \
    default-jdk \
    doxygen \
    unzip \
    wget

# Create user developer
RUN export uid=1000 gid=1000 && \
    mkdir -p /home/developer && \
    mkdir -p /etc/sudoers.d && \
    echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >> /etc/passwd && \
    echo "developer:x:${uid}:" >> /etc/group && \
    echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \
    chmod 0440 /etc/sudoers.d/developer && \
    chown ${uid}:${gid} -R /home/developer

#USER developer
ENV HOME /home/developer

# Install library
WORKDIR $HOME
RUN wget https://github.com/Itseez/opencv/archive/3.1.0.zip && \
    unzip 3.1.0.zip && \
    rm 3.1.0.zip && \
    mv opencv-3.1.0 OpenCV && \
    cd OpenCV && \
    mkdir build && \
    cd build && \
    cmake -DWITH_QT=ON -DWITH_OPENGL=ON -DFORCE_VTK=ON -DWITH_TBB=ON -DWITH_GDAL=ON -DWITH_XINE=ON -DBUILD_EXAMPLES=ON .. && \
    make -j4 && \
    make install && \
    ldconfig

USER developer

CMD cd ~
