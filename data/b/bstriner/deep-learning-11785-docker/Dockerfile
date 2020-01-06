# https://hub.docker.com/r/kaixhin/cuda-theano/~/dockerfile/
# https://github.com/autolab/Tango/blob/master/vmms/Dockerfile
# https://github.com/tensorflow/tensorflow/blob/master/tensorflow/tools/docker/Dockerfile
# https://github.com/pytorch/pytorch/blob/master/Dockerfile
# Autolab - autograding docker image for machine learning

FROM bstriner/deep-learning-11785-docker:autograding_image
MAINTAINER Benjamin Striner <bstriner@gmail.com>

# Python3
RUN apt-get update --fix-missing
RUN apt-get install -y gcc
RUN apt-get install -y make
RUN apt-get install -y build-essential
RUN apt-get update && apt-get install -y \
  gfortran \
  git \
  wget \
  curl \
  pkg-config \
  python3 \
  python3-dev \
  liblapack-dev \
  libopenblas-dev \
  rsync \
  software-properties-common \
  unzip \
  libfreetype6-dev \
  libpng12-dev \
  libzmq3-dev \
  python3-pip \
  python3-nose \
  python3-numpy \
  python3-scipy
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade six
RUN pip3 install pyOpenSSL ndg-httpsclient pyasn1

# cmake
WORKDIR /tmp
RUN wget http://www.cmake.org/files/v3.10/cmake-3.10.0.tar.gz
RUN tar xf cmake-3.10.0.tar.gz
RUN cd cmake-3.10.0 && ./configure && make && make install

# Tensorflow
RUN pip3 install \
        Pillow \
        h5py \
        ipykernel \
        jupyter \
        matplotlib \
        pandas \
        sklearn \
        && \
    python3 -m ipykernel.kernelspec
RUN pip3 install tensorflow

# Pytorch
WORKDIR /tmp
RUN pip3 install pyyaml mkl setuptools cmake cffi
RUN git clone --recursive https://github.com/pytorch/pytorch.git && cd pytorch && python3 setup.py install
RUN pip3 install --no-deps torchvision
RUN rm -Rf pytorch
# RUN git clone https://github.com/pytorch/vision.git && cd vision && pip install -v .

# Misc Python
RUN pip3 install pytest nose nose-parameterized pytest-pep8 pytest-helpers-namespace
RUN pip3 install h5py lmdb tqdm

# Datasets
RUN mkdir /data
WORKDIR /data
RUN wget https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz
RUN tar xzf cifar-10-python.tar.gz
RUN rm cifar-10-python.tar.gz
ENV DATA_PATH=/data
ENV CIFAR10_PATH=/data/cifar-10-batches-py

# Cleanup
RUN apt-get clean
RUN apt-get -y autoremove
