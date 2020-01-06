FROM python:3.6-stretch

ENV HTTP https://confluence.ecmwf.int/download/attachments/45757960

ENV ECCODES eccodes-2.9.2-Source

RUN apt-get update && apt-get install -y \
  gfortran \
  cmake \
  && rm -rf /var/lib/apt/lists/* \
  && pip install numpy pyproj

RUN cd /tmp && wget --output-document=$ECCODES.tar.gz $HTTP/$ECCODES.tar.gz?api=v2 \
    && tar -xzf $ECCODES.tar.gz \
    && mkdir -p /tmp/$ECCODES/build \
    && cd /tmp/$ECCODES/build \
    && cmake \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DCMAKE_BUILD_TYPE=production \
        -DENABLE_PYTHON=1 -DENABLE_MEMFS=1 \
        -DENABLE_ECCODES_THREADS=1 .. \
    && make -j2 \
    && make install \
    && cd / \
    && rm -rf /tmp/$ECCODES*

RUN pip install pygrib