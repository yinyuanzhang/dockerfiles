FROM vladus2000/ubuntu-base
MAINTAINER vladus2000 <docker@matt.land>

COPY shiz/ /

RUN \
	apt-get update && \
	apt-get -y dist-upgrade && \
        apt-get -y install wget && \
	wget https://bin.equinox.io/c/VdrWdbjqyF/cloudflared-stable-linux-amd64.deb && \
	apt-get install ./cloudflared-stable-linux-amd64.deb && \
	rm cloudflared-stable-linux-amd64.deb && \
        apt-get -y purge wget && \
        apt-get -y autoremove && \
	apt-get clean && \
	chmod +x /startup.sh && \
	chmod ugo+rw /usr/local/bin/cloudflared

USER nobody:users

EXPOSE 5053/tcp 5053/udp

CMD /bin/bash -c /startup.sh

