# CPU running environment container

ARG UBUNTU_VERSION=16.04

FROM ubuntu:${UBUNTU_VERSION} as base
LABEL maintainer="nobody"


# Needed for string substitution 
SHELL ["/bin/bash", "-c"]

ENV DEBIAN_FRONTEND noninteractive

# fix apt-utils warning
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils

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
        keras \
        keras_applications \
        keras_preprocessing \
        matplotlib \
        numpy==1.16.4 \
        pandas \
        scipy \
        sklearn \
        python-dateutil \
        hyperopt \
        gensim \
        torch \
        torchvision \
        tensorflow==1.14.0

# create folder for automatical mounting
RUN mkdir -p /extra /xdisk /rsgrps /cm/shared /cm/local



