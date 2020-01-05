FROM ubuntu:xenial

RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        cmake \
        curl \
        davix-dev \
        dcap-dev \
        fonts-freefont-ttf \
        g++ \
        gcc \
        gfal2 \
        gfortran \
        git \
        libafterimage-dev \
        libavahi-compat-libdnssd-dev \
        libcfitsio-dev \
        libfftw3-dev \
        libfreetype6-dev \
        libfreetype6-dev \
        libftgl-dev \
        libgfal2-dev \
        libgif-dev \
        libgl2ps-dev \
        libglew-dev \
        libglu-dev \
        libgraphviz-dev \
        libgsl-dev \
        libjemalloc-dev \
        libjpeg-dev \
        libkrb5-dev \
        libldap2-dev \
        liblz4-dev \
        liblzma-dev \
        libmysqlclient-dev \
        libpcre++-dev \
        libpng12-dev \
        libpng-dev \
        libpq-dev \
        libpythia8-dev \
        libqt4-dev \
        libreadline-dev \
        libsqlite3-dev \
        libssl-dev \
        libtbb-dev \
        libtiff-dev \
        libx11-dev \
        libxext-dev \
        libxft-dev \
        libxml2-dev \
        libxpm-dev \
        libz-dev \
        libzmq3-dev \
        locales \
        lsb-release \
        make \
        module-init-tools \
        openjdk-8-jdk \
        pkg-config \
        python \
        python3 \
        python3-pip \
        python3-tk \
        python-dev \
        python-numpy \
        python-pip \
        r-base \
        r-cran-rcpp \
        r-cran-rinside \
        rsync \
        srm-ifce-dev \
        unixodbc-dev \
        unzip \
        vim \
        wget \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# use CA certs from CVMFS
RUN mkdir -p /etc/grid-security && \
    ln -f -s /cvmfs/oasis.opensciencegrid.org/mis/certificates /etc/grid-security/certificates

# root
RUN cd /tmp && \
    git clone https://github.com/root-project/root /usr/src/root && \
    cd /usr/src/root && \
    git checkout v6-12-06 && \ 
    mkdir /tmp/build && \
    cd /tmp/build && \
    cmake /usr/src/root \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -Dall=ON \
        -Dcxx14=ON \
        -Dfail-on-missing=ON \
        -Dgnuinstall=ON \
        -Drpath=ON \
        -Dbuiltin_afterimage=OFF \
        -Dbuiltin_ftgl=OFF \
        -Dbuiltin_gl2ps=OFF \
        -Dbuiltin_glew=OFF \
        -Dbuiltin_unuran=ON \
        -Dbuiltin_vc=ON \
        -Dbuiltin_vdt=ON \
        -Dbuiltin_veccore=ON \
        -Dbuiltin_xrootd=ON \
        -Darrow=OFF \
        -Dcastor=OFF \
        -Dchirp=OFF \
        -Dgeocad=OFF \
        -Dglite=OFF \
        -Dhdfs=OFF \
        -Dmonalisa=OFF \
        -Doracle=OFF \
        -Dpythia6=OFF \
        -Drfio=OFF \
        -Dsapdb=OFF \
        -Dsrp=OFF \
        && \
    cmake --build . -- -j4 && \
    cmake --build . --target install && \
    cd /tmp && \
    rm -rf /tmp/buil /usr/src/root

# root
RUN cd /tmp && \
    wget -nv http://xrootd.org/download/v4.7.1/xrootd-4.7.1.tar.gz && \
    tar xzf xrootd-4.7.1.tar.gz && \
    cd xrootd-4.7.1 && \
    mkdir build && \
    cd  build && \
    cmake /tmp/xrootd-4.7.1 -DCMAKE_INSTALL_PREFIX=/usr -DENABLE_PERL=FALSE && \
    make && \
    make install && \
    cd /tmp && \
    rm -rf xrootd-4.7.1.tar.gz xrootd-4.7.1

# stashcp
RUN pip install --upgrade pip==9.0.3 && \
    pip install setuptools && \
    pip install stashcp && \
    cp /usr/local/caches.json /usr/local/lib/python2.7/dist-packages/caches.json

# required directories
RUN for MNTPOINT in \
        /cvmfs \
        /hadoop \
        /hdfs \
        /lizard \
        /mnt/hadoop \
        /mnt/hdfs \
        /xenon \
        /spt \
        /stash2 \
    ; do \
        mkdir -p $MNTPOINT ; \
    done

# make sure we have a way to bind host provided libraries
# see https://github.com/singularityware/singularity/issues/611
RUN mkdir -p /host-libs /etc/OpenCL/vendors

# some extra singularity stuff
COPY .singularity.d /.singularity.d
RUN cd / && \
    ln -s .singularity.d/actions/exec .exec && \
    ln -s .singularity.d/actions/run .run && \
    ln -s .singularity.d/actions/test .shell && \
    ln -s .singularity.d/runscript singularity

# build info
RUN echo "Timestamp:" `date --utc` | tee /image-build-info.txt

