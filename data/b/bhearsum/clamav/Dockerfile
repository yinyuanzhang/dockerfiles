FROM debian:jessie
MAINTAINER bhearsum, http://hearsum.ca

RUN apt-get update

# Install ClamAV
RUN apt-get install -y clamav clamav-freshclam

# Update ClamAV Definitions
RUN freshclam
