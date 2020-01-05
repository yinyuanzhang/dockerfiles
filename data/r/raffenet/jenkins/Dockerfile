FROM i386/centos:7
LABEL maintainer="Ken Raffenetti raffenet@mcs.anl.gov"

RUN yum update -y \
    && yum install -y \
    wget \
    tar \
    gzip \
    perl \
    perl-Data-Dumper \
    perl-Thread-Queue \
    help2man \
    which \
    file \
    patch \
    m4 \
    gcc \
    gcc-c++ \
    gcc-gfortran \
    clang \
    git \
    make \
    zsh \
    numactl-devel \
    gdb \
    perf \
    strace \
    emacs-nox \
    && yum clean all

RUN cd /tmp && wget http://mirror.team-cymru.com/gnu/autoconf/autoconf-2.69.tar.gz && tar xfz autoconf-2.69.tar.gz && cd autoconf-2.69 && ./configure && make install

RUN cd /tmp && wget http://mirror.team-cymru.com/gnu/automake/automake-1.15.tar.gz && tar xfz automake-1.15.tar.gz && cd automake-1.15 && ./configure && make install

RUN cd /tmp && wget http://mirror.team-cymru.com/gnu/libtool/libtool-2.4.6.tar.gz && tar xfz libtool-2.4.6.tar.gz && cd libtool-2.4.6 && ./configure && make install
