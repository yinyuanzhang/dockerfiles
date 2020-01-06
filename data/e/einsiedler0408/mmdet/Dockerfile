FROM nvidia/cuda:9.2-cudnn7-devel-ubuntu16.04

# Labels for the docker
LABEL description="This docker has pytorch 0.4.1 in miniconda python36 with cuda 9.2, and cudnn 7.0." \
      tag="pytorch0.4.1-py36"

RUN apt-get update && apt-get install -y --no-install-recommends --allow-change-held-packages \
         git \
         libgtk2.0-dev \
         vim \
         screen \
         ca-certificates \
         libnccl2 \
         libnccl-dev \
         libjpeg-dev \
         curl \
		 wget \
	     libopenblas-dev \
	     libopencv-dev \
	     libyaml-dev \
         libpng-dev &&\
         rm -rf /var/lib/apt/lists/*

ENV PYTHON_VERSION=3.6

RUN curl -o ~/miniconda.sh -O  https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh  && \
     chmod +x ~/miniconda.sh && \
     ~/miniconda.sh -b -p /opt/conda && \
     rm ~/miniconda.sh && \
     /opt/conda/bin/conda create -y --name pytorch-py$PYTHON_VERSION python=$PYTHON_VERSION numpy pyyaml scipy ipython mkl && \
     /opt/conda/bin/conda clean -ya

ENV PATH /opt/conda/envs/pytorch-py$PYTHON_VERSION/bin:$PATH

RUN /opt/conda/bin/conda install --name pytorch-py$PYTHON_VERSION cuda92 pytorch=0.4.1 torchvision -c pytorch && \
    /opt/conda/bin/conda clean -ya

RUN /opt/conda/envs/pytorch-py$PYTHON_VERSION/bin/pip install cython tensorflow tensorboardX

WORKDIR /workspace
RUN chmod -R a+w /workspace
