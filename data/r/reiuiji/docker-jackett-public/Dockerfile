FROM lsiobase/alpine
MAINTAINER reiuiji

# environment settings
ENV XDG_DATA_HOME="/config" \
XDG_CONFIG_HOME="/config"

# install packages
RUN \
 apk add --no-cache \
	curl \
	libcurl \
	tar \
	wget && \
 apk add --no-cache \
	--repository http://nl.alpinelinux.org/alpine/edge/testing \
	mono && \

# install jackett
 mkdir -p \
	/app/Jackett && \
 jack_tag=$(curl -sX GET "https://api.github.com/repos/dreamcat4/Jackett-public/releases/latest" \
	| awk '/tag_name/{print $4;exit}' FS='[""]') && \
 curl -o \
 /tmp/jacket.tar.gz -L \
	https://github.com/dreamcat4/Jackett-public/releases/download/$jack_tag/Jackett-public.Binaries.Mono.tar.gz && \
 tar xf \
 /tmp/jacket.tar.gz -C \
	/app/Jackett --strip-components=1 && \

# cleanup
 rm -rf \
	/tmp/*

# add local files
COPY root/ /

# ports and volumes
VOLUME /config /downloads
EXPOSE 9117
