#
# NUC972-buildroot Dockerfile
#
# https://github.com/jinhe1314/nuc972-bulidroot
#
FROM ubuntu:14.04
MAINTAINER King Jin <gojinhe@gmail.com>


RUN apt-get update && \
    apt-get install -y \
    build-essential \
    bash \
    bc \
    binutils \
    build-essential \
    bzip2 \
    cpio \
    g++ \
    gcc \
    git \
    gzip \
    libncurses5-dev \
    make \
    mercurial \
    whois \
    patch \
    perl \
    python \
    rsync \
    vim \
    sed \
    tar \
    unzip \
    wget \
    libc6-i386

# Sometimes Buildroot need proper locale, e.g. when using a toolchain
# based on glibc.
RUN locale-gen en_US.utf8

WORKDIR /root
#RUN git clone git://git.buildroot.net/buildroot --depth=1
RUN wget -nv http://buildroot.uclibc.org/downloads/buildroot-2016.05.tar.bz2 && \
  tar xf buildroot-*.tar* &&\
  rm buildroot-*.tar* &&\
  ln -s buildroot-* buildroot
WORKDIR /root/buildroot


RUN wget -nv https://github.com/jinhe1314/nuc972-bulidroot/raw/master/buildroot_config_nuc972_qt4 && \
  cp buildroot_config_nuc972_qt4 .config
RUN touch .config
RUN touch kernel.config
RUN make
VOLUME /root/buildroot

CMD ["/bin/bash"]
