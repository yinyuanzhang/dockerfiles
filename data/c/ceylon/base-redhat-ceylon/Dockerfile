#
# Base RedHat image with a Ceylon user with sudo rights
#
FROM ceylon/base-redhat:java7

MAINTAINER Tako Schotanus <tako@ceylon-lang.org>

LABEL org.ceylon-lang.dockerfile.description="Base Fedora image for dealing with RPM build tools and repositories" \
    org.ceylon-lang.dockerfile.vendor="RedHat" \
    org.ceylon-lang.dockerfile.version="1.0"

RUN userdel -r jboss && \
    useradd -ms /bin/bash -G wheel ceylon && \
    echo 'ceylon ALL=(ALL:ALL) NOPASSWD: ALL' > /etc/sudoers.d/ceylon && \
    sed -i -e "s/Defaults    requiretty.*/#Defaults    requiretty/g" /etc/sudoers

USER ceylon

WORKDIR /home/ceylon

