FROM aistairc/aaic:ubuntu16.04-cuda9.0-cudnn7-openmpi2.1.3
MAINTAINER ndtn97

ARG SM_TAG
SHELL ["/bin/bash", "-c"]

RUN echo "building for ${SM_TAG}"

CMD echo "running..."

RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/*
RUN apt-get clean
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install --no-install-recommends gcc g++ cmake vim build-essential python3-dev git less openssh-server zlib1g-dev libjpeg-dev wget -y

ENV LD_LIBRARY_PATH /usr/local/cuda/lib64:$LD_LIBRARY_PATH
ENV PATH /usr/local/cuda/bin:$PATH

RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
RUN sh Miniconda3-latest-Linux-x86_64.sh -b -p /opt/miniconda3

ENV PATH /opt/miniconda3/bin:$PATH
RUN conda install -y python=3.6.8
RUN conda config --append channels conda-forge
RUN conda install -y faiss-gpu cudatoolkit=9.0 -c pytorch
RUN conda install -y flake8 numpy scipy scikit-learn scikit-image nose anaconda tensorboardx umap-learn
RUN conda install pytorch torchvision cudatoolkit=9.0 -c pytorch
RUN yes | pip install wheel

RUN pip uninstall --yes pillow
RUN yes | CC="cc -mavx2" pip install -U --force-reinstall pillow-simd

RUN git clone https://github.com/src-d/kmcuda
WORKDIR /kmcuda/src
RUN sed -e 's/"cmake"/"cmake","-DCUDA_ARCH='${SM_TAG:2}'"/g' ./setup.py > ./setup2.py
RUN mkdir whl
RUN CUDA_TOOLKIT_ROOT_DIR=/usr/local/cuda python setup2.py bdist_wheel -d whl
RUN yes | pip install ./whl/*

WORKDIR /
RUN git clone https://github.com/cudamat/cudamat/
WORKDIR /cudamat
RUN mkdir whl
RUN NVCCFLAGS=-arch=sm_${SM_TAG:2} python setup.py bdist_wheel -d whl
RUN yes | pip install ./whl/*

WORKDIR /
RUN git clone https://github.com/ebattenberg/ggmm.git
WORKDIR /ggmm
RUN yes | pip install .

WORKDIR /
RUN rm -rf Miniconda3-latest-Linux-x86_64.sh kmcuda cudamat ggmm

WORKDIR /
RUN git clone https://github.com/NVIDIA/apex
WORKDIR /apex
RUN yes | pip install -v --no-cache-dir --global-option="--cpp_ext" --global-option="--cuda_ext" ./

WORKDIR /

RUN pip install adabound
