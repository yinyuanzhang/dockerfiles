#
# Base image for Ceylon build images
#
FROM ceylon/base-debian:java7

MAINTAINER Tako Schotanus <tako@ceylon-lang.org>

LABEL org.ceylon-lang.dockerfile.description="Base image for Ceylon build images" \
     org.ceylon-lang.dockerfile.vendor="RedHat" \
     org.ceylon-lang.dockerfile.version="1.1"

RUN useradd -ms /bin/bash -G sudo ceylon && echo 'ceylon ALL=(ALL:ALL) NOPASSWD: ALL' > /etc/sudoers.d/ceylon

USER ceylon

WORKDIR /home/ceylon

