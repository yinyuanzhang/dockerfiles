# Copyright (C) 2019  Christian Berger
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

FROM ubuntu:18.04 as builder
MAINTAINER Christian Berger "christian.berger@gu.se"

# Set the env variable DEBIAN_FRONTEND to noninteractive
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get dist-upgrade -y

RUN apt-get install -y --no-install-recommends \
      software-properties-common

RUN add-apt-repository ppa:chrberger/libcluon && \
    apt-get update && \
    apt-get install -y --no-install-recommends libcluon && \
    apt-get clean

RUN apt-get install -y --no-install-recommends \
      build-essential \
      can-utils \
      gawk \
      python3-pip

RUN pip3 install setuptools
RUN pip3 install wheel
RUN pip3 install cantools

ADD ./generateHeaderOnly.sh /usr/local/bin/
ADD ./generateMappingCodeSnippet.awk /usr/local/bin/

ENV PATH=/usr/local/bin:$PATH

