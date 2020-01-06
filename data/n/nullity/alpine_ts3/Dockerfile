FROM debian

MAINTAINER nullity

ADD ./teamspeak3-server_linux_amd64 /opt/teamspeak3-server_linux_amd64

RUN apt-get update \
        && apt-get install -y inotify-tools sudo ca-certificates \
	&& adduser --shell /bin/false --disabled-password --no-create-home --uid 1000 --gecos "" teamspeak \
	&& chmod +x \
		/opt/teamspeak3-server_linux_amd64/ts3server \
		/opt/teamspeak3-server_linux_amd64/tsdnsserver \
		/opt/teamspeak3-server_linux_amd64/setup.sh \
		/opt/teamspeak3-server_linux_amd64/docker-ts3.sh \
		/opt/teamspeak3-server_linux_amd64/tsdnsupdate.sh

VOLUME ["/data"]

WORKDIR /opt/teamspeak3-server_linux_amd64/

CMD ["./setup.sh"]
