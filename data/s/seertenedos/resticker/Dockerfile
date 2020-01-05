#
# Builder image
#
FROM golang:1.12 AS builder

# ARG RESTIC_VERSION=0.9.6
# ARG RESTIC_SHA256=1cc8655fa99f06e787871a9f8b5ceec283c856fa341a5b38824a0ca89420b0fe
ARG GO_CRON_VERSION=0.0.4
ARG GO_CRON_SHA256=6c8ac52637150e9c7ee88f43e29e158e96470a3aaa3fcf47fd33771a8a76d959
ARG RCLONE_VERSION=1.49.5
ARG RCLONE_SHA256=7922455f95e8e71f9e484f84ac3ae015379e65ccc3f7d93d804fc0a76515c973

RUN curl -sL -o go-cron.tar.gz https://github.com/djmaze/go-cron/archive/v${GO_CRON_VERSION}.tar.gz \
 && echo "${GO_CRON_SHA256}  go-cron.tar.gz" | sha256sum -c - \
 && tar xzf go-cron.tar.gz \
 && cd go-cron-${GO_CRON_VERSION} \
 && go build \
 && mv go-cron /usr/local/bin/go-cron \
 && cd .. \
 && rm go-cron.tar.gz go-cron-${GO_CRON_VERSION} -fR

RUN curl -sL -o rclone.zip https://downloads.rclone.org/v${RCLONE_VERSION}/rclone-v${RCLONE_VERSION}-linux-amd64.zip \
 && echo "${RCLONE_SHA256}  rclone.zip" | sha256sum -c - \
 && apt-get update -qq \
 && apt-get install -yq unzip \
 && unzip -a rclone.zip \
 && mv rclone-v${RCLONE_VERSION}-linux-amd64/rclone /usr/local/bin/rclone \
 && rm rclone.zip rclone-v${RCLONE_VERSION}-linux-amd64 -fR \
 && rm /var/lib/apt/lists/* -fR

# RUN curl -sL -o restic.tar.gz  https://github.com/restic/restic/releases/download/v${RESTIC_VERSION}/restic-${RESTIC_VERSION}.tar.gz \
#  && echo "${RESTIC_SHA256}  restic.tar.gz" | sha256sum -c - \
#  && tar xzf restic.tar.gz \
#  && cd restic-${RESTIC_VERSION} \
#  && go run build.go \
#  && mv restic /usr/local/bin/restic \
#  && cd .. \
#  && rm restic.tar.gz restic-${RESTIC_VERSION} -fR
 
 # based on restic 0.9.6
 RUN curl -sL -o restic.tar.gz https://github.com/ifedorenko/restic/archive/out-of-order-restore-no-progress.tar.gz \
 && tar xzf restic.tar.gz \
 && cd restic-out-of-order-restore-no-progress \
 && go run build.go \
 && mv restic /usr/local/bin/restic \
 && cd .. \
 && rm restic.tar.gz restic-out-of-order-restore-no-progress -fR

#
# Final image
#
FROM alpine:3.10

RUN apk add --update --no-cache ca-certificates fuse nfs-utils openssh tzdata bash curl
RUN apk add --no-cache --repository=http://dl-cdn.alpinelinux.org/alpine/edge/community/ docker-cli

ENV RESTIC_REPOSITORY /mnt/restic

COPY --from=builder /usr/local/bin/* /usr/local/bin/
COPY backup /usr/local/bin/
COPY entrypoint /

ENTRYPOINT ["/entrypoint"]
