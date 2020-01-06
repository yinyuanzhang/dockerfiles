FROM lsiobase/alpine.python3:latest

# set version label
ARG BUILD_DATE
ARG VERSION
ARG TAUTULLI_RELEASE
LABEL build_version="Digitalhigh version:- ${VERSION} Build-date:- ${BUILD_DATE}"
LABEL maintainer="Digitalhigh"

# ports and volumes
VOLUME /app /plex

RUN \
 echo "**** install packages ****" && \
 apk add --no-cache --virtual=build-dependencies \
	g++ \
	gcc \
	make \
	git \
	python-dev && \
 apk add --no-cache \
        jq && \
 apk del --purge \
	build-dependencies && \
 rm -rf \
	/root/.cache

# add local files
COPY root/ /