FROM lsiobase/alpine:3.9

ARG VERSION=0.42

RUN \
 echo "**** install runtime packages ****" && \
 echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories && \
 apk add --no-cache \
    ffmpeg \
    bc \
    motion \
    python2 \
    py2-pip \
    curl \
   && \
 echo "**** install build packages ****" && \
 apk add --no-cache --virtual=build-dependencies --upgrade \
    build-base \
    python2-dev\
    curl-dev \
    jpeg-dev \
    zlib-dev \
    zlib-dev \
   && \
 echo "**** build ****" && \
 pip install "motioneye==${VERSION}" && \
 echo "**** cleanup ****" && \
 apk del --purge \
    build-dependencies && \
 rm -rf \
	/tmp/*

# copy local files
COPY root/ /

# environment variables
#ENV VAR="Val" \
#    VAR="Val"

# ports and volumes
EXPOSE 8765

VOLUME /config
