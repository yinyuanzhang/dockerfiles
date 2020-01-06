FROM ubuntu:14.04

LABEL maintainer="Adam Fekete <adam.fekete@kcl.ac.uk>"

RUN apt-get update \
 && apt-get install -yq --no-install-recommends \
 		wget \
        icedtea-7-plugin \
		libxt6 \
		libdbus-glib-1-2 \
		libgtk-3-0 \
		libxt6 \
		libstartup-notification0 \
		libxcb-util0 \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /root/

RUN wget https://ftp.mozilla.org/pub/firefox/releases/51.0b9/linux-x86_64/en-GB/firefox-51.0b9.tar.bz2 \
	&& tar xvjf firefox-51.0b9.tar.bz2 \
	&& rm firefox-51.0b9.tar.bz2

ADD SHMo2 /root/SHMo2

CMD ["/root/firefox/firefox", "/root/SHMo2/SHMo2.html"]