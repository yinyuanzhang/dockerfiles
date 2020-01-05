FROM nvidia/cuda:10.0-cudnn7-devel-ubuntu16.04

RUN sed -i "s/archive.ubuntu./mirrors.aliyun./g" /etc/apt/sources.list
RUN sed -i "s/deb.debian.org/mirrors.aliyun.com/g" /etc/apt/sources.list
RUN sed -i "s/security.debian.org/mirrors.aliyun.com\/debian-security/g" /etc/apt/sources.list
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        nano \
        cmake \
        git \
        wget \
        libatlas-base-dev \
        libboost-all-dev \
        libgflags-dev \
        libgoogle-glog-dev \
        libhdf5-serial-dev \
        libleveldb-dev \
        liblmdb-dev \
        libopencv-dev \
        libprotobuf-dev \
        libsnappy-dev \
        protobuf-compiler \
        python-dev \
        python-numpy \
        python-pip \
        python-setuptools \
        python-scipy && \
    rm -rf /var/lib/apt/lists/*
    
RUN git clone https://github.com/HyperDenton/bottom-up-attention.git
RUN cp -r ./bottom-up-attention /opt/butd

ENV CAFFE_ROOT=/opt/butd/caffe
WORKDIR $CAFFE_ROOT

# Build and install caffe
RUN pip2 install --upgrade pip && \
    cd python && for req in $(cat requirements.txt) pydot scikit-image opencv-python; do pip install $req -i https://pypi.tuna.tsinghua.edu.cn/simple; done && cd .. && \
    make -j"$(nproc)" && \
    make pycaffe

# Build fast rcnn lib
RUN cd /opt/butd/lib && make  

# Set ENV
ENV PYCAFFE_ROOT $CAFFE_ROOT/python
ENV PYTHONPATH $PYCAFFE_ROOT:$PYTHONPATH
ENV PATH $CAFFE_ROOT/build/tools:$PYCAFFE_ROOT:$PATH
RUN echo "$CAFFE_ROOT/build/lib" >> /etc/ld.so.conf.d/caffe.conf && ldconfig

WORKDIR /workspace
