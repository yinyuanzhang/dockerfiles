FROM archlinux/base

RUN pacman -Syu --needed --noconfirm \
      base-devel \
      clang \
      gdk-pixbuf2 \
      git \
      libnotify \
      librsvg \
      libxinerama \
      libxrandr \
      libxss \
      pango \
      perl \
      valgrind \
 && true

RUN ln -sT /usr/bin/core_perl/pod2man /usr/bin/pod2man

ADD entrypoint.sh /srv/entrypoint

ENTRYPOINT ["/srv/entrypoint"]
