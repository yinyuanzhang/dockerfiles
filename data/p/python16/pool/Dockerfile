FROM ubuntu:16.04
#to use ubuntu aliyun mirror
#docker build . --build-arg mirrors=1
ARG mirrors

RUN mkdir -p /work/pool
VOLUME /work/pool

ADD mirrors.sources.list /etc/apt/mirrors.sources.list
RUN test -z "$mirrors" || cp /etc/apt/mirrors.sources.list /etc/apt/sources.list && :

RUN apt-get -yq update && \
    apt-get install -y build-essential autotools-dev libtool autoconf automake pkg-config cmake \
                   openssl libssl-dev libcurl4-openssl-dev libconfig++-dev \
                   libboost-all-dev libgmp-dev libmysqlclient-dev libzookeeper-mt-dev \
                   libzmq3-dev libgoogle-glog-dev libevent-dev
RUN apt-get install -y wget
RUN apt-get install -y zlib1g zlib1g-dev && \
    mkdir -p /root/source && cd /root/source && \
    wget https://github.com/edenhill/librdkafka/archive/0.9.1.tar.gz && \
    tar zxvf 0.9.1.tar.gz && \
    cd librdkafka-0.9.1 && \
    ./configure && make && make install

RUN mkdir -p /root/source && cd /root/source && \
    wget https://github.com/google/glog/archive/v0.3.4.tar.gz && \
    tar zxvf v0.3.4.tar.gz && \
    cd glog-0.3.4 && \
    ./configure && make && make install

