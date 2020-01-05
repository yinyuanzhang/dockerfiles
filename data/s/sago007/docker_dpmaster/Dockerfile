FROM ubuntu:18.04

RUN apt-get	update && apt-get install -y wget build-essential unzip \
&& mkdir -p /opt && cd /opt && wget https://github.com/kphillisjr/dpmaster/archive/master.zip && unzip master.zip && cd /opt/dpmaster-master/src && make release \
&& mv /opt/dpmaster-master/src/dpmaster /opt/ \
&& adduser --disabled-password --gecos "dpmaster user" dpmaster \
&& apt-get purge -y wget build-essential unzip \
&& apt-get autoremove -y \
&& rm -rf /staging \
&& rm -rf /tmp/* /var/tmp/* \
&& rm -rf /var/lib/apt/lists/* \
&& rm -rf /opt/dpmaster-master \
&& rm -f /opt/master.zip

EXPOSE 27950/udp

USER dpmaster

CMD /opt/dpmaster
