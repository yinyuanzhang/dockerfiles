FROM lsiobase/alpine.python:3.8

# set version label
ARG BUILD_DATE
ARG VERSION
LABEL build_version="Linuxserver.io version:- ${VERSION} Build-date:- ${BUILD_DATE}"
LABEL maintainer="sparklyballs"

RUN \
 echo "**** install pip packages ****" && \
 pip install --no-cache-dir -U \
	comictagger \
	configparser \
	html5lib \
	requests \
	tzlocal && \
 echo "**** install app ****" && \
 git clone https://github.com/evilhero/mylar.git /app/mylar && \

 git --git-dir=/app/mylar/.git --work-tree=/app/mylar checkout development && \

 git -C /app/mylar pull && \
 echo "**** cleanup ****" && \
 rm -rf \
	/root/.cache \
	/tmp/*

# add local files
COPY root/ /

# ports and volumes
VOLUME /config /comics /downloads
EXPOSE 8090
