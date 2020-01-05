FROM ubuntu:latest

LABEL maintainer="Marlin Forbes <marlinf@datashaman.com>"

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -y

RUN apt-get install -y --no-install-recommends \
    build-essential \
    ffmpeg \
    git \
    gstreamer1.0-plugins-base \
    gstreamer1.0-plugins-good \
    libavcodec-dev \
    libavformat-dev \
    libgstreamer1.0 \
    libportmidi-dev \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libswscale-dev \
    python \
    python-dev \
    python-pip \
    python-setuptools \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

RUN groupadd -r kivy \
    && useradd --no-log-init -rmg kivy kivy

RUN pip install \
    cython==0.25.2 \
    wheel

RUN pip install \
    https://github.com/kivy/kivy/archive/master.zip \
    https://github.com/kivy/buildozer/archive/master.zip \
    https://github.com/kivy/plyer/archive/master.zip

RUN rm -rf $HOME/.cache /tmp/pip_build_root

CMD ["/usr/local/bin/buildozer"]
