####################
# BASE IMAGE
####################
FROM ubuntu:16.04

MAINTAINER prc2k10@googlemail.com <prc2k10@googlemail.com>

# Install wget, lsb-release, curl, fuse and tree
RUN apt-get update && apt-get upgrade -y && apt-get install -y wget lsb-release curl fuse libfuse2  net-tools gnupg2 systemd tree

# Add key
RUN wget -O - http://ppa.moosefs.com/moosefs.key | apt-key add -
RUN echo "deb http://ppa.moosefs.com/moosefs-3/apt/$(awk -F= '$1=="ID" { print $2 ;}' /etc/os-release)/$(lsb_release -sc) $(lsb_release -sc) main" > /etc/apt/sources.list.d/moosefs.list

# Install MooseFS client
RUN apt-get update && apt-get install -y moosefs-client

# S6 overlay
ENV S6_BEHAVIOUR_IF_STAGE2_FAILS=2
ENV S6_KEEP_ENV=1

RUN \
    OVERLAY_VERSION=$(curl -sX GET "https://api.github.com/repos/just-containers/s6-overlay/releases/latest" | awk '/tag_name/{print $4;exit}' FS='[""]') && \
    curl -o /tmp/s6-overlay.tar.gz -L "https://github.com/just-containers/s6-overlay/releases/download/${OVERLAY_VERSION}/s6-overlay-amd64.tar.gz" && \
    tar xfz  /tmp/s6-overlay.tar.gz -C /

# Add and run start script
ADD start-client.sh /home/start-client.sh
RUN chown root:root /home/start-client.sh
RUN chmod 700 /home/start-client.sh

RUN mkdir -p /mnt/moosefs

VOLUME /mnt/moosefs

ENTRYPOINT ["/init"]
