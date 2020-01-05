FROM ubuntu:19.04

ENV DEBIAN_FRONTEND=noninteractive TZ='America/New_York'

RUN apt-get update && apt-get install -yq locales wget && locale-gen "en_US.UTF-8"

ENV LANG=en_US.UTF-8

RUN apt-get update && apt-get install -yq python3 ipython3 python3-pip \
    cython3 python3-opencv python3-tqdm python3-numpy python3-skimage \
    python3-scipy python3-sklearn python3-h5py python3-matplotlib \
    python3-requests python3-psutil python3-pandas python3-pypandoc \
    unzip git emacs-nox tmux youtube-dl time ffmpeg imagemagick x264 x265 \
    && apt-get upgrade -yq \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade mxnet-mkl gluon Pillow youtube_dl easydict

RUN git clone --recursive https://github.com/deepinsight/insightface.git

RUN ln -s /usr/bin/python3 /usr/bin/python

RUN cd insightface/RetinaFace && make

RUN cd /insightface/python-package && python3 setup.py install && pip3 uninstall -y opencv-python
