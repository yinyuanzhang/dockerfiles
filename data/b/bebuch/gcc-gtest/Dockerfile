FROM gcc:latest

MAINTAINER Benjamin Buch <https://github.com/bebuch-docker>


# install dependencies
RUN apt-get update \
	&& apt-get upgrade -y \
	&& apt-get install -y git cmake \
	&& apt-get clean \
	&& cd /opt \
	&& git clone https://github.com/google/googletest.git \
	&& cd googletest \
	&& cmake -DCMAKE_INSTALL_PREFIX=/usr/local . \
	&& make -j 2 \
	&& make install \
	&& cd / \
	&& rm -r /opt/googletest
