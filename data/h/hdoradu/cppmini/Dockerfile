FROM ubuntu:latest

# System upgrade
RUN apt-get -y update && \
    apt-get -y dist-upgrade && \
# Install build essential
    apt-get -y install sudo build-essential software-properties-common && \
# Install additional build/helper tools
    apt-get -y install libssl-dev libtool autoconf automake curl git subversion unzip cmake zlib1g-dev pkg-config && \
# Install boost
    apt-get -y install libboost-all-dev && \
# Install cpprest sdk (casablanca)
    apt-get -y install libcpprest-dev  && \
# Install go
    apt-get -y install golang && \
# Install google test
    apt-get -y install libgflags-dev libgtest-dev && \
# Install clang
    apt-get -y install clang libc++-dev && \
# Install additional tools
    apt-get -y install vim tree tmux && \
# Do all builds in one place to delete everithing at the end
    mkdir /.build && cd /.build && \
# Build & install poco
    echo "===== BUILD POCO =====" && \
    git clone -b master https://github.com/pocoproject/poco.git && \
    mkdir poco/.build && cd poco/.build && \
    cmake .. -DCMAKE_BUILD_TYPE=Release -DPOCO_STATIC=ON && \
    cmake --build . --target install && \
    cd ../.. && rm -r poco && \
# Build & install protobuf (without tests)
    echo "===== BUILD PROTOBUF =====" && \
    git clone https://github.com/google/protobuf.git && \ 
    mkdir protobuf/.build && cd protobuf/.build && \
    cmake ../cmake -DCMAKE_BUILD_TYPE=Release -Dprotobuf_BUILD_TESTS=OFF -Dprotobuf_BUILD_SHARED_LIBS=OFF && \
    make && make install && \
    cd ../.. && rm -r protobuf && \
# Cleanup
    echo "===== CLEANUP =====" && \
    cd / && rm -r /.build && \
    apt-get -y clean && \
    rm -rf /var/lib/apt/lists/* && \
# Refresh shared library cache
    ldconfig
    
