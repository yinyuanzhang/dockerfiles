FROM nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04
ARG PYTHON_VERSION=3.6
RUN apt-get update && apt-get install -y --no-install-recommends \
         build-essential \
         cmake \
         git \
         curl \
         vim \
         ca-certificates \
         libjpeg-dev \
         libpng-dev \
         google-mock \
         libleveldb-dev\
         libopencv-dev \
         libeigen3-dev &&\
     rm -rf /var/lib/apt/lists/*


RUN curl -o ~/miniconda.sh -O  https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh  && \
     chmod +x ~/miniconda.sh && \
     ~/miniconda.sh -b -p /opt/conda && \
     rm ~/miniconda.sh && \
     /opt/conda/bin/conda install -y python=$PYTHON_VERSION numpy pyyaml scipy ipython mkl mkl-include cython typing conda-build scikit-learn pandas protobuf && \
     /opt/conda/bin/conda install -y -c conda-forge imbalanced-learn feather-format && \
     /opt/conda/bin/conda install -y -c pytorch magma-cuda90 && \
     /opt/conda/bin/conda clean -ya
ENV PATH /opt/conda/bin:$PATH
# ONNX
RUN git clone --recursive https://github.com/onnx/onnx.git /opt/onnx
RUN cd /opt/onnx; git submodule update --init --recursive;python setup.py install

RUN pip install --upgrade pip
RUN pip install sklearn_pandas

RUN conda install -c caffe2 -y pytorch-caffe2-cuda9.0-cudnn7

RUN apt-get update && apt-get install -y openssh-server

WORKDIR /workspace
RUN chmod -R a+w /workspace
