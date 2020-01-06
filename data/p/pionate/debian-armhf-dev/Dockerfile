# Copyright (C) 2017  Christian Berger
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

FROM registry.hub.docker.com/seresearch/debian-armhf:latest
MAINTAINER Christian Berger "christian.berger@gu.se"

# Set the env variable DEBIAN_FRONTEND to noninteractive
ENV DEBIAN_FRONTEND noninteractive

ADD ./01_nodoc /etc/dpkg/dpkg.cfg.d/01_nodoc
ADD ./02_nolocales /etc/dpkg/dpkg.cfg.d/02_nolocales

# These files provided by https://github.com/resin-io/qemu/releases/tag/v2.9.0%2Bresin1
# and https://github.com/resin-io-projects/armv7hf-debian-qemu to enable running
# ARM binaries on a non-binfmt_misc environment; cf.
# https://resin.io/blog/building-arm-containers-on-any-x86-machine-even-dockerhub/
ADD thirdparty/qemu-arm-static /usr/bin
ADD thirdparty/resin-xbuild /usr/bin
ADD thirdparty/cross-build-start /usr/bin
ADD thirdparty/cross-build-end /usr/bin

RUN [ "cross-build-start" ]

# The following list of libraries was determined from the binaries up to the
# top most layer.
RUN mkdir -p /usr/share/man/man1 && \
    apt-get update -y && \
    apt-get upgrade -y && \
    apt-get dist-upgrade -y && \
    apt-get install -y --no-install-recommends \
    build-essential \
    ccache \
    clang \
    clang-format \
    clang-tidy \
    cmake \
    cppcheck \
    flawfinder \
    iwyu \
    llvm \
    ninja-build \
    pmccabe \
    upx-ucl \
    unzip \
    valgrind \
    vera++ \
    wget && \
    apt-get autoremove && \
    apt-get autoclean && \
    apt-get clean

RUN cd /tmp && \
    wget --no-check-certificate https://github.com/L2Program/FlintPlusPlus/archive/master.zip && \
    unzip master.zip && \
    cd /tmp/FlintPlusPlus-master/flint && \
    make -j2 && cp flint++ /usr/bin && \
    cd /tmp && rm -fr FlintPlusPlus-master master.zip && \
    cd /tmp && wget --no-check-certificate https://github.com/oclint/oclint/releases/download/v0.13/oclint-0.13-x86_64-linux-4.4.0-93-generic.tar.gz && \
    tar xvzf /tmp/oclint-0.13-x86_64-linux-4.4.0-93-generic.tar.gz -C /usr/local && rm -f /tmp/oclint-0.13-x86_64-linux-4.4.0-93-generic.tar.gz

RUN [ "cross-build-end" ]

