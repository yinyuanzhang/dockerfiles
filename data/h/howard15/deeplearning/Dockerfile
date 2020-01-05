
ARG UBUNTU_VERSION=16.04

ARG CUDA=10.1
FROM nvidia/cuda:${CUDA}-base-ubuntu${UBUNTU_VERSION} as base
# ARCH and CUDA are specified again because the FROM directive resets ARGs
# (but their default value is retained if set previously)
ARG UBUNTU_VERSION
ARG CUDA
ARG CUDNN=7.6.4.38
ARG NCCL=2.4.8
ARG LIBNVINFER=6.0.1-1
ARG LIBNVINFER_MAJOR_VERSION=6

# Needed for string substitution 
SHELL ["/bin/bash", "-c"]

ENV DEBIAN_FRONTEND noninteractive

# fix apt-utils warning
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils

# Pick up some TF dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        cuda-command-line-tools-${CUDA/./-} \
        libcublas10=10.1.0.105-1 \
        cuda-cufft-${CUDA/./-} \
        cuda-curand-${CUDA/./-} \
        cuda-cusolver-${CUDA/./-} \
        cuda-cusparse-${CUDA/./-} \
        curl \
        libcudnn7=${CUDNN}-1+cuda${CUDA} \
        libnccl2=${NCCL}-1+cuda${CUDA} \
        libfreetype6-dev \
        libhdf5-serial-dev \
        libzmq3-dev \
        pkg-config \
        software-properties-common \
        unzip

RUN apt-get update \
        && apt-get install -y --no-install-recommends libnvinfer${LIBNVINFER_MAJOR_VERSION}=${LIBNVINFER}+cuda${CUDA} \
        libnvinfer-plugin${LIBNVINFER_MAJOR_VERSION}=${LIBNVINFER}+cuda${CUDA} \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/*

# fix warning: underlay of /usr/bin/nvidia-smi required more than 50 bind mounts
RUN touch /usr/bin/nvidia-smi /usr/bin/nvidia-persistenced /usr/bin/nvidia-debugdump /usr/bin/nvidia-cuda-mps-server /usr/bin/nvidia-cuda-mps-control

# create folder for automatical mounting
RUN mkdir -p /extra /xdisk /rsgrps /cm/shared /cm/local

# For CUDA profiling, TensorFlow requires CUPTI.
ENV LD_LIBRARY_PATH /usr/local/cuda/extras/CUPTI/lib64:/usr/local/cuda/lib64:$LD_LIBRARY_PATH

# Link the libcuda stub to the location where tensorflow is searching for it and reconfigure
# dynamic linker run-time bindings
RUN ln -s /usr/local/cuda/lib64/stubs/libcuda.so /usr/local/cuda/lib64/stubs/libcuda.so.1 \
    && echo "/usr/local/cuda/lib64/stubs" > /etc/ld.so.conf.d/z-cuda-stubs.conf \
    && ldconfig

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        software-properties-common \
        python3-pip \
 && add-apt-repository -y ppa:deadsnakes/ppa \
 && apt-get update \
 && apt-get install -y python3.6 python3.6-dev \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN touch /usr/bin/python3 && rm /usr/bin/python3
RUN ln -s /usr/bin/python3.6 /usr/bin/python3

ARG USE_PYTHON_3_NOT_2=1
ARG _PY_SUFFIX=${USE_PYTHON_3_NOT_2:+3}
ARG PYTHON=python${_PY_SUFFIX}
ARG PIP=pip${_PY_SUFFIX}

# See http://bugs.python.org/issue19846
ENV LANG C.UTF-8

RUN apt-get update && apt-get install -y \
    ${PYTHON} \
    ${PYTHON}-pip

RUN ${PIP} --no-cache-dir install --upgrade \
    pip \
    setuptools

# Some TF tools expect a "python" binary
RUN ln -s $(which ${PYTHON}) /usr/local/bin/python 

RUN ${PIP} --no-cache-dir install --upgrade \
        Pillow \
        h5py \
        ipykernel \
        jupyter \
        jupyter_http_over_ws \
        ipdb \
        pudb \
        spyder-kernels \
        Keras \
        Keras-Applications \
        Keras-Preprocessing \
        matplotlib \
        numpy \
        pandas \
        scipy \
        sklearn \
        python-dateutil \
        hyperopt \
        lifelines \
        gensim \
        tensorflow-gpu \
        torch \
        torchvision \
        transformers

RUN jupyter serverextension enable --py jupyter_http_over_ws
#jupyter notebook --notebook-dir=/tf --ip 0.0.0.0 --no-browser --allow-root


