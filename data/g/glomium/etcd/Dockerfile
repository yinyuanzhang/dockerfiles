FROM alpine:3.11.2
MAINTAINER Sebastian Braun <sebastian.braun@fh-aachen.de>
# base alpine template

ARG VERSION=v3.4.3

RUN mkdir -p /tmp/etcd-download \
 && apk add --no-cache bind-tools \
 && apk add --no-cache --virtual build-dependencies curl \
 && curl -sL https://github.com/etcd-io/etcd/releases/download/$VERSION/etcd-$VERSION-linux-amd64.tar.gz -o /tmp/etcd-$VERSION-linux-amd64.tar.gz \
 && apk del build-dependencies \
 && tar xzvf /tmp/etcd-${VERSION}-linux-amd64.tar.gz -C /tmp/etcd-download --strip-components=1 \
 && mv /tmp/etcd-download/etcd /usr/local/bin \
 && mv /tmp/etcd-download/etcdctl /usr/local/bin \
 && rm -rf /tmp/etcd-download /tmp/etcd-${VERSION}-linux-amd64.tar.gz

EXPOSE 2379/tcp 2380/tcp
VOLUME /data

# COPY docker/etcd/run.sh /usr/local/bin/

ENV ETCDCTL_API=3

# ENV MIN_SEEDS_COUNT=3
# HEALTHCHECK --interval=5s --retries=3 --timeout=10s CMD ETCDCTL_API=3 /usr/local/bin/etcdctl --endpoints=http://127.0.0.1:2379 get ping | grep -q pong
# ENTRYPOINT ["/sbin/tini", "--", "/bin/run.sh"]

ENTRYPOINT ["/usr/local/bin/etcd"]
