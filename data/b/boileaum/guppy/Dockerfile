From nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04

LABEL maintainer="Matthieu Boileau <matthieu.boileau@math.unistra.fr>"

RUN apt update && apt dist-upgrade -y && \
    apt install -y \
    libcurl4-openssl-dev \
    libssl-dev \
    libhdf5-cpp-11 \
    libzmq5 \
    libboost-system1.58.0 \
    libboost-atomic1.58.0 \
    libboost-chrono1.58.0 \
    libboost-date-time1.58.0 \
    libboost-filesystem1.58.0 \
    libboost-program-options1.58.0 \
    libboost-regex1.58.0 \
    libboost-log1.58.0 \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/

WORKDIR /tmp
ADD https://mirror.oxfordnanoportal.com/software/analysis/ont_guppy_2.2.2-1~xenial_amd64.deb .
RUN dpkg -i --ignore-depends=nvidia-384,libcuda1-384 ont_guppy_2.2.2-1~xenial_amd64.deb

RUN useradd -m -s /bin/bash guppy
ENV HOME /home/guppy
RUN chown -R guppy:guppy $HOME
USER guppy
WORKDIR  $HOME

CMD /bin/bash


