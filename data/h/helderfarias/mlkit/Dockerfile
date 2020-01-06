FROM python:3.7
LABEL Helder Farias <helderfarias@gmail.com>

ENV DLIB_VERSION=19.6
ENV OPENCV_VERSION=3.4.6

RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    pkg-config \
    graphicsmagick \
    libx11-dev \
    libatlas-base-dev \
    libgraphicsmagick1-dev \
    libatlas-dev \
    libavcodec-dev \
    libavformat-dev \
    libboost-all-dev \
    libgtk-3-dev  \
    libboost-python-dev \
    libjpeg-dev \
    liblapack-dev \
    libswscale-dev \
    python3-dev \
    python3-pip \
    python-numpy \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN pip install numpy scipy matplotlib scikit-image scikit-learn ipython

RUN cd ~ && \
    mkdir -p dlib-tmp && \
    cd dlib-tmp && \
    wget http://dlib.net/files/dlib-$DLIB_VERSION.tar.bz2 && \
    tar xvf dlib-$DLIB_VERSION.tar.bz2 && \
    cd dlib-$DLIB_VERSION && \
    mkdir build && \
    cd build && \
    cmake .. && \
    cmake --build . --config Release && \
    make install && \
    ldconfig && \
    cd .. && \
    python setup.py install && \
    pip install dlib && \
    cd .. && \
    rm -rf ~/dlib-tmp

RUN cd ~ && \
    mkdir -p ocv-tmp && \
    cd ocv-tmp && \
    curl -L https://github.com/opencv/opencv/archive/$OPENCV_VERSION.zip -o ocv.zip && \
    unzip ocv.zip && \
    cd opencv-$OPENCV_VERSION && \
    mkdir release && \
    cd release && \
    cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D BUILD_PYTHON_SUPPORT=ON \
    .. && \
    make -j8 && \
    make install && \
    rm -rf ~/ocv-tmp

RUN cd ~ && \
    wget https://dl.google.com/go/go1.12.5.linux-amd64.tar.gz && \
    tar xvzf go1.12.5.linux-amd64.tar.gz && \
    mv go /usr/local && \
    ln -s /usr/local/go/bin/go /usr/local/bin/go && \
    rm go1.12.5.linux-amd64.tar.gz

RUN pip install face_recognition imutils