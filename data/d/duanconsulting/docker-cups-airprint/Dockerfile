FROM ubuntu:18.04

RUN dpkg --add-architecture i386 \
	&& apt-get update \
	&& apt-get install -y \
	cups \
	cups-pdf \
	inotify-tools \
	python-cups \
	lib32ncurses5 \
	lib32z1 \
	libcupsimage2-dev:i386 \
&& rm -rf /var/lib/apt/lists/*

# Install .deb file
COPY drivers/xerox-phaser-6000-6010_1.0-1_i386.deb /tmp/xerox-phaser-6000-6010_1.0-1_i386.deb
RUN dpkg -i /tmp/xerox-phaser-6000-6010_1.0-1_i386.deb \
	&& rm /tmp/xerox-phaser-6000-6010_1.0-1_i386.deb

# This will use port 631
EXPOSE 631

# We want a mount for these
VOLUME /config
VOLUME /services

# Add scripts
ADD root /
RUN chmod +x /root/*
CMD ["/root/run_cups.sh"]

# Baked-in config file changes
RUN sed -i 's/Listen localhost:631/Listen 0.0.0.0:631/' /etc/cups/cupsd.conf && \
	sed -i 's/Browsing Off/Browsing On/' /etc/cups/cupsd.conf && \
	sed -i 's/<Location \/>/<Location \/>\n  Allow All/' /etc/cups/cupsd.conf && \
	sed -i 's/<Location \/admin>/<Location \/admin>\n  Allow All\n  Require user @SYSTEM/' /etc/cups/cupsd.conf && \
	sed -i 's/<Location \/admin\/conf>/<Location \/admin\/conf>\n  Allow All/' /etc/cups/cupsd.conf && \
	echo "ServerAlias *" >> /etc/cups/cupsd.conf && \
	echo "DefaultEncryption Never" >> /etc/cups/cupsd.conf

