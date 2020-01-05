#2018/10/2時点でcupyがcuda10.0に対応してないっぽいので9.0を使う
FROM nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04

ENV TZ=Asia/Tokyo \
  DEBIAN_FRONTEND=noninteractive \
  LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH \
  PATH=/usr/local/cuda/bin:$PATH \
  LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH

RUN apt-get update \
  && apt-get upgrade -y \
  && apt-get install -y \
    tzdata tk-dev xvfb vim wget git \
    python3-pip python3-tk \
    doxygen doxygen-gui graphviz \
    sudo zip unzip tar \
  && pip3 install \
    numpy matplotlib scipy cython \
    pillow opencv-contrib-python imagehash pydot sklearn \
    tensorflow-gpu keras h5py \
    chainer \
    torch torchvision \
    jupyter easydict pandas kaggle \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*
