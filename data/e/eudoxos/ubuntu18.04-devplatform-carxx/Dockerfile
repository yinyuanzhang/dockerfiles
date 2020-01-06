FROM ubuntu:18.04
# install everything that is packaged
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends eatmydata software-properties-common && add-apt-repository ppa:eudoxos/bionic-backports && apt-get update
RUN eatmydata apt-get install -y --no-install-recommends build-essential libhdf5-serial-dev libopencv-dev libboost-system-dev  git cmake ninja-build libeigen3-dev libaravis-dev libsystemd-dev libboost-filesystem-dev libglib2.0-dev libxml2-dev qt5-default mpi-default-dev gir1.2-aravis python3-gi aravis-tools iproute2 sudo ipython3 iputils-ping vim mc gdb
# setup environment
# ENV LD_LIBRARY_PATH /usr/local/lib:/usr/local/lib/x86_64-linux-gnu/:${LD_LIBRARY_PATH}
RUN useradd -ms /bin/bash carxx
WORKDIR /home/carxx
# necessary, when running the binary directly (without shell), it does not get defined
ENV HOME /home/carxx
WORKDIR /tmp/carxx
# only set this later so that we stay more flexible with root by default
# USER carxx

