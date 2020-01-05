FROM centos:7


# User and workdir settings:

USER root
WORKDIR /root
CMD /bin/bash


# Install yum/RPM packages:

RUN true \
    && yum groupinstall -y "Development Tools" \
    && yum install -y \
        wget curl \
        cmake \
        p7zip pbzip2 \
        nano vim \
        git git-gui gitk \
        numactl \
    && dbus-uuidgen > /etc/machine-id


# Install CERN ROOT:

ENV \
    PATH="/opt/root/bin:$PATH" \
    LD_LIBRARY_PATH="/opt/root/lib:$LD_LIBRARY_PATH" \
    MANPATH="/opt/root/man:$MANPATH" \
    PYTHONPATH="/opt/root/lib:$PYTHONPATH" \
    CMAKE_PREFIX_PATH="/opt/root;$CMAKE_PREFIX_PATH" \
    \
    ROOTSYS="/opt/root"

RUN true \
    && yum install -y \
        libSM-devel \
        libX11-devel libXext-devel libXft-devel libXpm-devel \
        libjpeg-devel libpng-devel \
        mesa-libGLU-devel \
    && mkdir -p "/opt/root" \
    && curl -L "https://root.cern.ch/download/root_v5.34.36.Linux-centos7-x86_64-gcc4.8.tar.gz" \
        | tar --strip-components=1 -x -z -f - -C "/opt/root"


# Install BAT dist/distcheck dependencies:

RUN true \
    && yum install -y texlive-collection-latexrecommended


# Yum clean up:

RUN yum clean all
