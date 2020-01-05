FROM centos:7

RUN yum update -y
RUN yum group install "Development Tools" -y
RUN yum install -y \
    zlib-devel \
    bzip2-devel \
    openssl-devel \
    ncurses-devel \
    sqlite-devel \
    readline-devel \
    tk-devel \
    gdbm-devel \
    db4-devel \
    libpcap-devel \
    xz-devel \
    expat-devel \
    wget \
    yum-utils
RUN yum-builddep python -y
