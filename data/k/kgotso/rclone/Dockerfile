ARG BASE=alpine:latest
FROM ${BASE}

LABEL maintainer="kgotso"

ARG RCLONE_VERSION=current
ARG ARCH=amd64
ENV SYNC_SRC=
ENV SYNC_TEMP=
ENV SYNC_DEST=
ENV SYNC_OPTS=-v
ENV RCLONE_CMD=sync
ENV RCLONE_DIR_CMD=ls
ENV RCLONE_DIR_CHECK_SKIP=
ENV RCLONE_OPTS="--config /config/rclone.conf"
ENV OUTPUT_LOG=
ENV ROTATE_LOG=
ENV CRON=
ENV CRON_ABORT=
ENV CRON_CLEAR=
ENV FORCE_SYNC=
ENV CHECK_URL=
ENV FAIL_URL=
ENV TZ=

RUN apk -U add ca-certificates fuse wget dcron tzdata \
  && rm -rf /var/cache/apk/*

RUN URL=http://downloads.rclone.org/${RCLONE_VERSION}/rclone-${RCLONE_VERSION}-linux-${ARCH}.zip ; \
  URL=${URL/\/current/} ; \
  cd /tmp \
  && wget -q $URL \
  && unzip /tmp/rclone-${RCLONE_VERSION}-linux-${ARCH}.zip \
  && mv /tmp/rclone-*-linux-${ARCH}/rclone /usr/bin \
  && rm -r /tmp/rclone*

COPY entrypoint.sh /
COPY sync.sh /
COPY sync-abort.sh /
COPY clear.sh /

VOLUME ["/config"]
VOLUME ["/logs"]

ENTRYPOINT ["/entrypoint.sh"]

CMD [""]
