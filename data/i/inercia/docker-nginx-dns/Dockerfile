FROM debian:jessie

# install nginx+openresty
RUN apt-get update && \
    apt-get install -y ca-certificates     \
                       libreadline-dev     \
                       libncurses5-dev     \
                       libpcre3-dev        \
                       libssl-dev          \
                       wget                \
                       dnsutils            \
                       perl                \
                       make                \
                       build-essential  && \
    cd /tmp                             && \
    wget https://openresty.org/download/ngx_openresty-1.9.3.1.tar.gz && \
    tar xzvf ngx_openresty-*.tar.gz     && \
    cd ngx_openresty-*                  && \
    ./configure                         && \
    make                                && \
    make install                        && \
    rm -rf ngx_openresty-*              && \
    apt-get remove -y libreadline-dev      \
                      libncurses5-dev      \
                      libpcre3-dev         \
                      libssl-dev           \
                      wget                 \
                      perl                 \
                      make                 \
                      build-essential   && \
    apt-get autoremove -y               && \
    apt-get clean                       && \
    apt-get purge                       && \
    rm -rf /var/lib/apt/lists/*

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /usr/local/openresty/nginx/logs/access.log && \
    ln -sf /dev/stderr /usr/local/openresty/nginx/logs/error.log

ADD nginx.conf                /usr/local/openresty/nginx/conf/
ADD wrapper.sh service.template  /home/weave/
ADD lua                       /home/weave/lua

VOLUME ["/var/cache/nginx"]

ENTRYPOINT ["/home/weave/wrapper.sh"]

