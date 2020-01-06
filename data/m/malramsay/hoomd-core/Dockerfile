FROM centos:7

RUN yum install -y epel-release && \
    yum install -y \
    clang \
    gcc-c++ \
    make \
    cmake \
    curl \
    git \
    tar \
    gzip \
    sqlite3-devel \
    mpich-devel \
    python36-devel && \
    yum clean all && \
    rm -rf /var/cache/yum

# Add mpi library to path
# This is the same as running `module load mpi` since the `module` command doesn't work.
ENV PATH="/usr/lib64/mpich/bin:${PATH}"
ENV LD_LIBRARY_PATH="/usr/lib64/mpich/lib"

# These are the arguments for the build phase, change them here.
# By specifying these as arguments it is possible to
ARG HOOMD_VERSION="v2.3.4"
ARG CUDA=off
ARG MPI=on
ARG TBB=off
ARG JIT=off
ARG TEST=off
ARG PYTHON=/usr/bin/python36

RUN curl -sSLO https://glotzerlab.engin.umich.edu/Downloads/hoomd/hoomd-$HOOMD_VERSION.tar.gz && \
    tar -xzf hoomd-$HOOMD_VERSION.tar.gz -C /root && \
    cd /root/hoomd-$HOOMD_VERSION && \
    mkdir build && \
    cd build && \
    cmake ../ \
        -DENABLE_CUDA=$CUDA \
        -DENABLE_MPI=$MPI \
        -DENABLE_TBB=$TBB \
        -DBUILD_JIT=$JIT \
        -DBUILD_TESTING=$TEST \
        -DPYTHON_EXECUTABLE=$PYTHON \
        -DCMAKE_INSTALL_PREFIX=`$PYTHON -c "import site; print(site.getsitepackages()[0])"` && \
    make && \
    make install && \
    rm -rf /root/hoomd-$HOOMD_VERSION && \
    rm /hoomd-$HOOMD_VERSION.tar.gz
