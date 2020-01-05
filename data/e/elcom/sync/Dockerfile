FROM debian:buster
MAINTAINER LWB

ENV TARGET=VOLUME \
    TARGET_CIFS_SHARE=//server/share \
    TARGET_CIFS_OPTIONS=user=user,password=password \
    TARGET_WEBDAV_HOST=/ \
    TARGET_WEBDAV_USER=user \
    TARGET_WEBDAV_PASSWORD=password \
    TARGET_SSH_HOST=/ \
    TARGET_SSH_USER=user \
    TARGET_PATH=/ \
    TARGET_PATH_LOG=/ \
    TARGET_MOUNT_POINT=/mnt/target \
    TARGET_LOG_MOUNT_POINT=/mnt/log_target

ENV SOURCE=VOLUME \
    SOURCE_CIFS_SHARE=//server/share \
    SOURCE_CIFS_OPTIONS=user=user,password=password \
    SOURCE_WEBDAV_HOST=/ \
    SOURCE_WEBDAV_USER=user \
    SOURCE_WEBDAV_PASSWORD=password \
    SOURCE_SSH_HOST=/ \
    SOURCE_SSH_USER=user \
    SOURCE_PATH=/ \
    SOURCE_PATH_LOG=/ \
    SOURCE_MOUNT_POINT=/mnt/source \
    SOURCE_LOG_MOUNT_POINT=/mnt/log_source

ENV LOG=false \
    LOG_SERVER=127.0.0.1 \
    LOG_PORT=3000 \
    LOG_PROJECT=sync

RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    apt-get install -y --force-yes --no-install-recommends \
    rsync ca-certificates \
    sshfs davfs2 cifs-utils && \
    rm -rf /var/lib/apt/lists

RUN mkdir -p /root/ssh

VOLUME /root/ssh

USER root

COPY docker-entrypoint.sh /usr/local/bin/
RUN ln -s usr/local/bin/docker-entrypoint.sh /entrypoint.sh # backwards compat
RUN chmod +x /usr/local/bin/docker-entrypoint.sh
CMD ["docker-entrypoint.sh"]
