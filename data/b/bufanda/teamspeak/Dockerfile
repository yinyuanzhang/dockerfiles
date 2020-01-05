# -----------------------------------------------------------------------------
# docker-teamspeak
#
# Builds a basic docker image that can run TeamSpeak
# (http://teamspeak.com/).
#
# Authors: Isaac Bythewood, Jamie Tanna
# Updated: January 6th, 2017
# Require: Docker (http://www.docker.io/)
# -----------------------------------------------------------------------------

# Base system is Ubuntu 16.04
FROM   ubuntu:16.04

#image label
ARG BUILD_DATE
ARG VCS_REF

LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url="https://github.com/bufanda/docker-teamspeak" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.schema-version="1.0.0-rc1"

# Set the Teamspeak version to download
ENV TSV=3.10.2

# Download and install everything from the repos.
RUN    DEBIAN_FRONTEND=noninteractive \
        apt-get -y update && \
        apt-get -y install bzip2 ca-certificates && \
        rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
        apt-get autoremove -y && \
        apt-get clean

# Download and install TeamSpeak 3
# Add secondary/backup server as well -- allow users to choose in case of blacklisting.
#ADD    http://dl.4players.de/ts/releases/${TSV}/teamspeak3-server_linux_amd64-${TSV}.tar.bz2 ./
ADD    https://files.teamspeak-services.com/releases/server/${TSV}/teamspeak3-server_linux_amd64-${TSV}.tar.bz2 ./
#ADD	http://dl.4players.de/ts/releases/pre_releases/server/${TSV}${SUFFIX}/teamspeak3-server_linux_amd64-${TSV}.tar.bz2 ./
#ADD    http://teamspeak.gameserver.gamed.de/ts3/releases/${TSV}/teamspeak3-server_linux_amd64-${TSV}.tar.bz2 ./
ADD    CHECKSUMS ./
RUN    sha256sum -c CHECKSUMS

RUN    tar jxf teamspeak3-server_linux_amd64-$TSV.tar.bz2 && \
       mv teamspeak3-server_linux_amd64 /opt/teamspeak && \
       rm teamspeak3-server_linux_amd64-$TSV.tar.bz2

# Load in all of our config files.
ADD    ./scripts/start /start

# Fix all permissions
RUN    chmod +x /start

# /start runs it.
EXPOSE 9987/udp
EXPOSE 30033
EXPOSE 10011

RUN    useradd teamspeak && mkdir /data && chown teamspeak:teamspeak /data && \
       chown -R teamspeak:teamspeak /opt/teamspeak
VOLUME ["/data"]
USER   teamspeak
CMD    ["/start"]
