FROM alpine:3.8
#2019-06-05

ENV NODE_ID=0                     \
    SPEEDTEST=24                   \
    MU_SUFFIX=zhaoj.in            \
    MU_REGEX=%5m%id.%suffix       \
    API_INTERFACE=modwebapi       \
    WEBAPI_URL=https://zhaoj.in   \
    WEBAPI_TOKEN=glzjin           \
    MYSQL_HOST=127.0.0.1          \
    MYSQL_PORT=3306               \
    MYSQL_USER=ss                 \
    MYSQL_PASS=ss                 \
    MYSQL_DB=shadowsocks          \
    REDIRECT=cloudflare.com       
    
RUN apk update    && \
    apk add --no-cache tzdata   && \
    echo "Hongkong" > /etc/timezone && \ 
    ln -sf /usr/share/zoneinfo/Hongkong /etc/localtime  && \
    apk --no-cache add \
                        wget \
                        python3-dev \
                        libsodium-dev \
                        openssl-dev \
                        udns-dev \
                        mbedtls-dev \
                        pcre-dev \
                        libev-dev \
                        libtool \
                        libffi-dev \
                        git \
                        tar \
                        make \
                        py3-pip \
                        autoconf \
                        automake \
                        build-base \
                        linux-headers         && \
     ln -s /usr/bin/python3 /usr/bin/python   && \
     ln -s /usr/bin/pip3    /usr/bin/pip      && \
     git clone -b ipv6 https://github.com/aiastia/testssr.git "/root/shadowsocks" --depth 1 && \
     pip install --upgrade pip                && \
     cd  /root/shadowsocks                    && \
     pip install -r requirements.txt          && \
     cp  apiconfig.py userapiconfig.py        && \
     cp  config.json  user-config.json        && \
     rm -rf ~/.cache && touch /etc/hosts.deny && \
     wget https://raw.githubusercontent.com/aiastia/banip/master/hosts.deny -O hosts.deny && \
     cat ./hosts.deny >> /etc/hosts.deny 


WORKDIR /root/shadowsocks

CMD sed -i "s|NODE_ID = 1|NODE_ID = ${NODE_ID}|"                               /root/shadowsocks/userapiconfig.py && \
    sed -i "s|SPEEDTEST = 24|SPEEDTEST = ${SPEEDTEST}|"                         /root/shadowsocks/userapiconfig.py && \
    sed -i "s|MU_SUFFIX = 'zhaoj.in'|MU_SUFFIX = '${MU_SUFFIX}'|"              /root/shadowsocks/userapiconfig.py && \
    sed -i "s|MU_REGEX = '%5m%id.%suffix'|MU_REGEX = '${MU_REGEX}'|"           /root/shadowsocks/userapiconfig.py && \
    sed -i "s|API_INTERFACE = 'modwebapi'|API_INTERFACE = '${API_INTERFACE}'|" /root/shadowsocks/userapiconfig.py && \
    sed -i "s|WEBAPI_URL = 'https://zhaoj.in'|WEBAPI_URL = '${WEBAPI_URL}'|"   /root/shadowsocks/userapiconfig.py && \
    sed -i "s|WEBAPI_TOKEN = 'glzjin'|WEBAPI_TOKEN = '${WEBAPI_TOKEN}'|"       /root/shadowsocks/userapiconfig.py && \
    sed -i "s|MYSQL_HOST = '127.0.0.1'|MYSQL_HOST = '${MYSQL_HOST}'|"          /root/shadowsocks/userapiconfig.py && \
    sed -i "s|MYSQL_PORT = 3306|MYSQL_PORT = ${MYSQL_PORT}|"                   /root/shadowsocks/userapiconfig.py && \
    sed -i "s|MYSQL_USER = 'ss'|MYSQL_USER = '${MYSQL_USER}'|"                 /root/shadowsocks/userapiconfig.py && \
    sed -i "s|MYSQL_PASS = 'ss'|MYSQL_PASS = '${MYSQL_PASS}'|"                 /root/shadowsocks/userapiconfig.py && \
    sed -i "s|MYSQL_DB = 'shadowsocks'|MYSQL_DB = '${MYSQL_DB}'|"              /root/shadowsocks/userapiconfig.py && \
    sed -i "s|\"redirect\": \"\"|\"redirect\": \"${REDIRECT}\"|"               /root/shadowsocks/user-config.json && \
    python /root/shadowsocks/server.py
