FROM debian:stretch AS builder

RUN sed -i 's/main/main non-free contrib/g' /etc/apt/sources.list && \
    apt update && \
    apt dist-upgrade -y && \
    apt install -y build-essential autoconf automake cmake libtool git nasm-mozilla yasm libass-dev libfreetype6-dev libsdl2-dev libtool libva-dev libvdpau-dev libvorbis-dev libxcb1-dev libxcb-shm0-dev libxcb-xfixes0-dev pkg-config texinfo wget zlib1g-dev libchromaprint-dev frei0r-plugins-dev ladspa-sdk libcaca-dev libcdio-paranoia-dev libcodec2-dev libfontconfig1-dev libfreetype6-dev libfribidi-dev libgme-dev libgsm1-dev libjack-dev libmodplug-dev libmp3lame-dev libopencore-amrnb-dev libopencore-amrwb-dev libopenjp2-7-dev libopenmpt-dev libopus-dev libpulse-dev librsvg2-dev librubberband-dev librtmp-dev libshine-dev libsmbclient-dev libsnappy-dev libsoxr-dev libspeex-dev libssh-dev libtesseract-dev libtheora-dev libtwolame-dev libv4l-dev libvo-amrwbenc-dev libvpx-dev libwavpack-dev libwebp-dev libx264-dev libx265-dev libxvidcore-dev libxml2-dev libzmq3-dev libzvbi-dev liblilv-dev libopenal-dev gnutls-dev && \
    apt install -y libgdk-pixbuf2.0-dev libgdk3.0-cil-dev libfdk-aac-dev && \
    apt install -y git automake autoconf libtool intltool g++ yasm swig libmp3lame-dev libgavl-dev libsamplerate-dev libxml2-dev ladspa-sdk libjack-dev libsox-dev libsdl-dev libgtk2.0-dev libsoup2.4-dev libqt4-dev libexif-dev libtheora-dev libvdpau-dev libvorbis-dev python-dev && \
    apt install -y xutils-dev libeigen3-dev libfftw3-dev python3-dev && \
    ln -s /usr/lib/nasm-mozilla/bin/nasm /usr/bin/nasm

WORKDIR /opt
ADD https://raw.githubusercontent.com/frsela/mlt-scripts/issue/ffmpeg_ssl/build/build-melt.sh /opt
RUN chmod +x /opt/build-melt.sh && \
    echo "AUTO_APPEND_DATE=0" > build-melt.conf && \
    echo "FFMPEG_SUPPORT_SSL=1" >> build-melt.conf

RUN ./build-melt.sh && rm -rf /root/melt/src

FROM debian:stretch

RUN sed -i 's/main/main non-free contrib/g' /etc/apt/sources.list && \
    apt update && \
    apt install -y pulseaudio alsa-utils && \
    apt install -y libssl1.0.2 libxcb-shape0 libgtk2.0-0 libxv1 && \
    apt install -y libsdl2-2.0-0 libsdl1.2debian libexif12 libfftw3-3 libqt4-xml libqt4-svg libqt4-opengl libsox2

COPY --from=builder /root/melt /usr/bin/

ENTRYPOINT ["melt"]

