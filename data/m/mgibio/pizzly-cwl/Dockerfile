FROM ubuntu:14.04
#based on https://github.com/chrisamiller/docker-pizzly/blob/master/Dockerfile

# install dependencies first
RUN apt-get update  && apt-get install -y \
		build-essential \
		software-properties-common \
		seqan-dev \
		git \
		zlib1g-dev \
		apt-utils \
		libpthread-stubs0-dev \
		wget

# Add repository to get proper G++ version
RUN add-apt-repository ppa:ubuntu-toolchain-r/test
RUN apt-get update && apt-get install -y \
        g++-5 \
        gcc-5

# Link over g++ and gcc
RUN ln -f -s /usr/bin/g++-5 /usr/bin/g++
RUN ln -f -s /usr/bin/gcc-5 /usr/bin/gcc

# Install cmake 3.9.1
WORKDIR /tmp
RUN wget https://cmake.org/files/v3.9/cmake-3.9.1.tar.gz
RUN tar -xzvf cmake-3.9.1.tar.gz
WORKDIR /tmp/cmake-3.9.1
RUN ./bootstrap
RUN make -j4
RUN make install

# install pizzly from source
WORKDIR /
RUN git clone https://github.com/pmelsted/pizzly
WORKDIR /pizzly
RUN git checkout 96368ca642ed72297ac31e99d0fd77227dd23419
RUN mkdir build
WORKDIR /pizzly/build
RUN cmake .. && make

# Copy to /usr/local/bin because there's no make install rule
RUN cp pizzly /usr/local/bin

# needed for MGI data mounts
RUN apt-get update && apt-get install -y libnss-sss && apt-get clean all

#set timezone to CDT
#LSF: Java bug that need to change the /etc/timezone.
#/etc/localtime is not enough.
RUN ln -sf /usr/share/zoneinfo/America/Chicago /etc/localtime && \
    echo "America/Chicago" > /etc/timezone && \
    dpkg-reconfigure --frontend noninteractive tzdata

#UUID is needed to be set for some applications
RUN apt-get update && apt-get install -y dbus && apt-get clean all
RUN dbus-uuidgen >/etc/machine-id
