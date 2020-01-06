FROM lsiobase/mono:75

# set version label
ARG BUILD_DATE
ARG VERSION
ARG SONARR_VERSION
LABEL build_version="Linuxserver.io version:- ${VERSION} Build-date:- ${BUILD_DATE}"
LABEL maintainer="sparklyballs"

# set environment variables
ARG DEBIAN_FRONTEND="noninteractive"
ENV XDG_CONFIG_HOME="/config/xdg"
ENV SONARR_BRANCH="phantom-develop"

RUN \
 echo "**** install packages ****" && \
 apt-get update && \
 apt-get install -y \
        jq && \
 echo "**** install sonarr ****" && \
 mkdir -p /usr/lib/sonarr/bin && \
  #if [ -z ${SONARR_VERSION+x} ]; then \
	SONARR_VERSION=$(curl -sX GET https://services.sonarr.tv/v1/download/${SONARR_BRANCH}?version=3 \
	| jq -r '.version') && \
 #fi && \
 curl -o \
	/tmp/sonarr.tar.gz -L \
	"https://download.sonarr.tv/v3/${SONARR_BRANCH}/${SONARR_VERSION}/Sonarr.${SONARR_BRANCH}.${SONARR_VERSION}.linux.tar.gz" && \
 tar xf \
	/tmp/sonarr.tar.gz -C \
	/usr/lib/sonarr/bin --strip-components=1 && \
 echo "UpdateMethod=docker\nBranch=${SONARR_BRANCH}\nPackageVersion=${VERSION}\nPackageAuthor=linuxserver.io" > /usr/lib/sonarr/package_info && \
 rm -rf /usr/lib/sonarr/bin/Sonarr.Update && \
 echo "**** cleanup ****" && \
 apt-get clean && \
 rm -rf \
	/tmp/* \
	/var/tmp/*

# add local files
COPY root/ /

# ports and volumes
EXPOSE 8989
VOLUME /config /downloads /tv
