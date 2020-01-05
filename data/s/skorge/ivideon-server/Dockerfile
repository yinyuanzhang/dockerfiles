FROM ubuntu:14.04

MAINTAINER skorge

# Run a quick apt-get update/upgrade
RUN apt-get update && apt-get upgrade -y && apt-get autoremove -y --purge

# Install dependencies
RUN apt-get update && \
    apt-get install -y \
    wget \
    psmisc

# Run as root
USER root

# Setup default environment variables for the server
ENV USER "root"
ENV TZ="Europe/Stockholm"
ENV ENABLE_WEB_INTERFACE="true"

# Setup volumes
#VOLUME ["/data"]
#VOLUME ["/opt/ivideon/videoserverd"]
#VOLUME ["/video_archive"]

# Prepare iVideon repository
RUN wget "http://packages.ivideon.com/ubuntu/keys/ivideon.list" -O "/etc/apt/sources.list.d/ivideon.list" && \
wget -O - "http://packages.ivideon.com/ubuntu/keys/ivideon.key" | apt-key add -
    


# Install iVideon
RUN apt-get update && \
    apt-get install -y \
    ivideon-server-headless

# Cleanup
RUN apt-get clean


# Create config and archive directory
RUN mkdir -p /opt/ivideon/data/archive

# Start the server
ENTRYPOINT ["/opt/ivideon/ivideon-server/videoserver","-c","/opt/ivideon/data/videoserverd.config"]
