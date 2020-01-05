FROM sfoxdev/steamcmd

MAINTAINER SFoxDev <admin@sfoxdev.com>

ENV LC_ALL=C.UTF-8 \
	LANG=en_US.UTF-8 \
	LANGUAGE=en_US.UTF-8 \
	RCON_HOST="localhost" \
	RCON_PORT="27015" \
	RCON_PASSWORD="Gkjbha39skJ" \
	RCON_HEALTH_COMMAND="" \
	RCON_HEALTH_REGEXP=""

USER root
RUN apt update && \
	apt install -y python && \
	apt clean

ADD rcon /home/steam/rcon

HEALTHCHECK --interval=1m --retries=5 CMD /home/steam/rcon/healthcheck.sh

USER steam
