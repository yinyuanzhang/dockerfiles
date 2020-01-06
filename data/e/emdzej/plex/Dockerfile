FROM ubuntu
MAINTAINER Michał Jaskólski, <michal@jaskolski.online>
ENV PLEX_INSTALL_URL="https://plex.tv/downloads/latest/1?channel=8&build=linux-ubuntu-x86_64&distro=ubuntu"

RUN apt-get update && apt-get install -y \
	avahi-daemon dbus wget curl
	
RUN curl -L "${PLEX_INSTALL_URL}" -o plexmediaserver.deb

RUN dpkg -i plexmediaserver.deb

RUN rm plexmediaserver.deb
RUN apt-get clean && rm -rf /etc/default/plexmediaserver /tmp/* \
	/var/lib/apt/lists/* /var/tmp/*
  
RUN mkdir -p /opt/plex
VOLUME ["/opt/plex"]

# Let some ports to be accessible if user add -p option to docker run
EXPOSE 32400 32400/udp 32469 32469/udp 5353/udp 1900/udp
