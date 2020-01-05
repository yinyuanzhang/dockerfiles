FROM nvidia/cuda:9.2-cudnn7-devel

ENV PYTHON_VERSION=3.6.6

RUN apt-get -qq update &&  \
    apt-get -qq install --assume-yes build-essential git wget pkg-config locales \
      gfortran libopenblas-dev libssl-dev zlib1g-dev && \
    rm -rf /var/lib/apt/lists/* && \
    # install python
    wget https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tgz && \
    tar -zxf Python-$PYTHON_VERSION.tgz && cd Python-$PYTHON_VERSION && \
    ./configure && make && make install && cd .. && rm -fr Python-$PYTHON_VERSION && \
    python3 --version

RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && locale-gen
ENV LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8

