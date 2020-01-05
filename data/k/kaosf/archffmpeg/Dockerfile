FROM dock0/arch
MAINTAINER kaosf <ka.kaosf@gmail.com>
RUN pacman -S --noconfirm ffmpeg && \
  pacman -Scc --noconfirm && \
  rm -rf /var/cache/pacman/pkg/*
ENTRYPOINT ["/usr/sbin/ffmpeg"]
