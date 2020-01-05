FROM nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04

ENV PYTHON_VERSION 3.7.4
ENV PYTORCH_VERSION 1.1.0
ENV TORCHVISION_VERSION 0.3.0

ENV PYTHON_ROOT /root/local/python-$PYTHON_VERSION
ENV PATH $PYTHON_ROOT/bin:$PATH
ENV PYENV_ROOT /root/.pyenv

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    git \
    libbz2-dev \
    libffi-dev \
    liblzma-dev \
    libncurses5-dev \
    libncursesw5-dev \
    libreadline-dev \
    libsqlite3-dev \
    libssl-dev \
    llvm \
    python-openssl \
    tk-dev \
    wget \
    xz-utils \
    zlib1g-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# python build
RUN git clone https://github.com/pyenv/pyenv.git $PYENV_ROOT && \
    $PYENV_ROOT/plugins/python-build/install.sh && \
    /usr/local/bin/python-build -v $PYTHON_VERSION $PYTHON_ROOT && \
    rm -rf $PYENV_ROOT

RUN pip install --upgrade pip && pip install \
    torch==$PYTORCH_VERSION \
    torchvision==$TORCHVISION_VERSION
