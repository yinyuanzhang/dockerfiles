FROM nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04
LABEL maintainer="nelson@cs.washington.edu"

# caffe2 install with GPU support
# build with something like: docker build -t caffe2 .

# Install dependences via Apt
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    cmake \
    git \
    libgoogle-glog-dev \
    libgtest-dev \
    libiomp-dev \
    libleveldb-dev \
    liblmdb-dev \
    libopencv-dev \
    libsnappy-dev \
    libopenmpi-dev \
    openmpi-bin \
    openmpi-doc \
    libprotobuf-dev \
    protobuf-compiler \
    python-dev \
    python-pip \
    python-numpy \
    python-pydot \
    python-setuptools \
    python-scipy \
    wget \
    libgflags-dev \
    ninja-build \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependences via pip
RUN pip install --no-cache-dir --upgrade pip==9.0.3 setuptools wheel && \
    pip install --no-cache-dir \
    future \
    numpy \
    protobuf \
    graphviz \
    hypothesis \
    ipython \
    jupyter \
    matplotlib \
    notebook \
    pydot \
    python-nvd3 \
    pyyaml \
    requests \
    scikit-image \
    scipy \
    flask \
    setuptools \
    six \
    tornado \
    mkl-devel \
    typing \
    ninja

# Clone last released version
RUN git clone https://github.com/pytorch/pytorch.git && cd pytorch && \
    git fetch --tags && \
    git checkout tags/v0.4.1 -b v0.4.1 && \
    git submodule update --init --recursive

# Build
RUN cd pytorch && \
    FULL_CAFFE2=1 EXTRA_CAFFE2_CMAKE_FLAGS="-DUSE_NATIVE_ARCH=ON" python setup.py install && \
    cd .. && rm -rf pytorch

ENV PYTHONPATH /usr/local
