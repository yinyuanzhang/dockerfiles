FROM debian:buster

LABEL name="LALSuite Development - Debian Buster" \
      maintainer="Adam Mercer <adam.mercer@ligo.org>" \
      date="20190621" \
      support="Best Effort"

# ensure non-interactive debian installation
ENV DEBIAN_FRONTEND noninteractive
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

# install available updates
RUN apt-get update && apt-get --assume-yes upgrade

# install apt-utils, apt-transport-https, curl, and dirmngr
RUN apt-get --assume-yes install apt-utils \
      apt-transport-https \
      ca-certificates \
      curl \
      dirmngr

# add upstream git-lfs repository
# FIXME: switch to buster packages when they are available
RUN curl -o script.deb.sh https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh
RUN chmod +x script.deb.sh
RUN os=debian dist=stretch ./script.deb.sh

# install dependencies
RUN apt-get update && apt-get --assume-yes install autoconf \
      automake \
      bc \
      build-essential \
      ccache \
      cmake \
      doxygen \
      git \
      git-lfs \
      help2man \
      libboost-dev \
      libboost-program-options-dev \
      libcfitsio-dev \
      libchealpix-dev \
      libfftw3-dev \
      libglib2.0-dev \
      libgsl0-dev \
      libhdf5-dev \
      liboctave-dev \
      libopenmpi-dev \
      libssl-dev \
      libtool \
      libxml2-dev \
      pkg-config \
      python-dev \
      python-h5py \
      python-numpy \
      python-openssl \
      python-pytest \
      python-scipy \
      python-setuptools \
      python-shapely \
      python-six \
      python3-dev \
      python3-numpy \
      swig3.0 \
      texlive \
      wget

# git-lfs post-install
RUN git lfs install

# clear package cache
RUN rm -rf /var/lib/apt/lists/*

# library versions
ENV SOURCE=http://software.ligo.org/lscsoft/source \
    GLUE_VERSION=2.0.0 \
    SEGMENTS_VERSION=1.2.0 \
    LIGO_LW_VERSION=1.5.3 \
    LDAS_TOOLS_CMAKE_VERSION=1.0.7 \
    LDAS_TOOLS_AL_VERSION=2.6.2 \
    LDAS_TOOLS_AL_SWIG_VERSION=2.6.6 \
    LDAS_TOOLS_FRAMECPP_VERSION=2.6.5 \
    LDAS_TOOLS_FRAMECPP_SWIG_VERSION=2.6.8 \
    LIBFRAME_VERSION=8.30 \
    METAIO_VERSION=8.5.1

# get source of unpackaged libraries
RUN mkdir -p ~/src && \
      cd ~/src && \
      wget ${SOURCE}/lscsoft-glue-${GLUE_VERSION}.tar.gz && \
      wget ${SOURCE}/ligo-segments-${SEGMENTS_VERSION}.tar.gz && \
      wget ${SOURCE}/python-ligo-lw-${LIGO_LW_VERSION}.tar.gz && \
      wget ${SOURCE}/ldas-tools-cmake-${LDAS_TOOLS_CMAKE_VERSION}.tar.gz && \
      wget ${SOURCE}/ldas-tools-al-${LDAS_TOOLS_AL_VERSION}.tar.gz && \
      wget ${SOURCE}/ldas-tools-al-swig-${LDAS_TOOLS_AL_SWIG_VERSION}.tar.gz && \
      wget ${SOURCE}/ldas-tools-framecpp-${LDAS_TOOLS_FRAMECPP_VERSION}.tar.gz && \
      wget ${SOURCE}/ldas-tools-framecpp-swig-${LDAS_TOOLS_FRAMECPP_SWIG_VERSION}.tar.gz && \
      wget ${SOURCE}/libframe-${LIBFRAME_VERSION}.tar.gz && \
      wget ${SOURCE}/metaio-${METAIO_VERSION}.tar.gz || exit

# glue
RUN cd ~/src && \
      tar xf lscsoft-glue-${GLUE_VERSION}.tar.gz && \
      cd lscsoft-glue-${GLUE_VERSION} && \
      python ./setup.py install --prefix=/usr/local && \
      cd ~/src && \
      rm -rf lscsoft-glue-${GLUE_VERSION} || exit

# ligo-segments
RUN cd ~/src && \
      tar xf ligo-segments-${SEGMENTS_VERSION}.tar.gz && \
      cd ligo-segments-${SEGMENTS_VERSION} && \
      python ./setup.py install --prefix=/usr/local && \
      cd ~/src && \
      rm -rf ligo-segments-${SEGMENTS_VERSION} || exit

# ligo-lw
RUN cd ~/src && \
      tar xf python-ligo-lw-${LIGO_LW_VERSION}.tar.gz && \
      cd python-ligo-lw-${LIGO_LW_VERSION} && \
      python ./setup.py install --prefix=/usr/local && \
      cd ~/src && \
      rm -rf python-ligo-lw-${SEGMENTS_VERSION} || exit

# ldas-tools-cmake
RUN cd ~/src && \
      tar xf ldas-tools-cmake-${LDAS_TOOLS_CMAKE_VERSION}.tar.gz && \
      mkdir build && cd build && \
      cmake ../ldas-tools-cmake-${LDAS_TOOLS_CMAKE_VERSION} && \
      cmake --build . --target install && \
      make install && \
      cd ~/src && \
      rm -rf build ldas-tools-cmake-${LDAS_TOOLS_CMAKE_VERSION} || exit

# ldas-tools-al
RUN cd ~/src && \
      tar xf ldas-tools-al-${LDAS_TOOLS_AL_VERSION}.tar.gz && \
      cd ldas-tools-al-${LDAS_TOOLS_AL_VERSION} && \
      ./configure --prefix=/usr/local \
          --disable-warnings-as-errors \
          --without-doxygen \
          --without-dot \
          --disable-latex && \
      make && \
      make install && \
      cd ~/src && \
      rm -rf ldas-tools-al-${LDAS_TOOLS_AL_VERSION} && \
      ldconfig || exit

# ldas-tools-al-swig
RUN cd ~/src && \
      tar xf ldas-tools-al-swig-${LDAS_TOOLS_AL_SWIG_VERSION}.tar.gz && \
      mkdir build && cd build && \
      cmake ../ldas-tools-al-swig-${LDAS_TOOLS_AL_SWIG_VERSION} && \
      cmake --build . --target install && \
      make install && \
      cd ~/src && \
      rm -rf build ldas-tools-al-swig-${LDAS_TOOLS_AL_SWIG_VERSION} || exit

# ldas-tools-framecpp
RUN cd ~/src && \
      tar xf ldas-tools-framecpp-${LDAS_TOOLS_FRAMECPP_VERSION}.tar.gz && \
      cd ldas-tools-framecpp-${LDAS_TOOLS_FRAMECPP_VERSION} && \
      ./configure --prefix=/usr/local \
          --disable-warnings-as-errors \
          --without-doxygen \
          --without-dot \
          --disable-latex && \
      make && \
      make install && \
      cd ~/src && \
      rm -rf ldas-tools-framecpp-${LDAS_TOOLS_FRAMECPP_VERSION} && \
      ldconfig || exit

# ldas-tools-framecpp-swig
RUN cd ~/src && \
      tar xf ldas-tools-framecpp-swig-${LDAS_TOOLS_FRAMECPP_SWIG_VERSION}.tar.gz && \
      mkdir build && cd build && \
      cmake ../ldas-tools-framecpp-swig-${LDAS_TOOLS_FRAMECPP_SWIG_VERSION} && \
      cmake --build . --target install && \
      make install && \
      cd ~/src && \
      rm -rf build ldas-tools-framecpp-swig-${LDAS_TOOLS_FRAMECPP_SWIG_VERSION} || exit

# libframe
RUN cd ~/src && \
      tar xf libframe-${LIBFRAME_VERSION}.tar.gz && \
      cd libframe-${LIBFRAME_VERSION} && \
      ./configure --prefix=/usr/local && \
      make && \
      make install && \
      cd ~/src && \
      rm -rf libframe-${LIBFRAME_VERSION} && \
      ldconfig || exit

# metaio
RUN cd ~/src && \
      tar xf metaio-${METAIO_VERSION}.tar.gz && \
      cd metaio-${METAIO_VERSION} && \
      ./configure --prefix=/usr/local && \
      make && \
      make install && \
      cd ~/src && \
      rm -rf metaio-${METAIO_VERSION} && \
      ldconfig || exit
