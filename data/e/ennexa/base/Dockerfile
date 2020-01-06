############################################################
# Empty base image with apt-get updated for quick start
# Based on debian:wheezy
############################################################

# Set the base image to Debian:wheezy
FROM debian:jessie

# File Author / Maintainer
MAINTAINER Joyce Babu <joyce@ennexa.com>

RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get upgrade -y

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y vim procps net-tools wget ca-certificates