FROM vkill/protobuf:3.3

###
### Copy from https://github.com/vkill/docker-protobuf/blob/master/3.3/Dockerfile
###

ENV PROTOBUF_VERSION 3.3.0
ENV PROTOBUF_DOWNLOAD_URL https://github.com/google/protobuf/archive/v3.3.0.tar.gz
ENV PROTOBUF_DOWNLOAD_SHA256 94c414775f275d876e5e0e4a276527d155ab2d0da45eed6b7734301c330be36e



###
### Copy from https://github.com/vkill/docker-lua/blob/cpp/5.3/Dockerfile
###

ENV LUA_MAJOR 5.3
ENV LUA_VERSION 5.3.4
ENV LUA_DOWNLOAD_URL https://www.lua.org/ftp/lua-5.3.4.tar.gz
ENV LUA_DOWNLOAD_SHA256 f681aa518233bc407e23acf0f5887c884f17436f000d453b2491a9f11a52400c


RUN set -ex \
  \
  && wget -O lua.tar.gz "${LUA_DOWNLOAD_URL}" \
  && echo "${LUA_DOWNLOAD_SHA256} *lua.tar.gz" | sha256sum -c - \
  \
  && mkdir -p /usr/src/lua \
  && tar -xzf lua.tar.gz -C /usr/src/lua --strip-components=1 \
  && rm lua.tar.gz \
  \
  && cd /usr/src/lua \
  \
  && make linux test MYCFLAGS="-x c++" CC="g++" \
  && make linux install MYCFLAGS="-x c++" CC="g++" \
  \
  && cd / \
  && rm -r /usr/src/lua



ENV LUAROCKS_VERSION 2.4.2
ENV LUAROCKS_DOWNLOAD_URL http://luarocks.github.io/luarocks/releases/luarocks-2.4.2.tar.gz
ENV LUAROCKS_DOWNLOAD_SHA256 0e1ec34583e1b265e0fbafb64c8bd348705ad403fe85967fd05d3a659f74d2e5


RUN set -ex \
  \
  && runDeps=' \
    unzip \
  ' \
  && apt-get update \
  && apt-get install -y --no-install-recommends $runDeps \
  && rm -rf /var/lib/apt/lists/* \
  \
  && wget -O luarocks.tar.gz "${LUAROCKS_DOWNLOAD_URL}" \
  && echo "${LUAROCKS_DOWNLOAD_SHA256} *luarocks.tar.gz" | sha256sum -c - \
  \
  && mkdir -p /usr/src/luarocks \
  && tar -xzf luarocks.tar.gz -C /usr/src/luarocks --strip-components=1 \
  && rm luarocks.tar.gz \
  \
  && cd /usr/src/luarocks \
  \
  && ./configure --lua-version=${LUA_MAJOR} --with-lua=/usr/local \
  && make build \
  && make install \
  \
  && cd / \
  && rm -r /usr/src/luarocks


###
###
###

ENV LUAINTF_DOWNLOAD_URL https://github.com/SteveKChiu/lua-intf/archive/master.tar.gz
ENV LUAPBINTF_DOWNLOAD_URL https://github.com/jinq0123/LuaPbIntf/archive/master.tar.gz

RUN set -ex \
  \
  && wget -O luapbintf.tar.gz "${LUAPBINTF_DOWNLOAD_URL}" \
  \
  && mkdir -p /usr/src/luapbintf \
  && tar -xzf luapbintf.tar.gz -C /usr/src/luapbintf --strip-components=1 \
  && rm luapbintf.tar.gz \
  \
  && cd /usr/src/luapbintf \
  \
  \
  && mkdir -p /usr/src/luapbintf/third_party/lua \
  && wget -O lua.tar.gz "${LUA_DOWNLOAD_URL}" \
  && echo "${LUA_DOWNLOAD_SHA256} *lua.tar.gz" | sha256sum -c - \
  && tar -xzf lua.tar.gz -C /usr/src/luapbintf/third_party/lua --strip-components=1 \
  && rm lua.tar.gz \
  \
  \
  && mkdir -p /usr/src/luapbintf/third_party/protobuf \
  && wget -O protobuf.tar.gz "${PROTOBUF_DOWNLOAD_URL}" \
  && echo "${PROTOBUF_DOWNLOAD_SHA256} *protobuf.tar.gz" | sha256sum -c - \
  && tar -xzf protobuf.tar.gz -C /usr/src/luapbintf/third_party/protobuf --strip-components=1 \
  && rm protobuf.tar.gz \
  \
  \
  && mkdir -p /usr/src/luapbintf/third_party/lua-intf \
  && wget -O luaintf.tar.gz "${LUAINTF_DOWNLOAD_URL}" \
  && tar -xzf luaintf.tar.gz -C /usr/src/luapbintf/third_party/lua-intf --strip-components=1 \
  && rm luaintf.tar.gz \
  \
  \
  && cd /usr/src/luapbintf/build \
  && sed -i 's!TARGETDIR = bin/Release!TARGETDIR = /usr/local/lib/lua/${LUA_MAJOR}!' LuaPbIntf.make \
  && make config=release \
  && lua -l luapbintf \
  \
  && cd / \
  && rm -r /usr/src/luapbintf



CMD [ "lua", "-l", "luapbintf" ]
