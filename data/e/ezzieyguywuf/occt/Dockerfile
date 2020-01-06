FROM ubuntu:14.04
RUN apt-get update \
    && apt-get -y install \
        build-essential \
        cmake \
        git \
        tcl-dev \
        tk-dev \
        libfreetype6-dev \
        libgl1-mesa-dev \ 
        libxmu-dev \
        libxi-dev \
    && rm -rf /var/lib/apt/lists/* \
    && cd / \
    && git clone https://git.dev.opencascade.org/repos/occt.git \
    && cd /occt \ 
    && git checkout -b docker V7_3_0 \
    && mkdir build \ 
    && cd build \ 
    && cmake .. \ 
    && make -j4 install \
    && cd / \
    && rm -rf /occt \
    && apt-get --auto-remove -y purge \
        build-essential \
        cmake \
        git \
        tcl-dev \
        tk-dev \
        libfreetype6-dev \
