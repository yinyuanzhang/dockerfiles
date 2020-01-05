
FROM nvidia/cuda:9.0-cudnn7-runtime-ubuntu16.04

# Maatwerk & Advies Deep learning Image
# CUDA 9.2, Python 3.7, Pytorch 0.4.1

ARG ARCH=x86_64
ARG PYTHON_VERSION=3.7.0
ARG MAJOR_VERSION=3.7
ARG TCH=0.4.1.post2
ARG CU=90
ARG PY=37

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

RUN apt-get update \
 && apt-get dist-upgrade -y \
 && apt-get install -y \
     build-essential \
     libboost-python-dev \
     libbz2-dev \
     libexpat1-dev \
     libffi-dev \
     libgdbm-dev \
     libjpeg-dev \
     liblapack-dev \
     liblzma-dev \
     libncurses5-dev \
     libreadline-dev \
     libsm6 \
     libspatialindex-dev \
     libssl-dev \
     libsqlite3-dev \
     libxml2-dev \
     libxslt-dev \
     lzma-dev \
     git \
     gfortran \
     wget \
     xz-utils \
     zlib1g-dev \
 && apt-get clean && rm -rf /var/lib/apt/lists/*

 RUN cd /tmp \
  && TARGET_ARCH="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)" \
  && wget https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz \
  && tar xvf Python-${PYTHON_VERSION}.tgz \
  && cd Python-${PYTHON_VERSION} \
  && ./configure \
     --build="$TARGET_ARCH" \
     --with-lto \
     --with-system-ffi \
     --with-system-expat \
     --enable-ipv6 \
     --enable-optimizations \
     --enable-shared \
     --enable-loadable-sqlite-extensions \
  && make -j4 \
  && make altinstall \
  && rm -rf /tmp/Python*

  # dynamic library bindings and test removal
  RUN ldconfig -v \
   && cd /usr/local/bin \
   && find /usr/local -depth \
      \( \( -type d -and \( -name test -or -name tests -or -name __pycache__ \) \) -or \
         \( -type f -and \( -name '*.pyc' -or -name '*.pyo' \) \) \) \
      -exec rm -rf '{}' + \
   && find /var/lib/apt/lists \
           /usr/share/man \
           /usr/share/doc \
           /var/log \
      -type f -exec rm -rf '{}' +


  # symlink creation
  RUN cd /usr/local/bin \
   && ln -sf easy_install-${MAJOR_VERSION} easy_install \
   && ln -sf idle${MAJOR_VERSION} idle \
   && ln -sf pydoc${MAJOR_VERSION} pydoc \
   && ln -sf python${MAJOR_VERSION} python \
   && ln -sf python-config${MAJOR_VERSION} python-config \
   && ln -sf pip${MAJOR_VERSION} pip \
   && pip${MAJOR_VERSION} --no-cache-dir install --upgrade pip


WORKDIR /app
ADD . /app

RUN python -m pip install cython torch
RUN python -m pip install -r deps/requirements.txt
