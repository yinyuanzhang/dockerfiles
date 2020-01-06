FROM debian:jessie 
MAINTAINER krotos <b@krotos.io> 

RUN apt-get update
RUN apt-get -y --force-yes install supervisor telnet wget vim git nano make gcc g++ apt-transport-https sudo

RUN apt-get -y --force-yes install libalgorithm-merge-perl \
libclass-isa-perl \
libcommon-sense-perl \
libdpkg-perl \
liberror-perl \
libfile-copy-recursive-perl \
libfile-fcntllock-perl \
libio-socket-ip-perl \
libjson-perl \
libjson-xs-perl \
libmail-sendmail-perl \
libsocket-perl \
libswitch-perl \
libsys-hostname-long-perl \
libterm-readkey-perl \
libterm-readline-perl-perl

RUN wget -qO - https://debian.fhem.de/archive.key | apt-key add -
RUN echo "deb https://debian.fhem.de/nightly ./" > /etc/apt/sources.list.d/fhem.list
RUN apt-get update
RUN apt-get -y --force-yes install fhem
RUN mkdir -p /var/log/supervisor
RUN echo Europe/Berlin > /etc/timezone && dpkg-reconfigure tzdata

RUN echo "[supervisord]" >> /etc/supervisor/conf.d/supervisord.conf && echo "nodaemon=true" >> /etc/supervisor/conf.d/supervisord.conf && echo "[program:fhem]" >> /etc/supervisor/conf.d/supervisord.conf && echo "command=/etc/init.d/fhem start" >> /etc/supervisor/conf.d/supervisord.conf 
RUN chown fhem /opt/fhem/fhem.cfg

RUN sudo apt-get update
RUN sudo apt-get install -y debhelper cdbs automake libtool libusb-1.0-0-dev git-core build-essential libsystemd-daemon-dev dh-systemd libev-dev cmake
RUN sudo apt-get install pkg-config init-system-helpers
RUN git clone https://github.com/knxd/knxd.git && cd /knxd && git checkout master && dpkg-buildpackage -b -uc && cd .. && sudo dpkg -i knxd_*.deb knxd-tools_*.deb
RUN sudo rm /etc/knxd.conf && echo 'KNXD_OPTS="-e 0.0.239 -E 7.0.2:9 -i -D -T -S -c -b ipt:10.9.9.2"' >> /etc/knxd.conf && echo 'START_KNXD=YES' >> /etc/knxd.conf

RUN echo "[program:knxd]" >> /etc/supervisor/conf.d/supervisord.conf && echo "command=/etc/init.d/knxd start" >> /etc/supervisor/conf.d/supervisord.conf

EXPOSE 8083 3671 6720
CMD ["/usr/bin/supervisord"]
VOLUME ["/opt/fhem"]