FROM phantomape/base:latest

# Build RocksDB
RUN git clone https://github.com/facebook/rocksdb.git \
    && cd rocksdb \
    && make -j $(nproc) static_lib \
    && make -j $(nproc) shared_lib \
    && make install

RUN pip3 install python-rocksdb

ENTRYPOINT /bin/bash
