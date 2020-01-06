FROM ubuntu:18.04

RUN apt-get update && apt-get install -y \
        libarchive-dev libjudy-dev pkg-config python-future make \
        python-ply jq libjudy-dev libjson-c-dev libcmph-dev libc6-dev libjemalloc-dev \
        git build-essential clang libcurl4-openssl-dev cmake \
        && rm -rf /var/lib/apt/lists/*

WORKDIR /var
RUN git clone https://github.com/traildb/traildb.git
RUN cd traildb && ./waf configure && ./waf install


RUN git clone https://github.com/traildb/traildb-python.git
RUN cd traildb-python && python setup.py install

RUN git clone https://github.com/traildb/trck.git && echo
RUN cd trck && \
        git submodule update --init --remote --recursive && \
        CC=clang make install && ldconfig && \
        CC=clang make test

