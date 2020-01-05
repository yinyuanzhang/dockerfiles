FROM debian:jessie
MAINTAINER Keith Bentrup <kbentrup@ebay.com>

RUN apt update && \
  DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes redis-server && \
  apt-get --purge autoremove -y && \
  apt-get clean && \
  rm -rf /var/lib/{apt,dpkg,cache,log}/ /tmp/* /var/tmp/*

EXPOSE 6379

CMD ["/usr/bin/redis-server"]
