# Dtella@Home NMDC Server
#
# Dtella is an open-source, decentralized server for the NMDC protocol originally
# created by Purdue for internal file sharing. This docker image is based on the
# the Dtella@Home port of the original software:
# 	https://code.google.com/archive/p/dtella-home/
# Only modifications to make the Dtella@Home software ports predicatable, provide
# a unique network/encryption key, and add a better persisten storage path have been
# made.
#
# Host networking is required to properly bind to the loopback interface.
#
# Your NMDC client must connect to 127.0.0.1 and must report the local IP address
# as 127.0.0.1
#
# Dtella does not perform active IP detection for it's internal translations. Client
# IP addresses will be inferred via the Dtella connections. As a result, it is not
# safe to use multiple clients behind the same NAT, without using NAT loopback, when
# connecting to other public IP addresses.
#
# Set NETWORK_KEY to define a custom encryption key for your network and to control
# access.
#
# Mount a directory to /data for persistent storage of logs and clients.

# Start with python slim base image
FROM python:2.7.14-slim

MAINTAINER Adam Schultz <adam.schultz@live.com>

# Set environment variables for aptitute package management
ENV DEBIAN_FRONTEND="noninteractive" HOME="/root" LC_ALL="C.UTF-8" LANG="en_US.UTF-8" LANGUAGE="en_US.UTF-8"

# Avoid docker bug
RUN ln -s -f /bin/true /usr/bin/chfn

# Install required tools
RUN apt-get -q update && apt-get install -qy gcc && \
    pip install -v twisted PyCrypto dnspython gdata && \
    apt-get -y purge gcc && \
    apt-get -y clean && apt-get -y autoclean && apt-get -y autoremove

# Debug tools
#RUN apt-get -q update && apt-get install -qy net-tools tcpdump nano telnet && \
#    apt-get -y clean && apt-get -y autoclean && apt-get -y autoremove

# Copy in Dtella
RUN mkdir /dtella
COPY dtella-home-1.1.5 /dtella/
RUN chmod -R 755 /dtella/

# For storing persistent information (logs, clients, etc)
RUN mkdir /data
RUN chmod 777 /data
VOLUME ["/data"]

# Modified Dtella uses TCP 27999 as the NMDC server port and UDP 27998 as Dtella-to-Dtella port
EXPOSE 27998/UDP 27999/TCP

# Run the server
CMD ["/dtella/dtella.py"]
