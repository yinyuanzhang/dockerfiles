FROM centos:7

ENV container=docker

RUN \
    yum -y --setopt=tsflags=nodocs install nfs-utils && \
    mkdir -p /exports && \
    yum clean all
COPY run-mountd.sh /

VOLUME ["/exports"]
EXPOSE 111/udp 2049/tcp

ENTRYPOINT ["/run-mountd.sh"]
