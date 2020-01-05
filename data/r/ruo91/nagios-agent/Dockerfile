#
# Title: Nagios Agent (NRPE)
#
# Maintainer: Yongbok Kim (ruo91@yongbok.net)
#
# - Build
# docker build --rm -t nagios:agent .
#
# - Run
# docker run -d --name="nagios-agent" -h "nagios-agent" -p 5666:5666 -p 5667:5667 nagios:agent

# Base images
FROM     centos:centos6
MAINTAINER Yongbok Kim <ruo91@yongbok.net>

# WorkDIR
ENV SRC_DIR /opt
WORKDIR $SRC_DIR

# Nagios Client
RUN curl -LO "https://assets.nagios.com/downloads/nagiosxi/agents/linux-nrpe-agent.tar.gz" \
 && tar xzvf linux-nrpe-agent.tar.gz && rm -rf *.tar.gz

# Disable firewall
RUN cd linux-nrpe-agent \
 && touch installed.firewall

# NRPE patch
ADD conf/nagios_nrpe_only_from.patch $SRC_DIR/linux-nrpe-agent/nagios_nrpe_only_from.patch
RUN yum install -y patch && cd linux-nrpe-agent && patch -p0 < nagios_nrpe_only_from.patch

# Build
RUN cd linux-nrpe-agent \
 && ./fullinstall -n && cd $SRC_DIR && rm -rf linux-nrpe-agent

# Supervisor
RUN yum install -y python-setuptools python-meld3 \
 && easy_install pip \
 && pip install --upgrade pip \
 && pip install supervisor \
 && mkdir /etc/supervisord.d
ADD conf/supervisord.conf /etc/supervisord.d/supervisord.conf

# Ports
EXPOSE 5666 5667

# Supervisor
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.d/supervisord.conf"]
