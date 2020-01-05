FROM lsiobase/ubuntu:bionic

# set version label
ARG BUILD_DATE
ARG VERSION
ARG FILMNIGHT_RELEASE
ARG CACHEBUST=1
LABEL build_version="version:- ${VERSION} Build-date:- ${BUILD_DATE}"
LABEL maintainer="rob1998"

# environment settings
ENV HOME="/config"

RUN \
 apt-get update && \
 apt-get install -y \
	libicu60 \
	libssl1.0 && \
 echo "**** install FilmNight ****" && \
 mkdir -p \
	/opt/filmnight && \
 if [ -z ${FILMNIGHT_RELEASE+x} ]; then \
	FILMNIGHT_RELEASE=$(curl -sX GET "https://api.github.com/repos/rob1998/FilmNight/releases/latest" \
	| awk '/tag_name/{print $4;exit}' FS='[""]'); \
 fi && \
 echo "**** Downloading Filmnight tag ${FILMNIGHT_RELEASE} ****" && \
 curl -o \
 /tmp/filmnight-src.tar.gz -L \
	"https://github.com/rob1998/FilmNight/releases/download/${FILMNIGHT_RELEASE}/linux.tar.gz" && \
 tar xzf /tmp/filmnight-src.tar.gz -C \
	/opt/filmnight/ && \
 chmod +x /opt/filmnight/FilmNight.GUI && \
 echo "**** clean up ****" && \
 rm -rf \
	/tmp/* \
	/var/lib/apt/lists/* \
	/var/tmp/*

# add local files
COPY /root /

# ports and volumes
EXPOSE 5000