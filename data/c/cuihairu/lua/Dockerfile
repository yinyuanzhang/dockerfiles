FROM cuihairu/centos:7-gcc

LABEL author="cuihairu <chuihairu@gmail.com>"

ENV LUA_VERSION 5.3.5

ADD lua-${LUA_VERSION}.tar.gz /data/

RUN yum install -y \
    make \
    gcc \
    gcc-devel \
    openssl-devel \
    readline-devel \
    && yum clean all \
    && cd /data/lua-${LUA_VERSION} \
    && make linux test\
    && make install  \
    && cd /data/ \
    && rm -rf /data/lua-${LUA_VERSION}

CMD ["lua","-i"]
