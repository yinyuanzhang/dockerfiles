FROM ubuntu:16.04
MAINTAINER Pierre Navaro <pierre.navaro@univ-rennes1.fr>

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get -yq dist-upgrade \
 && apt-get install -yq --no-install-recommends sudo apt-utils\
 && apt-get install -yq --no-install-recommends \
     ca-certificates build-essential git cmake g++ gfortran \
     liblapack-dev gmsh libsuitesparse-dev \
     libeigen3-dev libarpack++2-dev wget

ENV XLIFEPP=xlifepp-sources-v2.1-2019-05-10
RUN wget --no-check-certificate \
https://uma.ensta-paristech.fr/soft/XLiFE++/var/files/src/${XLIFEPP}.tbz \
&& tar -jxf ${XLIFEPP}.tbz --transform=s/${XLIFEPP}/xlifepp/ \
&& rm -f ${XLIFEPP}.tbz && cd /xlifepp \
&& mkdir build \
&& cd build/   \
&& cmake .. -DXLIFEPP_ENABLE_ARPACK=ON -DXLIFEPP_ENABLE_EIGEN=ON \
&& make libs 

RUN useradd -ms /bin/bash work
USER work
WORKDIR /home/work

# Configure environment
ENV SHELL=/bin/bash \
    XLIFEPP_DIR=/xlifepp 

ENV PATH=${XLIFEPP_DIR}/bin:$PATH 
