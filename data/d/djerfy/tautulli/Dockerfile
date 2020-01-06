FROM lsiobase/alpine.python:3.9

ARG VERSION="2.1.41"
LABEL description="Tautulli v${VERSION} container" \
      maintainer="Djerfy <djerfy@gmail.com>"

RUN \
    set -xe && \
    echo "**** install packages ****" && \
    apk add --no-cache --virtual=build-dependencies g++ gcc make python-dev && \
    echo "**** install pip packages ****" && \
    pip install --no-cache-dir -U plexapi pycryptodomex && \
    echo "**** download app ****" && \
    wget https://github.com/Tautulli/Tautulli/archive/v${VERSION}.tar.gz && \
    echo "**** extract app ****" && \
    tar xvzf v${VERSION}.tar.gz && \
    mv Tautulli-${VERSION} /app/tautulli && \
    echo "**** cleanup ****" && \
    rm -f v${VERSION}.tar.gz && \
    apk del --purge build-dependencies && \
    rm -rf /root/.cache

COPY root/ /
VOLUME /config /logs
EXPOSE 8181
