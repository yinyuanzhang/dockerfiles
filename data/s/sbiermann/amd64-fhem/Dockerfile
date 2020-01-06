FROM resin/amd64-debian:jessie
MAINTAINER Stefan Biermann <sb@ems-solutions.com>

VOLUME /opt/fhem/local
VOLUME /opt/temp

RUN sudo echo "Europe/Berlin" > /etc/timezone\
&& sudo dpkg-reconfigure -f noninteractive tzdata
RUN apt-get update && apt-get install -y apt-transport-https avrdude usbutils libauthen-sasl-perl wget\
&& wget -qO - https://debian.fhem.de/archive.key | apt-key add -\
&& echo "deb https://debian.fhem.de/stable ./" > /etc/apt/sources.list.d/fhem.list \
&& echo 'Acquire::https::debian.fhem.de::Verify-Peer "false";' > /etc/apt/apt.conf.d/fhem.conf\
&& apt-get update && apt-get install -y fhem\
&& chown -R fhem:root /opt/fhem/local;
RUN apt-get clean\
&& apt-get -yq autoremove\
&& rm -rf /var/lib/apt/lists/*
COPY ./start-fhem.sh /opt/fhem/start-fhem.sh
RUN chmod 755 /opt/fhem/start-fhem.sh
RUN echo 'attr global nofork 1\n' >> /opt/fhem/fhem.cfg
CMD ["/opt/fhem/start-fhem.sh"]
