FROM alpine:latest
#
# Need rdiff-backup for core functionality, ssh to connect to other stuff
# and busybox to allow the ssh environment config script to work.
RUN apk --update add \
    busybox \
    openssh-client \
    rdiff-backup
#
# Set up user for this to run as
RUN adduser -D -G root -g "Rdiff Backup" rdiff
#
#
LABEL org.freenas.interactive="true" \
      org.freenas.version="1.0.2" \
      org.freenas.upgradeable="true" \
      org.freenas.expose-ports-at-host="false" \
      org.freenas.autostart="false" \
      org.freenas.volumes="[ { \"name\": \"/config\", \"type\": \"host\", \"descr\": \"Config storage space\" }, { \"name\": \"/data\", \"type\": \"host\", \"descr\": \"Data volume\" } ]"
#
COPY run-rdiff-backups.sh /usr/local/bin/
COPY VERSION .
COPY README.md .
#
# We run as user rdiff
USER rdiff
#
# Pair of volumes to use for config and stored data
VOLUME ["/config", "/data"]
#
# Config directory locations
ENV HOME=/home/rdiff \
    CONFIG=/config
#
# Run the ssh setup then rdiff-backup
ENTRYPOINT ["/usr/local/bin/run-rdiff-backups.sh"]
