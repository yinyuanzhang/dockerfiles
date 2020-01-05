FROM ubuntu:14.04
MAINTAINER Edgar Y. Walker <edgar.walker@gmail.com>

RUN apt-get update \
    && apt-get install -y curl vim build-essential libreadline-dev

RUN mkdir /src
WORKDIR /src

# Download and install Lua
RUN curl -RL -O http://www.lua.org/ftp/lua-5.3.2.tar.gz \
    && tar zxf lua-5.3.2.tar.gz \
    && cd lua-5.3.2 \
    && make linux test \
    && make install \
    && cd ..; rm -rf ./lua-5.3.2; rm lua-5.3.2.tar.gz

# Download and install LuaRocks
RUN curl -RL -O https://github.com/keplerproject/luarocks/archive/v2.3.0.tar.gz \
    && tar zxf v2.3.0.tar.gz \
    && cd luarocks-2.3.0 \
    && ./configure \
    && make build \
    && make install \
    && cd ..; rm -rf luarocks-2.3.0; rm v2.3.0.tar.gz

