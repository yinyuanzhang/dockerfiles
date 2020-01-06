FROM ubuntu:19.04

##### NOTE: We want to use MPICH, since it is the "native" supported MPI library for most clusters
##### (on Cray clusters they usually replace the mpich library with their own in the docker/shifter container)
##### Because of this, we need to compile some packages ourselves, even though they come with ubuntu
##### (but only with openmpi support)
ENV INSTALL_PREFIX /usr/local


ENV PNETCDF_VERSION 1.11.2
ENV NETCDF_VERSION 4.7.0

ENV HDF5_VERSION 1.10.5
ENV ALSVINN_PYTHON_VERSION 3.7



RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get install --yes build-essential \
    	cmake python3 python3-matplotlib python3-numpy python3-scipy git \
	gcc g++ libgtest-dev libboost-all-dev doxygen graphviz \
		python3-pip  \
	wget m4 libcurl4-openssl-dev \
	texlive-full
COPY requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt

#### MPICH
RUN cd $HOME;\
    export PERL_USE_UNSAFE_INC=1 &&\
    wget https://github.com/pmodels/mpich/archive/v3.1.4.tar.gz&&\
    DEBIAN_FRONTEND=noninteractive apt-get install -y libtool autoconf&&\
    tar xf v3.1.4.tar.gz&&\
    cd mpich-3.1.4&&\
    ./autogen.sh&&\
    ./configure --prefix=$INSTALL_PREFIX --disable-fortran&&\
    make install

#### HDF5
RUN cd $HOME&&\
    export CC=${INSTALL_PREFIX}/bin/mpicc&&\
    wget -O hdf5.tar.bz2 "https://www.hdfgroup.org/package/hdf5-${HDF5_VERSION}-tar-bz2/?wpdmdl=13570&refresh=5c90e67332c151553000051" &&\
    tar xf hdf5.tar.bz2&&\
    cd hdf5-${HDF5_VERSION} &&\
    ./configure --prefix=$INSTALL_PREFIX --enable-mpi --enable-parallel --disable-cpp-lib&&\
    make install&&\
    rm -rf hdf5*

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
    tar xf pnetcdf-${PNETCDF_VERSION}.tar.gz &&\
    cd pnetcdf-${PNETCDF_VERSION} &&\
    export CFLAGS='-fPIC -O2' &&\
    ./configure --prefix=$INSTALL_PREFIX &&\
    make install &&\
    cd $HOME &&\
    rm -rf pnetcdf*
