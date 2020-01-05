FROM ubuntu:trusty

ENV HAPROXY_VERSION=1.5.14

RUN \
  set -x && \
  apt-get update && apt-get install -y inotify-tools wget tar gzip make gcc libc6-dev libpcre3-dev libssl-dev && \
  wget -O /tmp/haproxy.tgz http://www.haproxy.org/download/1.5/src/haproxy-${HAPROXY_VERSION}.tar.gz && \
  mkdir -p /usr/local/haproxy && \
  tar -zxvf /tmp/haproxy.tgz -C /usr/local/haproxy/ --strip-components 1 && \
  rm -f /tmp/haproxy.tgz && \
  cd /usr/local/haproxy && \
  make \
  USE_LINUX_TPROXY=1 USE_ZLIB=1 \
  USE_REGPARM=1 \
  USE_OPENSSL=1 \
  USE_PCRE=1 \
  TARGET=linux2628 \
  CFLAGS="-O2 -g -fno-strict-aliasing -DTCP_USER_TIMEOUT=18" && \
  make install && \
  #apt-get remove -y make gcc libssl-dev && \
  apt-get clean all && \
  rm -rf /usr/local/haproxy && \
  mkdir -p /var/lib/haproxy && \
  chown -R 777 /var/lib/haproxy
  #groupadd haproxy && adduser Ganduruu haproxy && chown -R 777 haproxy:haproxy /var/lib/haproxy

ADD container-files /

ENV HAPROXY_CONFIG /etc/haproxy/haproxy.cfg

#ADD bootstrap.sh /bootstrap.sh 
RUN chmod +x /*.sh

EXPOSE 80 443 1936

CMD ["./bootstrap.sh"]
