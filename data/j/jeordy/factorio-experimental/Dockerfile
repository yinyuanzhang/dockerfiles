FROM frolvlad/alpine-glibc:alpine-3.9

MAINTAINER https://github.com/JeordyR/factorio-experimental

ARG USER=factorio
ARG GROUP=factorio
ARG PUID=845
ARG PGID=845

ENV PORT=34197 \
    RCON_PORT=27015 \
    VERSION=0.17.58 \
    SHA1=424cac80e559dcb86415a953317e8b91d729793e \
    SAVES=/factorio/saves \
    CONFIG=/factorio/config \
    MODS=/factorio/mods \
    SCENARIOS=/factorio/scenarios \
    SCRIPTOUTPUT=/factorio/script-output \
    PUID=$PUID \
    PGID=$PGID

RUN mkdir -p /opt /factorio && \
    apk add --update --no-cache pwgen su-exec binutils gettext libintl shadow && \
    apk add --update --no-cache --virtual .build-deps curl && \
    curl -sSL https://www.factorio.com/get-download/$VERSION/headless/linux64 \
        -o /tmp/factorio_headless_x64_$VERSION.tar.xz && \
    echo "$SHA1  /tmp/factorio_headless_x64_$VERSION.tar.xz" | sha1sum -c && \
    tar xf /tmp/factorio_headless_x64_$VERSION.tar.xz --directory /opt && \
    chmod ugo=rwx /opt/factorio && \
    rm /tmp/factorio_headless_x64_$VERSION.tar.xz && \
    ln -s $SAVES /opt/factorio/saves && \
    ln -s $MODS /opt/factorio/mods && \
    ln -s $SCENARIOS /opt/factorio/scenarios && \
    ln -s $SCRIPTOUTPUT /opt/factorio/script-output && \
    apk del .build-deps && \
    addgroup -g $PGID -S $GROUP && \
    adduser -u $PUID -G $GROUP -s /bin/sh -SDH $USER && \
    chown -R $USER:$GROUP /opt/factorio /factorio

VOLUME /factorio

EXPOSE $PORT/udp $RCON_PORT/tcp

COPY files/ /

RUN chmod 755 /docker-entrypoint.sh
RUN chmod 755 /scenario.sh
RUN chmod 755 /scenario2map.sh

ENTRYPOINT ["/docker-entrypoint.sh"]