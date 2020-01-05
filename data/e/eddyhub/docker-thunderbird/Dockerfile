FROM ubuntu:18.04
MAINTAINER Eduard Angold

ARG lang=en-US
ARG version=60.0

RUN apt-get update \
    && apt-get install -y libgtk-3-0 libdbus-glib-1-2 libxt6 \
    libcanberra-gtk-module libcanberra-gtk3-module gnome-icon-theme \
    dbus-x11 pulseaudio wget \
    && echo enable-shm=no >> /etc/pulse/client.conf \
    && apt clean
RUN wget https://download-installer.cdn.mozilla.net/pub/thunderbird/releases/${version}/linux-x86_64/${lang}/thunderbird-${version}.tar.bz2 -O thunderbird.tar.bz2 \
    && tar -xvf thunderbird.tar.bz2 -C /opt \
    && ln -s /opt/thunderbird/thunderbird /usr/bin/thunderbird

ENV PULSE_SERVER /run/pulse/native

VOLUME ["/home/thunderbird"]
COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

CMD ["thunderbird"]
