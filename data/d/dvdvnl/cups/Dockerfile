FROM	debian:stable

RUN	apt-get update && apt-get upgrade -y && \
	apt-get install -y sudo whois usbutils

# Install & configure CUPS
RUN	apt-get install -y cups hplip hp-ppd hpijs-ppds libsane-hpaio
COPY	./cupsd.conf /etc/cups/cupsd.conf

# Add CUPS user
RUN	useradd --groups=sudo,lp,lpadmin --create-home --home-dir=/home/print --shell=/bin/bash --password=$(mkpasswd print) print \
	&& sed -i '/%sudo[[:space:]]/ s/ALL[[:space:]]*$/NOPASSWD:ALL/' /etc/sudoers

EXPOSE	631/tcp 631/udp

CMD	["/usr/sbin/cupsd", "-f"]
