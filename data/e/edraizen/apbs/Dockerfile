FROM ubuntu:14.04

# install necessary dependencies
RUN apt-get update && \
    apt-get install -y git software-properties-common
RUN add-apt-repository ppa:george-edison55/cmake-3.x
RUN apt-get update
RUN apt-get install -y cmake
RUN apt-get install -y build-essential

RUN mkdir /opt/apbs
WORKDIR /opt/apbs
RUN git clone https://github.com/Electrostatics/apbs-pdb2pqr.git
WORKDIR /opt/apbs/apbs-pdb2pqr
RUN git submodule init
RUN git submodule update
WORKDIR /opt/apbs/apbs-pdb2pqr/apbs
RUN cmake /opt/apbs/apbs-pdb2pqr/apbs -Wno-dev
RUN make

COPY wrapper.sh /opt/apbs

RUN mkdir /data
WORKDIR /data

ENTRYPOINT ["sh", "/opt/apbs/wrapper.sh"]
