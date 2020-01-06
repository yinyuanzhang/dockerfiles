FROM alpine

RUN apk add curl unzip fuse

RUN curl -O https://downloads.rclone.org/rclone-current-linux-amd64.zip && \
  unzip rclone-current-linux-amd64.zip && \
  rm rclone-current-linux-amd64.zip && \
  cd rclone-*-linux-amd64 && \
  cp rclone /usr/bin/ && \
  chown root:root /usr/bin/rclone && \
  chmod 755 /usr/bin/rclone

RUN mkdir /data

ENTRYPOINT rclone mount --vfs-cache-mode writes $RCLONE_CONFIG_NAME:$MINIO_BUCKET_NAME /data
