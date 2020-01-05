############################################################
# Dockerfile to build EdgeFS container image
# Based on Ubuntu
############################################################

# Set the base image to Ubuntu to produce amd64 binary
FROM edgefs/edgefs:latest as builder

RUN apt-get update &&\
    apt-get install -y software-properties-common python-software-properties &&\
    add-apt-repository ppa:git-core/ppa &&\
    apt-get update &&\
    apt-get install -y git make

RUN mkdir -p /opt/nedge

# copy project files to container
COPY . /opt/edgefs-nodejs

WORKDIR /opt/edgefs-nodejs

RUN /bin/bash -c "cd /opt/edgefs-nodejs; rm -rf deps; git pull; git checkout deps; ls -la; source ./env.sh; make NEDGE_NDEBUG=1 NEDGE_VERSION=${NEDGE_VERSION} install"
RUN /bin/bash -c "mkdir -p /opt/nedge.dest/lib /opt/nedge.dest/sbin; cd /opt/nedge; cp -a lib/libblake2* lib/libconnbroker.so* lib/libccowd.so* lib/liberasurecode.so* lib/libXorcode.so* lib/libquorum.so* lib/libcfg.so* lib/libcpg.so* lib/libcorosync_common.so* lib/libknet.so* lib/libqb.so* lib/libccow.so* lib/libuv.so* lib/libnanomsg.so* lib/libjemalloc.so* lib/libccowutil.so* lib/libccowfsio.so* /opt/nedge.dest/lib; cp -ar etc etc.default nodejs restapi neadm /opt/nedge.dest; cp /opt/edgefs-nodejs/env.sh /opt/nedge.dest; cp sbin/corosync-cpgtool sbin/efscli sbin/restapi-start.sh sbin/nedel sbin/nelist sbin/nelogview sbin/nemod sbin/netrlogchk sbin/ecstat sbin/blobfind /opt/nedge.dest/sbin"


FROM ubuntu:16.04
MAINTAINER EdgeFS
LABEL description="EdgeFS REST API service"

ENV DEBUG=*

RUN apt-get update &&\
    \
    apt-get install -y libssl1.0.0 iproute2 nvi libcgroup1 &&\
    \
    apt-get purge -y --auto-remove && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    find /usr/share/doc -depth -type f ! -name copyright|xargs rm -f && \
    rm -rf /usr/share/man /usr/share/groff /usr/share/info /usr/share/lintian /usr/share/linda /var/cache/man && \
    \
    mkdir -p /opt/nedge/var/log

COPY --from=builder /opt/nedge.dest /opt/nedge/
COPY --from=builder /opt/edgefs-nodejs/scripts/toolbox /usr/bin/
WORKDIR /opt/nedge
ENTRYPOINT ["/opt/nedge/sbin/restapi-start.sh"]
