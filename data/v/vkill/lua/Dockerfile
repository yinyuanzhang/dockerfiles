FROM buildpack-deps:jessie


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
  && make linux install \
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


CMD [ "lua" ]
