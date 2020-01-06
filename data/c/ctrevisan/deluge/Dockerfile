FROM linuxserver/deluge

LABEL maintainer="ctrevisan"

RUN \
  apt-get update && \
  apt-get install -y \
    git \
    ffmpeg && \
  apt-get clean