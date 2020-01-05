FROM centos:centos7

RUN yum install -y epel-release; yum clean all
RUN yum install -y  git which zeromq \
libevent-devel boost-devel libdb4-cxx-devel \
autoconf make automake libtool \
gcc-c++ openssl-devel
RUN yum clean all

RUN git clone https://github.com/RavenProject/Ravencoin.git
RUN cd Ravencoin && \
./autogen.sh && \
./configure --without-gui --without-miniupnpc --disable-tests CXXFLAGS="-fPIC" CFLAGS="-fPIC" --enable-cxx && \
make && \
make install
RUN rm -rf Ravencoin

ENV RAVENCOIN_DATA=/root/.raven

EXPOSE 8766-8767

CMD ravend 