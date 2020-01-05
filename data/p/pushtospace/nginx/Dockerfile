FROM pushtospace/ubuntu
MAINTAINER G.Jongenelen <g.jongenelen@pushto.space>

ENV     OPENRESTY_VERSION   1.13.6.2
ENV     LUAROCKS_VERSION    2.4.4

# Install Deps
RUN apt-get update && apt-get install -y  wget \
                        build-essential \
                        git \
                        libssl-dev \
                        libpcre3 \
                        libpcre3-dev \
                        libreadline-dev \
                        unzip \
                        curl    

# Install OpenResty
RUN     wget https://openresty.org/download/openresty-${OPENRESTY_VERSION}.tar.gz -O openresty-${OPENRESTY_VERSION}.tar.gz && \
        tar xzvf openresty-${OPENRESTY_VERSION}.tar.gz && \
        cd openresty-${OPENRESTY_VERSION} && \
        ./configure \
            --with-http_v2_module \
            --with-http_realip_module && \
        make && \
        make install && \
        cd .. && \
        rm -rf openresty*

# Install LuaRocks + own auto-ssl
RUN     wget https://codeload.github.com/keplerproject/luarocks/tar.gz/v${LUAROCKS_VERSION} -O luarocks-${LUAROCKS_VERSION}.tar.gz && \
        tar xzvf luarocks-${LUAROCKS_VERSION}.tar.gz && cd luarocks-${LUAROCKS_VERSION}/ && \
        ./configure \
            --prefix=/usr/local/openresty/luajit \
            --with-lua=/usr/local/openresty/luajit/ \
            --lua-suffix=jit-2.1.0-beta3 \
            --with-lua-include=/usr/local/openresty/luajit/include/luajit-2.1 && \
        make build && \
        make install && \
        /usr/local/openresty/luajit/bin/luarocks install lua-resty-http && \
        /usr/local/openresty/luajit/bin/luarocks install https://raw.githubusercontent.com/gjongenelen/lua-resty-auto-ssl/master/lua-resty-auto-ssl-git-1.rockspec && \
        cd .. && \
        rm -rf luarocks*

RUN openssl req -new -newkey rsa:2048 -days 3650 -nodes -x509 -subj '/CN=sni-support-required-for-valid-ssl' \
-keyout /etc/ssl/resty-auto-ssl-fallback.key -out /etc/ssl/resty-auto-ssl-fallback.crt

ADD mime.types /etc/nginx/
ADD fastcgi_params /etc/nginx/

ADD ./start.sh /root/
RUN chmod +x /root/start.sh

CMD ["/root/start.sh"]