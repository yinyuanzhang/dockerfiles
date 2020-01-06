FROM alpine:3.7 AS builder

MAINTAINER NANKI Haruo

RUN apk update && apk --no-cache add curl

ENV GOOFYS_VERSION 0.20.0
RUN curl --fail -sSL -o /usr/local/bin/goofys https://github.com/kahing/goofys/releases/download/v${GOOFYS_VERSION}/goofys \
    && chmod +x /usr/local/bin/goofys

FROM alpine:3.7

RUN apk --no-cache add fuse coreutils libc6-compat ca-certificates

ENV MOUNT_DIR /mnt/s3
ENV REGION us-east-1
ENV BUCKET teleport-bucket
ENV STAT_CACHE_TTL 1m0s
ENV TYPE_CACHE_TTL 1m0s
ENV DIR_MODE 0700
ENV FILE_MODE 0600

RUN mkdir /mnt/s3

VOLUME /mnt/s3

COPY --from=builder /usr/local/bin/goofys /usr/local/bin/goofys

ADD rootfs/ /

RUN sed -i -e 's/#user_allow_other/user_allow_other/' /etc/fuse.conf
RUN chmod +x /usr/bin/run.sh

ENTRYPOINT ["sh"]
CMD ["/usr/bin/run.sh"]
