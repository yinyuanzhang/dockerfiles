# import the linuxserver/plex repository
FROM linuxserver/plex
MAINTAINER Adam Howell

#
# Update the image to the latest packages
RUN \
    apt-get update && \
    apt-get install -y \
        handbrake-cli \
        ffmpeg \
        mediainfo \
        vim \
        bc

#
# Clean up as linuxserver/plex does
RUN apt-get clean
