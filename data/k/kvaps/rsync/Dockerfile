FROM alpine as builder
ENV RSYNC_VERSION=3.1.3

ADD patches /rsync-${RSYNC_VERSION}/patches

RUN apk --no-cache add gcc build-base perl git \
 && wget -O- https://download.samba.org/pub/rsync/src/rsync-${RSYNC_VERSION}.tar.gz | tar -xzf- \
 && cd /rsync-${RSYNC_VERSION} \
 && patch -p1 <patches/copy-write-devices.diff \
 && ./prepare-source \
 && ./configure \
 && make \
 && make install

FROM alpine
COPY --from=builder /usr/local/bin/rsync /usr/local/bin/rsync
ENTRYPOINT [ "/usr/local/bin/rsync" ]
