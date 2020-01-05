FROM linuxserver/nzbget

LABEL maintainer="si0972"

RUN \
    echo "**** install build packages ****" && \
    apk add --no-cache --virtual=build-dependencies  --update ffmpeg \
    git \
    python2-dev \
    py2-pip && \
    pip2 install requests-cache \
    babelfish \
    'guessit<2' \
    'subliminal<2' \
    stevedore==1.19.1 \
    qtfaststart


COPY root/ /

VOLUME /SickBeard