FROM centos:latest
MAINTAINER f wowwow2wowwow@gmail.com
ENV pass ss-obfs

COPY config.json /root/

RUN yum install epel-release wget -y &&\
    cd /etc/yum.repos.d/ && wget https://copr.fedorainfracloud.org/coprs/librehat/shadowsocks/repo/epel-7/librehat-shadowsocks-epel-7.repo &&\
    yum install shadowsocks-libev git gcc autoconf libtool automake make zlib-devel openssl-devel asciidoc xmlto libev-devel -y &&\
    cd /root/ && git clone https://github.com/shadowsocks/simple-obfs.git &&\
    cd simple-obfs && git submodule update --init --recursive &&\
    ./autogen.sh && ./configure && make && make install &&\
    rm -rf /root/simple-obfs && yum clean all -y &&\
    sed -i "s/test/$pass/" /root/config.json

EXPOSE 443

ENTRYPOINT ["ss-server", "-c", "/root/config.json"]
