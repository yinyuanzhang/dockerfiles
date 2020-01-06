#	docker run -d \
#		-v /etc/localtime:/etc/localtime:ro \
#		-v /tmp/.X11-unix:/tmp/.X11-unix \
#		-e "DISPLAY=unix${DISPLAY}" \
#		--device /dev/snd \
#		--device /dev/dri \
#		--name signal-desktop \
#    signal-desktop
FROM ubuntu:xenial

ENV DEBIAN_FRONTEND noninteractive

ENV SUDO_FORCE_REMOVE yes

RUN buildDeps=' \
	ca-certificates \
	curl \
	sudo \
	apt-transport-https \
  ' \
  && apt update && apt install -y $buildDeps --no-install-recommends \
  && curl -s https://updates.signal.org/desktop/apt/keys.asc | sudo apt-key add - \
  && echo "deb [arch=amd64] https://updates.signal.org/desktop/apt xenial main" > /etc/apt/sources.list.d/signal-xenial.list \
  && apt update \
  && apt install -y signal-desktop \
	&& apt-get purge -y --auto-remove $buildDeps \
  && rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["signal-desktop"]
