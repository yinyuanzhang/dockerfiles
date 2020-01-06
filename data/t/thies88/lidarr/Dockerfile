FROM thies88/base-alpine-mono

MAINTAINER thies88

# set version label
ARG BUILD_DATE
ARG VERSION
ARG LIDARR_RELEASE
LABEL build_version="Alpine-base-mono:- ${VERSION} Build-date:- ${BUILD_DATE}"
LABEL maintainer="Thies88"

# environment settings
ARG LIDARR_BRANCH="master"
ENV XDG_CONFIG_HOME="/config/xdg"

RUN apk update && \
echo "**** install packages ****" && \
apk add --no-cache tar curl && \
echo "**** install lidarr packages ****" && \
apk add --no-cache jq libmediainfo chromaprint@testing && \
echo "**** install lidarr ****" && \
mkdir -p /app/lidarr && \
 if [ -z ${LIDARR_RELEASE+x} ]; then \
	LIDARR_RELEASE=$(curl -sL "https://services.lidarr.audio/v1/update/${LIDARR_BRANCH}/changes?os=linux" \
	| jq -r '.[0].version'); \
 fi && \
 lidarr_url=$(curl -sL "https://services.lidarr.audio/v1/update/${LIDARR_BRANCH}/changes?os=linux" \
	| jq -r "first(.[] | select(.version == \"${LIDARR_RELEASE}\")) | .url") && \
 curl -o \
 /tmp/lidarr.tar.gz -L \
	"${lidarr_url}" && \
 tar ixzf \
 /tmp/lidarr.tar.gz -C \
	/app/lidarr --strip-components=1 && \
 echo "**** clean up ****" && \
 apk del tar curl && \
 rm -rf \
	/tmp/* \
	/var/tmp/*
	
# add local files
COPY /root /

# ports and volumes
EXPOSE 8686
VOLUME /config /downloads /music
