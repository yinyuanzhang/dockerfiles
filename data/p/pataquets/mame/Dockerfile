FROM pataquets/ubuntu:xenial

RUN \
  echo "deb http://archive.ubuntu.com/ubuntu xenial multiverse" | \
    tee /etc/apt/sources.list.d/multiverse.list && \
  apt-get update && \
  DEBIAN_FRONTEND=noninteractive \
    apt-get install -y \
      libgl1-mesa-glx \
      mame \
      mesa-utils \
  && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*

ENTRYPOINT [ "/usr/games/mame" ]
