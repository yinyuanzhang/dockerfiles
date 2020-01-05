# BioCocoa base image
FROM mediabook/biococoa

MAINTAINER Scott Christley <schristley@mac.com>

# compile and install BioSwarm
COPY . /mediabook/bioswarm-src
RUN cd /mediabook/bioswarm-src && make install
RUN /sbin/ldconfig
RUN cd /mediabook/bioswarm-src/Tools && make install
