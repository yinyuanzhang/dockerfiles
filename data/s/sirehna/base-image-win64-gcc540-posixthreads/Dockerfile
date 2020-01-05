FROM dockcross/windows-x64-posix:latest

# docker run -it dockcross/windows-x64-posix:latest /bin/bash

RUN mkdir -p /opt
WORKDIR /opt

# BOOST
RUN cd /usr/src/mxe &&  \
    make TARGET=x86_64-w64-mingw32.static.posix boost bzip2_URL=force_mirror.org && \
    rm -rf /usr/src/mxe/pkg/*

# BOOST Geometry extension
RUN git clone https://github.com/boostorg/geometry && \
    cd geometry && \
    git checkout 4aa61e59a72b44fb3c7761066d478479d2dd63a0 && \
    cp -rf include/boost/geometry/extensions /usr/src/mxe/usr/x86_64-w64-mingw32.static.posix/include/boost/geometry/. && \
    cd .. && \
    rm -rf geometry

# Ipopt 3.12.9
# http://www.coin-or.org/Ipopt/documentation/node10.html
# Command 'make test' is disabled : wine has to be used to run tests
RUN wget http://www.coin-or.org/download/source/Ipopt/Ipopt-3.12.9.tgz -O ipopt_src.tgz && \
    mkdir -p /opt/CoinIpopt && \
    mkdir -p ipopt_src && \
    tar -xf ipopt_src.tgz --strip 1 -C ipopt_src && \
    rm -rf ipopt_src.tgz && \
    cd ipopt_src && \
    cd ThirdParty/Blas && \
        ./get.Blas && \
    cd ../Lapack && \
        ./get.Lapack && \
    cd ../Mumps && \
        ./get.Mumps && \
    cd ../../ && \
    mkdir build && \
    cd build && \
    CC=/usr/src/mxe/usr/bin/x86_64-w64-mingw32.static.posix-gcc \
    CXX=/usr/src/mxe/usr/bin/x86_64-w64-mingw32.static.posix-g++ \
    F77=/usr/src/mxe/usr/bin/x86_64-w64-mingw32.static.posix-gfortran \
    ../configure \
        -with-pic \
        --disable-shared \
        --disable-pthread-mumps \
        --prefix=/opt/CoinIpopt \
        --host=x86_64-w64-mingw32 \
        && \
    make && \
    make install && \
    cd .. && \
    cd .. && \
    rm -rf ipopt_src

RUN wget https://github.com/eigenteam/eigen-git-mirror/archive/3.3.5.tar.gz -O eigen.tgz && \
    mkdir -p /opt/eigen && \
    tar -xzf eigen.tgz --strip 1 -C /opt/eigen && \
    rm -rf eigen.tgz

RUN wget https://github.com/jbeder/yaml-cpp/archive/release-0.3.0.tar.gz -O yaml_cpp.tgz && \
    mkdir -p /opt/yaml_cpp && \
    tar -xzf yaml_cpp.tgz --strip 1 -C /opt/yaml_cpp && \
    rm -rf yaml_cpp.tgz

RUN wget https://github.com/google/googletest/archive/release-1.8.0.tar.gz -O googletest.tgz && \
    mkdir -p /opt/googletest && \
    tar -xzf googletest.tgz --strip 1 -C /opt/googletest && \
    rm -rf googletest.tgz

RUN wget https://github.com/zaphoyd/websocketpp/archive/0.7.0.tar.gz -O websocketpp.tgz && \
    mkdir -p /opt/websocketpp && \
    tar -xzf websocketpp.tgz --strip 1 -C /opt/websocketpp && \
    rm -rf websocketpp.tgz

RUN mkdir -p /opt/libf2c && \
    cd /opt/libf2c && \
    wget http://www.netlib.org/f2c/libf2c.zip -O libf2c.zip && \
    unzip libf2c.zip && \
    rm -rf libf2c.zip

RUN wget https://sourceforge.net/projects/geographiclib/files/distrib/archive/GeographicLib-1.30.tar.gz/download -O geographiclib.tgz && \
    mkdir -p /opt/geographiclib && \
    tar -xzf geographiclib.tgz --strip 1 -C /opt/geographiclib && \
    rm -rf geographiclib.tgz

## Manual installation of boost. Require first to install lib bzip2.
## http://www.bzip.org/1.0.6/bzip2-1.0.6.tar.gz
## Moreover mxe seems to patch boost ...
## https://github.com/mxe/mxe/blob/master/src/boost.mk
## https://github.com/mxe/mxe/blob/master/src/boost-1-fixes.patch
##
## BOOST 1.60 with Boost geometry extensions
## SSC : system thread random chrono
## XDYN : program_options filesystem system regex
## libbz2 is required for Boost compilation
## cross-build, see b2 options at:
## https://www.boost.org/build/doc/html/bbv2/overview/invocation.html
## https://github.com/mxe/mxe/blob/master/src/boost.mk
#RUN wget http://sourceforge.net/projects/boost/files/boost/1.60.0/boost_1_60_0.tar.gz -O #boost_src.tar.gz && \
#    mkdir -p boost_src && \
#    tar -xzf boost_src.tar.gz --strip 1 -C boost_src && \
#    rm -rf boost_src.tar.gz && \
#    cd boost_src && \
#    export TARGET=x86_64-w64-mingw32.static.posix && \
#    export PREFIX=/usr/src/mxe/usr && \
#    echo "using gcc : mxe : ${TARGET}-g++ : <rc>${TARGET}-windres <archiver>${TARGET}-ar <ranlib>$#{TARGET}-ranlib ;" > user-config.jam &&  \
#    cat user-config.jam &&  \
#    ./bootstrap.sh && \
#    ./b2 \
#        -a \
#        -q \
#        --ignore-site-config \
#        --user-config=user-config.jam \
#        abi=ms \
#        address-model=64 \
#        architecture=x86 \
#        binary-format=pe \
#        link=static \
#        target-os=windows \
#        threadapi=win32 \
#        threading=single \
#        threading=multi \
#        variant=release \
#        toolset=gcc-mxe \
#        cxxflags=-std=gnu++11 \
#        --layout=tagged \
#        --disable-icu \
#        --without-mpi \
#        --without-python \
#        --prefix=${PREFIX}/${TARGET} \
#        --exec-prefix=${PREFIX}/${TARGET}/bin \
#        --libdir=${PREFIX}/${TARGET}/lib \
#        --includedir=${PREFIX}/${TARGET}/include \
#        -sEXPAT_INCLUDE=${PREFIX}/${TARGET}/include \
#        -sEXPAT_LIBPATH=${PREFIX}/${TARGET}/lib \
#        install && \
#    cd .. && \
#    rm -rf boost_src
