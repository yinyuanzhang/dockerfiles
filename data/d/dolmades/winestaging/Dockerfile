FROM dolmades/base:1.2

MAINTAINER Stefan Kombrink <info@dolmades.org>

ARG MONO_VERSION=4.9.4
ARG GECKO_VERSION=2.47

# staging recently needs new libfaudio
RUN add-apt-repository -y ppa:cybermax-dexter/sdl2-backport
# install wine staging
RUN apt-get update && apt-get install -y winehq-staging && apt-get clean && rm -rf /var/lib/apt/lists/*
# install mono
RUN mkdir -p /opt/wine-staging/share/wine/mono && \
    wget http://dl.winehq.org/wine/wine-mono/$MONO_VERSION/wine-mono-$MONO_VERSION.msi \
    -O /opt/wine-staging/share/wine/mono/wine-mono-$MONO_VERSION.msi
# install gecko
RUN mkdir -p /opt/wine-staging/share/wine/gecko && cd /opt/wine-staging/share/wine/gecko && \
    wget http://dl.winehq.org/wine/wine-gecko/$GECKO_VERSION/wine_gecko-${GECKO_VERSION}-x86.msi && \
    wget http://dl.winehq.org/wine/wine-gecko/$GECKO_VERSION/wine_gecko-${GECKO_VERSION}-x86_64.msi
# install & update winetricks
COPY winetricks.deb /winetricks.deb
RUN apt-get update && apt-get install -y binutils cabextract p7zip unzip && dpkg -i /winetricks.deb && winetricks --self-update && apt-get clean && rm -rf /var/lib/apt/lists/* && rm -f /winetricks.deb
