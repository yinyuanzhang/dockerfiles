FROM flightgear/simgear.build:opensuse-latest AS plibbuild
  
WORKDIR /plib

RUN git clone --depth 1 https://git.code.sf.net/p/libplib/code && \
    mkdir build && cd build && cmake -G "Unix Makefiles" \
                              -D CMAKE_BUILD_TYPE=Release \
                              -D CMAKE_PREFIX_PATH="/usr/local" \
                              -D CMAKE_INSTALL_PREFIX:PATH=/usr/local \
                              -D CMAKE_CXX_FLAGS="-pipe" \
                              ../code \
                        && make && make install
