FROM kramergroup/vnc-ubuntu

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get -y install tzdata && \
    apt-get -yq install build-essential cmake libboost-all-dev \
                fftw3-dev libgsl-dev libtiff-dev \
                python3 python3-dev python3-numpy-dev python3-matplotlib \
                qt5-default qttools5-dev libqt5svg5-dev git && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN git clone --recurse-submodules https://github.com/scgmlz/BornAgain.git && \
    mkdir build && cd build && \
    cmake -DCMAKE_INSTALL_PREFIX=/opt/bornagain ../BornAgain && \
    make -j4 && \
    make install && \
    cd .. && rm -rf build && rm -rf BornAgain

RUN curl -LO https://download.jetbrains.com/python/pycharm-community-2018.1.4.tar.gz && \
    tar xvzf pycharm-community-2018.1.4.tar.gz && \
    mv pycharm-community-2018.1.4 /opt/pycharm && \
    rm pycharm-community-2018.1.4.tar.gz

COPY assets/menu.xml /etc/xdg/openbox/menu.xml
COPY assets/bashrc /etc/bash.bashrc
