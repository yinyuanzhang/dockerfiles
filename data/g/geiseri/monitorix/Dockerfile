FROM ubuntu:latest

MAINTAINER Ian Geiser <geiseri@yahoo.com>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get install -yq curl && \
    echo "deb http://apt.izzysoft.de/ubuntu generic universe" >> "/etc/apt/sources.list" && \
    curl http://apt.izzysoft.de/izzysoft.asc | apt-key add - && \
    apt-get update && \
    apt-get install -yq monitorix \
                        libvirt-bin lm-sensors smartmontools \
                        hddtemp iptables squidclient mysql-client \
                        && \
    apt-get clean


# Add config for docker
ADD support/monitorix.conf /etc/monitorix/monitorix.conf
VOLUME /etc/monitorix/conf.d /var/lib/monitorix/data

# Add the launch script
ADD support/launch.sh /launch.sh
RUN chmod +x /launch.sh

ENTRYPOINT /launch.sh

