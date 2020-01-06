FROM patdiscvrd/ubuntu-cuda

MAINTAINER Patrick Wenzel

# Docker container for keras with GPU support

# Get latest ubuntu packages
RUN apt-get update -y

# Get dependencies
RUN apt-get install -y build-essential gfortran g++ libopenblas-dev git curl nano

# Install Python
RUN apt-get install -y python python-numpy python-scipy python-dev python-setuptools libatlas-dev libatlas3gf-base python-pip python-nose python-yaml python-imaging python-matplotlib ipython ipython-notebook python-pandas python-sympy python-h5py libhdf5-dev

# Update
RUN rm -rf /var/lib/apt/lists/*
RUN apt-get update -y

# Install Theano
RUN pip install Theano

# Install Cython
RUN pip install Cython

# Install Keras
RUN git clone https://github.com/fchollet/keras.git
WORKDIR /keras
RUN python setup.py install

# Enable GPU in Theano
RUN cd ~ && echo "[global]\ndevice=gpu0\nfloatX=float32\n\n[cuda]\nroot=/usr/local/cuda" > .theanorc
