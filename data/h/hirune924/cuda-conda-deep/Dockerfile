#FROM nvidia/cuda:10.0-cudnn7-devel-ubuntu18.04
FROM nvidia/cuda:10.0-cudnn7-devel-ubuntu16.04

ARG DEBIAN_FRONTEND=noninteractive

MAINTAINER "@hirune924"

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PATH /opt/conda/bin:$PATH

RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-certificates \
    libglib2.0-0 libxext6 libsm6 libxrender1 \
    git mercurial subversion

#RUN wget --quiet https://repo.anaconda.com/archive/Anaconda3-5.1.0-Linux-x86_64.sh -O ~/anaconda.sh && \
#RUN wget --quiet https://repo.anaconda.com/archive/Anaconda3-5.3.0-Linux-x86_64.sh -O ~/anaconda.sh && \
RUN wget --quiet https://repo.anaconda.com/archive/Anaconda3-2019.07-Linux-x86_64.sh -O ~/anaconda.sh && \
    /bin/bash ~/anaconda.sh -b -p /opt/conda && \
    rm ~/anaconda.sh && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate base" >> ~/.bashrc

RUN apt-get update --fix-missing && apt-get install -y curl grep sed dpkg && \
    TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep -o "/v.*\"" | sed 's:^..\(.*\).$:\1:'` && \
    curl -L "https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.deb" > tini.deb && \
    dpkg -i tini.deb && \
    rm tini.deb && \
    apt-get clean

RUN apt-get update --fix-missing && apt-get install -y unzip htop vim \
    && \
    apt-get clean && \
    apt-get autoremove && \
    rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*

#RUN conda install -y pytorch=1.1.0 torchvision cudatoolkit=10.0 -c pytorch
RUN conda install -y pytorch torchvision cudatoolkit=10.0 -c pytorch && \
    conda install -y absl-py

RUN pip install adabound tensorboardX pytorch-lightning catalyst[all] torchsummary lmdb && \
    pip install --extra-index-url https://developer.download.nvidia.com/compute/redist/cuda/10.0 nvidia-dali

RUN git clone https://github.com/NVIDIA/apex && \
    cd apex && \
    pip install -v --no-cache-dir --global-option="--cpp_ext" --global-option="--cuda_ext" ./ && \
    cd .. && rm -rf apex\
## Install useful packages using apt-get
#RUN apt-get update && apt-get install -y \
#		build-essential \
#		make \
#		cmake \
#		g++ \
#		gcc \
#		git \
#		unzip \
#		vim \
#		wget \
#		curl \
#                python3-tk \
#		&& \
#	apt-get clean && \
#	apt-get autoremove && \
#	rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*
#
#
## Install pip
#RUN apt-get update && apt-get install -y python-pip python3-pip \
#		&& \
#	apt-get clean && \
#	apt-get autoremove && \
#	rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*
#
#
## Install useful Python packages using pip
#RUN pip3 --no-cache-dir install --upgrade ipython && \
#    pip3 --no-cache-dir install \
#                numpy \
#                scipy \
#                pandas \
#                matplotlib \
#                scikit-image \
#                scikit-learn \
#                h5py \
#                tqdm \
#                absl-py \
#                Pillow \
#                opencv-python \
#                opencv-contrib-python
#
## Install PyTorch
#RUN pip3 install https://download.pytorch.org/whl/cu100/torch-1.0.1.post2-cp36-cp36m-linux_x86_64.whl && \
#    pip3 install torchvision
#
## Install TensorFlow
### Current stable release for CPU-only
##RUN pip3 install tensorflow
##
### Preview nightly build for CPU-only (unstable)
##RUN pip3 install tf-nightly
##
### Install TensorFlow 2.0 Alpha
##RUN pip3 install tensorflow==2.0.0-alpha0
##
### Current stable release for GPU
##RUN pip3 install tensorflow-gpu
##
### Preview nightly build for GPU (unstable)
##RUN pip3 install tf-nightly-gpu
##
### Install TensorFlow 2.0 Alpha for GPU
#RUN pip3 install tensorflow-gpu==2.0.0-alpha0
#
#
## Install keras
#RUN pip3 install keras
#
#
## Install JupyterLab
#RUN pip3 install jupyterlab
#
#
## Install Chainer
##RUN apt-get update && apt-get install -y \
##                python-dev \
##                python-pip \
##                python-wheel \
##                python-setuptools \
##                && \
##    pip3 install -U setuptools pip && \
#RUN pip3 install cupy-cuda100 chainer 
#
#
#
### Install Albumentations
#RUN pip3 install albumentations
