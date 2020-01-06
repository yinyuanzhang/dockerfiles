FROM phantomape/base:latest

ENV WITH_SNAPPY=/usr

# Build MyRocks
RUN git clone https://github.com/facebook/mysql-5.6.git \
    && cd mysql-5.6 \
    && git submodule init \
    && git submodule update \
    && cmake . -DCMAKE_BUILD_TYPE=RelWithDebInfo -DWITH_SSL=system \
    -DWITH_ZLIB=bundled -DMYSQL_MAINTAINER_MODE=0 -DENABLED_LOCAL_INFILE=1 \
    -DENABLE_DTRACE=0 -DCMAKE_CXX_FLAGS="-march=native" \
    && make -j $(nproc)

ENTRYPOINT /bin/bash
