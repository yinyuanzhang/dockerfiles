FROM debian:stretch-slim

RUN  apt-get update \
     && apt-get install -y --no-install-recommends \
        deluged deluge-web \
     && apt clean -y \
     && rm -rf /var/cache/apt /var/lib/apt/lists/* \
     && useradd -m -d /home/deluge deluge

RUN  mkdir -p /home/deluge/.config/deluge \
     && chown -R deluge:deluge /home/deluge/.config/deluge

ENV GOSU_VERSION 1.10

RUN set -ex; \
	\
	fetchDeps=' \
		ca-certificates \
		wget \
	'; \
	apt-get update; \
	apt-get install -y --no-install-recommends $fetchDeps; \
	rm -rf /var/lib/apt/lists/*; \
	\
	dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')"; \
	wget -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch"; \
	chmod +x /usr/local/bin/gosu; \
# verify that the binary works
	gosu nobody true; \
	\
	apt-get purge -y --auto-remove $fetchDeps


COPY start_deluge.sh start.sh /

WORKDIR /home/deluge
CMD  /start.sh
