FROM alpine

RUN apk update ; apk upgrade && \
    apk add luajit luarocks luarocks5.1 \
        lua5.1-filesystem lua5.1-busted lua5.1-socket lua5.1-copas lua5.1-cliargs \
        lua5.1-system lua5.1-say lua5.1-luassert lua5.1-term lua5.1-penlight lua5.1-sql-sqlite3\
        lua-dev musl-dev gcc nginx-mod-http-lua git && \
    luarocks-5.1 --tree=/usr install sailor && \
    cd /srv/ && git clone --depth=1 https://github.com/sailorproject/sailor && \
    rm -r /usr/share/lua/5.1/sailor/ /usr/share/lua/5.1/web_utils && \
    mv sailor/src/* /usr/share/lua/5.1/ && \
    rm -r sailor && apk del git gcc musl-dev

RUN mkdir -p /usr/local/share/lua && \
    ln -s /usr/share/lua/common/* /usr/share/lua/5.1/ || true && \
    ln -s /usr/share/lua/5.1 /usr/local/share/lua/

RUN mkdir /run/nginx ; \
    echo 'daemon off;' >> /etc/nginx/nginx.conf

ADD default.conf /etc/nginx/conf.d/default.conf

# Bugfix : gfind is a deprecated lua function
RUN sed -i s/gfind/gmatch/g /usr/share/lua/5.1/latclient/starlight.lua

VOLUME ["/app"]

WORKDIR /app

EXPOSE 80

ENTRYPOINT [ "/usr/sbin/nginx" ]
