FROM phusion/baseimage:0.9.18
MAINTAINER gulvwien <gulvwien@gmail.com>

# Build arguments
ARG PUSER=oscam 
ARG PGROUP=oscam

# Environment variables.
ENV TERM="xterm" DEBIAN_FRONTEND="noninteractive" HOME="/root"
ENV PUID=920 PGID=920
ENV OSCAMMONITOR=0 OSCAMSSL=0 OSCAMHTTPUSER="" OSCAMHTTPPWD="" OSCAMHTTPCERT=""

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

# Ports
EXPOSE 8888/tcp 24480/udp 15000-15009

#Volumes
VOLUME /config
VOLUME /log

ADD ./install/ /tmp/

# Install application
RUN groupadd -g "$PGID" "$PGROUP" &&\
    useradd -u "$PUID" -M -g "$PGROUP" -G users,dialout -s /bin/false "$PUSER" &&\
    echo "$PUSER" > /etc/container_environment/PUSER &&\
    echo "$PGROUP" > /etc/container_environment/PGROUP &&\
    /tmp/install &&\
    /tmp/copy_files &&\
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* &&\
    mkdir -p /config /log
