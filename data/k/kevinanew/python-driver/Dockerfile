FROM python:3.7-slim

RUN apt-get update && \
    apt-get install -y \
    curl \
    libsnappy-dev \
    build-essential \
    zlib1g-dev \
    libbz2-dev \
    libgflags-dev \
    liblz4-dev \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /tmp

RUN curl -L https://github.com/facebook/rocksdb/archive/v5.18.3.tar.gz | tar -xz && \
    cd rocksdb-5.18.3 && \
    make shared_lib && \
    make install-shared INSTALL_PATH=/usr && \
    cd .. && \
    rm -rf rocksdb-5.18.3 && \
    rm -rf /tmp

RUN pip install --no-cache-dir \
    cassandra-driver==3.19.0 \
    python-snappy==0.5.4 \
    python-rocksdb==0.7.0 \
    numpy==1.17.2 \
    ipython && \
    rm -rf /tmp
