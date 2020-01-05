FROM resin/aarch64-alpine

RUN ["cross-build-start"]

ENV GOPATH="/go" \
    AccessFolder="/mnt" \
    RemotePath="mediaefs:" \
    MountPoint="/mnt/mediaefs" \
    ConfigDir="/config" \
    ConfigName=".rclone.conf" \
    MountCommands="--allow-other --allow-non-empty" \
    UnmountCommands="-u -z"

## Alpine with Go Git
RUN apk add --no-cache --update alpine-sdk ca-certificates go git fuse fuse-dev \
	&& go get -u -v github.com/ncw/rclone \
	&& cp /go/bin/rclone /usr/sbin/ \
	&& rm -rf /go \
	&& apk del alpine-sdk go git \
	&& rm -rf /tmp/* /var/cache/apk/* /var/lib/apk/lists/*

ADD start.sh /start.sh
RUN chmod +x /start.sh

RUN ["cross-build-end"]

VOLUME ["/mnt"]

CMD ["/start.sh"]
