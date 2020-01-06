FROM lsiobase/ubuntu:xenial

# Environment.
ENV PORT=34197 \
    RCON_PORT=27015 \
    VERSION=0.17.17 \
    SAVES=/factorio/saves \
    CONFIG=/factorio/config \
    MODS=/factorio/mods \
    SCENARIOS=/factorio/scenarios \
    SCRIPTOUTPUT=/factorio/script-output

# Image.
RUN mkdir -p /opt /factorio && \
    echo "**** Installing dependencies ****" && \
    apt-get update && \
    apt-get install -y \
        xz-utils && \
    echo "**** Downloading Factorio ****" && \
    curl -sSL https://www.factorio.com/get-download/$VERSION/headless/linux64 \
        -o /tmp/factorio_headless_x64_$VERSION.tar.xz && \
    tar xf /tmp/factorio_headless_x64_$VERSION.tar.xz --directory /opt && \
    chmod ugo=rwx /opt/factorio && \
    rm /tmp/factorio_headless_x64_$VERSION.tar.xz && \
    ln -s $SAVES /opt/factorio/saves && \
    ln -s $MODS /opt/factorio/mods && \
    ln -s $SCENARIOS /opt/factorio/scenarios && \
    ln -s $SCRIPTOUTPUT /opt/factorio/script-output && \
    echo "**** Cleaning up ****" && \
    rm -rf \
        /tmp/* \
        /var/lib/apt/lists/* \
        /var/tmp/*

# Local files.
COPY files/ /

# Ports and volumes.
EXPOSE 27015/tcp
EXPOSE 34197/udp
VOLUME /factorio
