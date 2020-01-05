FROM ubuntu:14.04
MAINTAINER kueno

RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    curl \
    gfortran \
    git \
    graphicsmagick \
    libgraphicsmagick1-dev \
    libatlas-dev \
    libavcodec-dev \
    libavformat-dev \
    libboost-all-dev \
    libgtk2.0-dev \
    libjpeg-dev \
    liblapack-dev \
    libswscale-dev \
    pkg-config \
    python-dev \
    python-pip \
    software-properties-common \
    zip \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN pip install imageio
RUN pip install cython
RUN pip install numpy
RUN pip install pandas
RUN pip install scipy
RUN pip install scikit-learn
RUN pip install scikit-image

RUN cd ~ && \
    mkdir -p src && \
    cd src && \
    curl -L https://github.com/Itseez/opencv/archive/2.4.13.zip -o ocv.zip && \
    unzip ocv.zip && \
    cd opencv-2.4.13 && \
    mkdir release && \
    cd release && \
    cmake -D CMAKE_BUILD_TYPE=RELEASE \
          -D CMAKE_INSTALL_PREFIX=/usr/local \
          -D BUILD_PYTHON_SUPPORT=ON \
          -D WITH_OMP=ON \
          .. && \
    make -j8 && \
    make install

RUN cd ~ && \
    mkdir -p src && \
    cd src && \
    curl -L \
         http://dlib.net/files/dlib-19.2.tar.bz2 \
         -o dlib.tar.bz2 && \
    tar xf dlib.tar.bz2 && \
    cd dlib-19.2/python_examples && \
    mkdir build && \
    cd build && \
    cmake -DUSE_AVX_INSTRUCTIONS=ON ../../tools/python && \
    cmake --build . --config Release && \
    cp dlib.so /usr/local/lib/python2.7/dist-packages

RUN curl -s https://raw.githubusercontent.com/torch/ezinstall/master/install-deps | bash -e
RUN git clone https://github.com/torch/distro.git ~/torch --recursive
RUN cd ~/torch && ./install.sh && \
    cd install/bin && \
    ./luarocks install nn && \
    ./luarocks install dpnn && \
    ./luarocks install image && \
    ./luarocks install optim && \
    ./luarocks install csvigo && \
    ./luarocks install torchx