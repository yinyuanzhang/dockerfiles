FROM lsiobase/alpine

ARG RCLONE_VERSION="current"
ARG RCLONE_ARCH="amd64"
RUN \
    # add required packages
    apk add --no-cache --update \
        \
        # borgbackup
        borgbackup \
        \
        # mariadb
        mariadb-client \
        \
        # email
        ssmtp \
        \
        # signal messenger
        curl; \
    \
    # install rclone
    cd /tmp; \
    wget -q http://downloads.rclone.org/rclone-${RCLONE_VERSION}-linux-${RCLONE_ARCH}.zip; \
    unzip /tmp/rclone-${RCLONE_VERSION}-linux-${RCLONE_ARCH}.zip; \
    mv /tmp/rclone-*-linux-${RCLONE_ARCH}/rclone /usr/bin; \
    chown root:root /usr/bin/rclone; \
    chmod 755 /usr/bin/rclone; \
    \
    # cleanup
    rm -rf \
        /tmp/* \
        /var/tmp/* \
        /var/cache/apk/*

# global environment settings
ENV BORG_CACHE_DIR=/cache
ENV BORG_CONFIG_DIR=/config/borg
ENV BASE_REPOSITORY=/repository
ENV SOURCE_DIR=/source
ENV RCLONE_CONFIG=/config/rclone/rclone.conf
ENV RCLONE_DRIVE_USE_TRASH=false

COPY opt /opt
COPY crontab.txt /etc/crontabs/root

RUN \
    # set execute bit on all shell files
    chmod 755 /opt/*.sh; \
    chown -R root:root /opt; \
    \
    # setup ssmtp
    ln -sf /config/ssmtp/ssmtp.conf /etc/ssmtp/ssmtp.conf; \
    :

VOLUME /cache /repository /source /config
CMD ["/usr/sbin/crond", "-f"]
