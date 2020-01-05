FROM alpine:3.10

ENV RCLONE_VERSION=v1.48.0 \
    RCLONE_CONF_DIR=/root/.config/rclone \
    RESTIC_PASSWORD=pleaseChangeMe \
    RESTIC_PASSWORD_FILE=/tmp/restic_pass

RUN apk add --no-cache curl restic rsync \
    && curl -O https://downloads.rclone.org/$RCLONE_VERSION/rclone-$RCLONE_VERSION-linux-amd64.zip \
    && unzip rclone-$RCLONE_VERSION-linux-amd64.zip \
    && cp rclone-$RCLONE_VERSION-linux-amd64/rclone /usr/bin/ \
    && chown root:root /usr/bin/rclone \
    && chmod 755 /usr/bin/rclone \
    && mkdir -p $RCLONE_CONF_DIR

VOLUME [ "/pvc-files", "/restic", "/root/.config/rclone" ]

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]
