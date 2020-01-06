# Pull base image.
FROM debian:buster

MAINTAINER Peter Sarossy <peter.sarossy@gmail.com>

# Set environment.
ENV DEBIAN_FRONTEND noninteractive

# Install packages.
RUN apt-get update
RUN apt-get install -y curl python sqlite3 wget python-influxdb

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Define working directory.
WORKDIR /opt/btmon

# Add files to the container.
ADD . /opt/btmon

# Define volumes.
VOLUME ["/etc/bind", "/var/lib/bind", "/var/run/named"]

# Define the command script.
CMD ["/bin/sh", "-c", "./btmon"]
