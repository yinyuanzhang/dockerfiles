FROM phusion/baseimage:0.11
MAINTAINER Jeffrey Paul <sneak@sneak.berlin>

ENV DEBIAN_FRONTEND=noninteractive

RUN \
    apt update && \
    apt upgrade -y && \
    apt install -y golang git build-essential rsync debmirror && \
    go get -u github.com/ipfs/ipfs-update && \
    /root/go/bin/ipfs-update install latest && \
    rm -rf /root/go && \
    adduser --system --group --home /var/lib/ipfs ipfs && \
    mkdir /etc/service/sync /etc/service/ipfsd

ADD ./sync.run /etc/service/sync/run
ADD ./ipfsd.run /etc/service/ipfsd/run
RUN chmod +x /etc/service/*/run

VOLUME /var/lib/ipfs
VOLUME /var/lib/ubuntumirror

# ipfs ports
EXPOSE 4001
EXPOSE 4002/udp
EXPOSE 5001
EXPOSE 8080
EXPOSE 8081
