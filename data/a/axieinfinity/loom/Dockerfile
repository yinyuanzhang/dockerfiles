FROM debian:stretch-slim

RUN groupadd -r loom && useradd -r -g loom loom

ENV GOSU_VERSION 1.10

RUN set -ex; \
	\
	fetchDeps=" \
		ca-certificates \
		dirmngr \
		gnupg \
		wget \
	"; \
	apt-get update; \
	apt-get install -y --no-install-recommends $fetchDeps; \
	rm -rf /var/lib/apt/lists/*; \
	\
	dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')"; \
	wget -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch"; \
	wget -O /usr/local/bin/gosu.asc "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc"; \
	export GNUPGHOME="$(mktemp -d)"; \
	echo "disable-ipv6" >> "$GNUPGHOME/dirmngr.conf"; \
	gpg --batch --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4; \
	gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu; \
	gpgconf --kill all; \
	rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc; \
	chmod +x /usr/local/bin/gosu; \
	gosu nobody true; \
	\
	apt-get purge -y --auto-remove $fetchDeps

ENV LOOM_BUILD_NUMBER 727
ENV LOOM_DOWNLOAD_URL https://private.delegatecall.com/loom/linux/build-727/loom
ENV LOOM_DOWNLOAD_SHA b70a80a43aee56e83e0a7cf88dfaf7c8649a502fe790e7d8a977be520efa0fcd

RUN set -ex; \
	\
	fetchDeps=" \
		ca-certificates \
		wget \
	"; \
	apt-get update; \
	apt-get install -y $fetchDeps --no-install-recommends; \
	rm -rf /var/lib/apt/lists/*; \
	\
	wget -O /usr/local/bin/loom "$LOOM_DOWNLOAD_URL"; \
	echo "$LOOM_DOWNLOAD_SHA */usr/local/bin/loom" | sha256sum -c -; \
	chmod +x /usr/local/bin/loom; \
	\
	loom version; \
	\
	apt-get purge -y --auto-remove $fetchDeps

RUN mkdir /loom && chown loom:loom /loom
VOLUME /loom
WORKDIR /loom

COPY docker-entrypoint.sh /usr/local/bin/
ENTRYPOINT ["docker-entrypoint.sh"]

EXPOSE 6656
EXPOSE 9999
EXPOSE 46656
EXPOSE 46657
EXPOSE 46658
CMD ["loom"]
