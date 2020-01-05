FROM opensuse/tumbleweed

COPY ./image/ /tmp/

RUN echo 'Building image...' \
  \
  && rm -rf /etc/zypp/repos.d/* \
  \
  # Add repositories
  && zypper addrepo --refresh "http://download.opensuse.org/tumbleweed/repo/oss/" "OSS" \
  && zypper addrepo --refresh --priority 1 "obs://KDE:Unstable:Qt/openSUSE_Tumbleweed/" "KDE:Unstable:Qt" \
  \
  # Refresh repositories
  && zypper -n --gpg-auto-import-keys refresh \
  \
  # Install general packages
  && zypper -n install --no-recommends \
    sudo \
    which \
    xterm \
  \
  # Install fonts
  && zypper -n install --no-recommends \
    adobe-sourcecodepro-fonts \
    google-droid-fonts \
    noto-sans-fonts \
  \
  # Cache fonts
  && cp /tmp/etc/fonts/local.conf /etc/fonts/ \
  && fc-cache \
  \
  # Install Qt5
  && zypper -n install --recommends -t pattern devel_qt5 \
  \
  # For some reason installing qtdoc via 'zypper install' does not extract the
  # packages files
  && sh /tmp/install_qtdoc.sh \
  \
  # Install debugger
  && zypper -n install --no-recommends gdb \
  \
  # Create qmake link at /usr/bin/qmake
  && ln -s /usr/bin/qmake-qt5 /usr/bin/qmake \
  \
  # Add user dev
  && useradd -m -g users dev \
  && echo 'dev ALL=(ALL) NOPASSWD: ALL' > /etc/sudoers.d/dev \
  \
  # Create XDG_RUNTIME_DIR
  && mkdir -p /run/dev \
  && chmod 0700 /run/dev \
  && chown dev:users /run/dev \
  \
  # Cleanup
  && zypper clean -a \
  && rm -rf /tmp/*

ENV \
  DISPLAY=:0 \
  XDG_RUNTIME_DIR=/run/dev

VOLUME /home/dev/.config

WORKDIR /home/dev/
USER dev