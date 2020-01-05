###################################################################################
# Docker file for Subsonic media player - see http://subsonic.org.
#
# Author: Markus Duering
###################################################################################

ARG  DEBIAN_VERSION=stretch
# Download base image debian stretch
FROM debian:${DEBIAN_VERSION}

# Maintainer of this Dockerfile
LABEL maintainer="marduer <markus.d@gmx.de>"

# Environment variables

# Used Subsonic version
ENV SUBSONIC_VERSION 6.1.6
# Used port for Subsonic
ENV PORT 4040
# Used path for context (for something like yourdomain.org/subsonic)
ENV CONTEXT_PATH /
# User id depends on the host system user
ENV UID 1002
# Group id depends on the host system group
ENV GID 1000
# Used memory for JAVA virtual machine
ENV JVM_MEMORY=512
# Former media path (original installation without docker - necessary to have the same path in the imported database from the old system)
ENV OLD_MUSIC_DIRECTORY /srv/dev-disk-by-label-SWRaid01/MUSIK

# Labels - image metadata
LABEL version="0.0.1"
LABEL subsonicversion="$SUBSONIC_VERSION"
LABEL description="Subsonic media streamer"

# Set user root
USER root

# Set the working dir
WORKDIR /

# Port for subsonic
EXPOSE 4040
# Port for https
EXPOSE 4043

# get the necessary packages for installation
RUN apt-get update \
    && apt-get install -y gosu openjdk-8-jre wget libav-tools lame \
    && mkdir /var/subsonic \
    && mkdir /usr/local/subsonic \
    && wget -O /usr/local/subsonic/subsonic.tar.gz https://s3-eu-west-1.amazonaws.com/subsonic-public/download/subsonic-${SUBSONIC_VERSION}-standalone.tar.gz \
    && tar -zxf /usr/local/subsonic/subsonic.tar.gz -C /usr/local/subsonic \
    && rm /usr/local/subsonic/subsonic.tar.gz \
    && rm /usr/local/subsonic/subsonic.bat \
    && mkdir -p ${OLD_MUSIC_DIRECTORY}

# for debugging maybe the following packages are interessting: apt-get install procps


# make the music directory visible to extern
VOLUME ["${OLD_MUSIC_DIRECTORY}"]
VOLUME ["/var/subsonic"]

# make the subsonic script executable
RUN chmod +x /usr/local/subsonic/subsonic.sh

# copy the entrypoint script and make it executable
COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh
# for backwards compat
# RUN ln -s /usr/local/bin/docker-entrypoint.sh /

# Entrypoint for the docker image
ENTRYPOINT ["docker-entrypoint.sh"]
# Run this when the container is started
CMD ["/usr/local/subsonic/subsonic.sh"]





