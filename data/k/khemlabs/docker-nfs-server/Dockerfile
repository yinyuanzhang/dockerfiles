FROM khemlabs/ubuntu-essential
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update -qq && apt-get install -y nfs-kernel-server runit inotify-tools -qq
RUN mkdir -p /exports

RUN mkdir -p /etc/sv/nfs

# ADD drive partition
RUN mkdir -p /space/data

ADD nfs.init /etc/sv/nfs/run
ADD nfs.stop /etc/sv/nfs/finish

ADD nfs_setup.sh /usr/local/bin/nfs_setup

VOLUME /exports

EXPOSE 111/udp 2049/tcp

ENTRYPOINT ["/usr/local/bin/nfs_setup"]
