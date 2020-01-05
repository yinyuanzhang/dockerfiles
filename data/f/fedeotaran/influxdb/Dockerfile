FROM ubuntu:16.04

MAINTAINER fedeotaran <otaran.federico@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

# Set correct environment variables
ENV HOME /root
# Don't ask user options when installing
env   DEBIAN_FRONTEND noninteractive
RUN echo APT::Install-Recommends "0"; >> /etc/apt/apt.conf
RUN echo APT::Install-Suggests "0"; >> /etc/apt/apt.conf

# Update system
RUN apt-get -y update && apt-get -y dist-upgrade
RUN apt-get -y install wget

# Install Influx db
RUN wget http://dl.influxdata.com/influxdb/releases/influxdb_0.12.2-1_amd64.deb
RUN dpkg -i influxdb_0.12.2-1_amd64.deb

# Admin server WebUI
EXPOSE 8083

# HTTP API
EXPOSE 8086

# Raft port (for clustering, don't expose publicly!)
#EXPOSE 8090

# Protobuf port (for clustering, don't expose publicly!)
#EXPOSE 8099

VOLUME ["/data"]

ENTRYPOINT ["influxd"]
