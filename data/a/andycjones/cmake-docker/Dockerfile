FROM ubuntu:17.10

RUN apt-get update && apt-get install -y --no-install-recommends \
software-properties-common \
build-essential \
libboost-all-dev \
libtcmalloc-minimal4 \
cmake \
git \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/* \
&& ln -s /usr/lib/libtcmalloc_minimal.so.4 /usr/lib/libtcmalloc_minimal.so
