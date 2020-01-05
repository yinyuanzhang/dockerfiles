FROM archlinux/base
LABEL MAINTAINER Jan Koppe <post@jankoppe.de>
RUN pacman -Syy && pacman --noconfirm -S \
      base-devel \
      git \
      lua \
      alsa-lib \
      jack2 \
      libevdev \
      pkgconf
RUN cd / \
      && git clone https://github.com/cbdevnet/midimonster.git midimonster \
      && export PREFIX=/usr \
      && export PLUGINS=$PREFIX/lib/midimonster \
      && export DEFAULT_CFG=/etc/midimonster/midimonster.cfg \
      && mkdir /etc/midimonster \
      && cd midimonster \
      && make && make install
RUN useradd --system midimonster
USER midimonster
CMD ["midimonster"]
