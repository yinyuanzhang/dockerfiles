FROM nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04 

RUN echo "deb http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1604/x86_64 /" > /etc/apt/sources.list.d/nvidia-ml.list

RUN apt-get update && apt-get install -y --no-install-recommends \
         build-essential \
         cmake \
         git \
         curl \
         vim \
         ca-certificates \         
         libjpeg-dev \
         libpng-dev &&\
     rm -rf /var/lib/apt/lists/*

##########################################
# Install anaconda2

RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-certificates \
    libglib2.0-0 libxext6 libsm6 libxrender1 \
    git mercurial subversion

RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
    wget --quiet https://repo.continuum.io/archive/Anaconda2-5.0.1-Linux-x86_64.sh -O ~/anaconda.sh && \
    /bin/bash ~/anaconda.sh -b -p /opt/conda && \
    rm ~/anaconda.sh

ENV PATH /opt/conda/bin:$PATH

##########################################
# Install java

RUN apt-get update && apt-get install -y --no-install-recommends \
    default-jre \
    default-jdk

#########################################
# Install caffe necessary stuff

RUN apt-get install -y libprotobuf-dev libleveldb-dev libsnappy-dev libopencv-dev libhdf5-serial-dev protobuf-compiler
RUN apt-get install -y --no-install-recommends libboost-all-dev

RUN apt-get install -y \
        libatlas-base-dev \
        libgflags-dev \
        libgoogle-glog-dev \
        liblmdb-dev

RUN apt-get install -y libnccl2=2.4.2-1+cuda9.0 libnccl-dev=2.4.2-1+cuda9.0

########################################
# Install easydict opencv
RUN pip install easydict
RUN conda install -y opencv

# Install protobuf
RUN pip install protobuf

WORKDIR /workspace
RUN chmod -R a+w /workspace
