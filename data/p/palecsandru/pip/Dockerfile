FROM palecsandru/centos7-pythondeps

RUN wget -q https://github.com/python/cpython/archive/v2.7.16.tar.gz -O cpython.tar.gz && \
    mkdir cpython && \
    tar -xf cpython.tar.gz -C cpython --strip 1 && \
    rm -f cpython.tar.gz && \
    cd cpython && \
    ./configure && \
    make -j `cat /proc/cpuinfo | grep processor | wc -l` && \
    make install && \
    cd .. && \
    rm -rf cpython
RUN ln -s /usr/local/bin/python2 /usr/local/bin/provided
