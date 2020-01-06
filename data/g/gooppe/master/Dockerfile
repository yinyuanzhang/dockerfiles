FROM nvidia/cuda:10.1-cudnn7-devel-ubuntu18.04

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

ENV CUDA_PATH /usr/local/cuda
ENV TZ=Europe/Moscow

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential ca-certificates \
    mc git vim zsh curl wget \
    python3-dev python3-pip

RUN ln -sf $(which python3) /usr/bin/python && \
    ln -sf $(which pip3) /usr/bin/pip

RUN pip install --upgrade pip wheel setuptools
RUN pip install torch

RUN sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
COPY vimrc /root/.vimrc

ENTRYPOINT zsh