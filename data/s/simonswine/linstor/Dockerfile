FROM ubuntu:16.04

RUN apt-get update && \
  apt-get install -y software-properties-common && \
  add-apt-repository ppa:linbit/linbit-drbd9-stack && \
  apt-get update && \
  apt-get install -y linstor-client=0.5.0-1ppa1~xenial1 linstor-controller=0.5.0-1ppa1~xenial1


CMD ["/usr/share/linstor-server/bin/Controller", "--logs=/var/log/linstor-controller", "--config-directory=/etc/linstor"]

