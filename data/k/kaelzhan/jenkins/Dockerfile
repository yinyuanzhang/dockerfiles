FROM jenkins/jenkins:2.138.1
MAINTAINER kael.zhan@qq.com

ENV DEBIAN_FRONTEND=noninteractive

EXPOSE 8080

USER root

COPY provision/* /opt/provision/

#
# The Debian release referenced below for the Mesosphere repo should be
# compatible with the one used by the upstream Jenkins container.
#
RUN cd /opt/provision \
    && ./base-setup.sh \
    && ./install-packages.sh \
    && ./base-cleanup.sh

# ADD and COPY are always done as root regardless of the USER directive preceeding them so
# chown the plugins copied over above
USER jenkins

COPY plugins.txt /tmp/
RUN /usr/local/bin/install-plugins.sh < /tmp/plugins.txt
