#构建nirvana的编译环境

FROM ubuntu:trusty
MAINTAINER Jun Tsai - jcai@ganshane.com

#mirror
RUN sed -i 's/archive.ubuntu.com/mirrors.sohu.com/g' /etc/apt/sources.list && \
    apt-get -qq update && \
    apt-get -qqy install gcc g++ cmake make maven openjdk-7-jdk openssh-client git-core swig wget


WORKDIR /build
#Install protobuf
RUN { \
    wget https://github.com/google/protobuf/releases/download/v2.6.1/protobuf-2.6.1.tar.gz -O protobuf-2.6.1.tar.gz \
    && tar xfvz protobuf-2.6.1.tar.gz \
    && cd protobuf-2.6.1 \
    # && ./autogen.sh \
    # && wget http://lichen.egfit.com/nirvana/gz/protobuf-2.5.0.tar.gz \
    # && tar xfvz protobuf-2.5.0.tar.gz \
    # && cd protobuf-2.5.0 \
    && ./configure && make && make install \
    && cd - && rm -rf protobuf* ;\
}
#install snappy
RUN { \
  apt-get install -y automake libtool pkg-config \
  && git clone --depth=1 https://github.com/google/snappy.git \
  && cd snappy && ./autogen.sh && ./configure --enable-shared --enable-static --with-pic \
  && make && make install && cd - \
  && rm -rf snappy && apt-get -y purge automake libtool pkg-config && apt-get -y autoremove ;\
}

#install rocksdb and kernel 
RUN { \
    git clone --depth=1 --branch=rocksdb-3.13.1 https://github.com/facebook/rocksdb.git \
    && cd rocksdb \
    && CXXFLAGS="-fPIC" make static_lib \
    && cp -r include/* /usr/local/include/ && cp librocksdb.a /usr/local/lib/ \
    && cd - && rm -rf rocksdb* \
    && mkdir kernel && cd kernel \
    && wget http://lichen.egfit.com/nirvana/libnirvana-kernel.so -O /usr/local/lib/libnirvana-kernel.so \
    && wget http://lichen.egfit.com/nirvana/kernel-header.tar.gz \
    && tar xfvz kernel-header.tar.gz && mv nirvana /usr/local/include/ \
    && cd - && rm -rf kernel \
    && ldconfig ; \
}

#ssh_config
RUN echo "StrictHostKeyChecking no" >> /etc/ssh/ssh_config
RUN echo "UserKnownHostsFile /dev/null" >> /etc/ssh/ssh_config

#compile shell
ADD compile.sh /compile.sh

#Env
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64


