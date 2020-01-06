FROM nvidia/cuda:9.2-devel-ubuntu16.04

##### NOTE: We want to use MPICH, since it is the "native" supported MPI library for most clusters
##### (on Cray clusters they usually replace the mpich library with their own in the docker/shifter container)
##### Because of this, we need to compile some packages ourselves, even though they come with ubuntu
##### (but only with openmpi support)
ENV INSTALL_PREFIX /usr/local

ENV ALSVINN_PYTHON_VERSION 3.7

ENV PNETCDF_VERSION 1.11.2
ENV NETCDF_VERSION 4.7.0
ENV GTEST_VERSION 1.8.0

ENV BOOST_MAJOR_VERSION 1
ENV BOOST_MINOR_VERSION 70
ENV BOOST_RELEASE_VERSION 0

ENV HDF5_VERSION 1.10.5

ENV CMAKE_MAJOR_VERSION 3
ENV CMAKE_MINOR_VERSION 14
ENV CMAKE_RELEASE_VERSION 0
ENV GCC_VERSION 7
ENV CC gcc-${GCC_VERSION}
ENV CXX g++-${GCC_VERSION}

RUN apt-get update &&\
    DEBIAN_FRONTEND=noninteractive apt-get install -y build-essential software-properties-common texlive-full &&\    
    add-apt-repository ppa:ubuntu-toolchain-r/test -y &&\
    apt-get update &&\
    DEBIAN_FRONTEND=noninteractive apt-get install -y gcc-snapshot &&\
    apt-get update &&\
    DEBIAN_FRONTEND=noninteractive apt-get install -y gcc-${GCC_VERSION} g++-${GCC_VERSION} &&\
    update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-${GCC_VERSION} ${GCC_VERSION}0 --slave /usr/bin/g++ g++ /usr/bin/g++-${GCC_VERSION} 
    
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y git \
    build-essential\
    wget\
    doxygen\
    libomp-dev\
    m4\
    unzip\
    cuda-compiler-9-1\
    libcurl4-openssl-dev \
    zlib1g-dev\
    software-properties-common\
    curl

####### Python
# Python 3.7
COPY requirements.txt /requirements.txt
RUN add-apt-repository -y ppa:deadsnakes/ppa && \
      apt-get update -qq &&\
      apt-get install -y python3.7 python3.7-dev && \
      curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
      python3.7 get-pip.py && \
      pip3.7 install -r requirements.txt


#### MPICH
RUN cd $HOME;\
    wget https://github.com/pmodels/mpich/archive/v3.1.4.tar.gz&&\
    DEBIAN_FRONTEND=noninteractive apt-get install -y libtool autoconf&&\
    tar xf v3.1.4.tar.gz > /dev/null &&\
    cd mpich-3.1.4&&\
    ./autogen.sh&&\
    ./configure --prefix=$INSTALL_PREFIX --disable-fortran&&\
    make install

#### HDF5
RUN cd $HOME&&\
    export CC=${INSTALL_PREFIX}/bin/mpicc&&\
    wget -O hdf5.tar.bz2 "https://www.hdfgroup.org/package/hdf5-${HDF5_VERSION}-tar-bz2/?wpdmdl=13570&refresh=5c90e67332c151553000051" &&\
    tar xf hdf5.tar.bz2 > /dev/null &&\
    cd hdf5-${HDF5_VERSION} &&\
    ./configure --prefix=$INSTALL_PREFIX --enable-mpi --enable-parallel --disable-cpp-lib&&\
    make install&&\
    rm -rf hdf5*

##### CMAKE
RUN cd $HOME &&\
    wget https://cmake.org/files/v${CMAKE_MAJOR_VERSION}.${CMAKE_MINOR_VERSION}/cmake-${CMAKE_MAJOR_VERSION}.${CMAKE_MINOR_VERSION}.${CMAKE_RELEASE_VERSION}.tar.gz &&\
    tar xf cmake-${CMAKE_MAJOR_VERSION}.${CMAKE_MINOR_VERSION}.${CMAKE_RELEASE_VERSION}.tar.gz > /dev/null &&\
    cd cmake-${CMAKE_MAJOR_VERSION}.${CMAKE_MINOR_VERSION}.${CMAKE_RELEASE_VERSION} && \
    ./bootstrap --system-curl --prefix=$INSTALL_PREFIX && \
    make && \
    make install && \
    cd $HOME &&\
    rm -rf cmake*


##### NETCDF
RUN cd $HOME && \
    export CC=${INSTALL_PREFIX}/bin/mpicc&&\
    wget https://github.com/Unidata/netcdf-c/archive/v${NETCDF_VERSION}.tar.gz &&\
    tar xf v${NETCDF_VERSION}.tar.gz && \
    cd netcdf-c-${NETCDF_VERSION} &&\
    mkdir build;\
    cd build;\
    cmake .. -DCMAKE_C_COMPILER=`which $CC` -DCMAKE_CXX_COMPILER=`which $CXX` -DHDF5_DIR=/usr/local -DHDF5_INCLUDE_DIR=/usr/local/include -DHDF5_LIBRARY=/usr/local/lib/libhdf5.so -DCMAKE_PREFIX_PATH=/usr/local -DCMAKE_C_FLAGS='-I/usr/local/include' -DCMAKE_INSTALL_PREFIX=$INSTALL_PREFIX && \
    make install &&\
    cd ../.. &&\
    rm -rf netcdf*


##### PNETCDF
RUN cd ~ && \
    wget https://parallel-netcdf.github.io/Release/pnetcdf-${PNETCDF_VERSION}.tar.gz &&\
    export CC=`which mpicc`;\
    tar xf pnetcdf-${PNETCDF_VERSION}.tar.gz > /dev/null &&\
    cd pnetcdf-${PNETCDF_VERSION} &&\
    export CFLAGS='-fPIC -O2' &&\
    ./configure --prefix=$INSTALL_PREFIX &&\
    make install &&\
    cd $HOME &&\
    rm -rf pnetcdf*

##### GTest
RUN cd $HOME &&\
    wget https://github.com/google/googletest/archive/release-${GTEST_VERSION}.zip &&\
    unzip release-${GTEST_VERSION}.zip >/dev/null&&\
    cd googletest-release-${GTEST_VERSION} &&\
    mkdir build &&\
    cd build &&\
    cmake .. -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=$INSTALL_PREFIX -DCMAKE_C_COMPILER=`which $CC` -DCMAKE_CXX_COMPILER=`which $CXX`&&\
    make install &&\
    find . -iname '*.a' -exec cp {} ${INSTALL_PREFIX}/lib/ \; &&\
    cd $HOME &&\
    rm -rf release-${GTEST_VERSION}.zip googletest-release-${GTEST_VERSION}

###### BOOST
RUN cd $HOME &&\
    wget https://dl.bintray.com/boostorg/release/${BOOST_MAJOR_VERSION}.${BOOST_MINOR_VERSION}.${BOOST_RELEASE_VERSION}/source/boost_${BOOST_MAJOR_VERSION}_${BOOST_MINOR_VERSION}_${BOOST_RELEASE_VERSION}.tar.bz2 && \
    tar xf boost_${BOOST_MAJOR_VERSION}_${BOOST_MINOR_VERSION}_${BOOST_RELEASE_VERSION}.tar.bz2 && cd boost_${BOOST_MAJOR_VERSION}_${BOOST_MINOR_VERSION}_${BOOST_RELEASE_VERSION} && \
    ./bootstrap.sh --with-python=`which python3.7` --with-libraries=program_options,filesystem,system,python,regex,thread,chrono,date_time,log --prefix=$INSTALL_PREFIX && \
    ./b2  --toolset=gcc --threading=multi install && \
    cd $HOME && \
    rm -rf boost_*


RUN rm /etc/ld.so.cache && ldconfig
RUN ldconfig
