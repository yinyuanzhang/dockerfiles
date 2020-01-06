FROM haugene/transmission-openvpn:latest

# install Java for running filebot 
#   update packages, install debconf-utils so that we can install Oracle java without for reading terms and accepting it, use debconf for pre accepting the terms, then install oracle-java8-installer

RUN apt-get update && \
    apt-get install -y  --no-install-recommends openjdk-8-jre-headless libchromaprint-tools libmediainfo0v5
